from typing import Dict, TypedDict
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from src.tools.custom_tools import fetch_ado_and_confluence_deltas
from src.utils.rag_handler import DocRAGHandler

# Define the orchestration state contract
class AgentState(TypedDict):
    project_scope: str
    raw_deltas: str
    summary_report: str
    final_draft: str

class DocumentationGraphPipeline:
    def __init__(self):
        # Configure Gemini Flash for lightweight, ultra-fast structural parsing
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.1)
        self.rag_handler = DocRAGHandler()
        self.workflow = self._build_graph()

    def _analyzer_node(self, state: AgentState) -> Dict:
        """Agent Node 1: Scans integration environments and formats delta parameters."""
        
        # Call the LangChain tool directly
        raw_changes = fetch_ado_and_confluence_deltas.invoke({"project_scope": state["project_scope"]})
        
        analyzer_prompt = ChatPromptTemplate.from_template(
            "You are a Lead Release Intelligence Systems Analyst.\n"
            "Analyze the following raw engineering items and wiki modifications for scope: '{scope}'.\n"
            "Categorize updates cleanly into architectural variations, structural parameters changes, and bugs.\n\n"
            "Raw Platform Feed:\n{data}\n\n"
            "Output a structured markdown Summary Report containing exact item names and parameters."
        )
        
        chain = analyzer_prompt | self.llm
        response = chain.invoke({"scope": state["project_scope"], "data": raw_changes})
        
        return {"raw_deltas": raw_changes, "summary_report": response.content}

    def _drafter_node(self, state: AgentState) -> Dict:
        """Agent Node 2: Interrogates Chroma vector stores and generates clean revision logs."""
        # Querying vector embeddings based directly on extracted technical parameters
        context_data = self.rag_handler.query_knowledge_base(query=state["summary_report"], k=5)
        
        drafter_prompt = ChatPromptTemplate.from_template(
            "You are a Senior Technical Documentation Engineer and Information Architect.\n"
            "Analyze historical functional specifications from the current system blueprint data context:\n\n"
            "[ORIGINAL DOCUMENTATION BASELINE SYSTEM CONTEXT]\n{context}\n\n"
            "Now review the specific changes targeted for application by the Systems Analyst:\n\n"
            "[NEW SUMMARY REPORT DELTAS]\n{summary}\n\n"
            "CRITICAL EXECUTIONS RULES:\n"
            "1. Pinpoint exactly which headers, files, or functional parameter zones within the context require updating.\n"
            "2. Generate clear Markdown revisions showing precise modification anchors (e.g., `[UPDATE FOR SECTION X]`).\n"
            "3. Ensure configuration flags, environment rules, and target dependencies match the new changes perfectly.\n"
            "4. Retain all unrelated paragraphs from the original text completely. Avoid content gaps.\n\n"
            "Drafted System Update Revisions:"
        )
        
        chain = drafter_prompt | self.llm
        response = chain.invoke({"context": context_data, "summary": state["summary_report"]})
        
        return {"final_draft": response.content}

    def _build_graph(self):
        """Builds a deterministic sequential execution graph topology."""
        builder = StateGraph(AgentState)
        
        builder.add_node("release_analyzer", self._analyzer_node)
        builder.add_node("documentation_drafter", self._drafter_node)
        
        builder.set_entry_point("release_analyzer")
        builder.add_edge("release_analyzer", "documentation_drafter")
        builder.add_edge("documentation_drafter", END)
        
        return builder.compile()

    def run_pipeline(self, scope_context: str) -> str:
        """Executes the compiled multi-agent state lifecycle engine."""
        initial_state: AgentState = {
            "project_scope": scope_context,
            "raw_deltas": "",
            "summary_report": "",
            "final_draft": ""
        }
        
        final_output = self.workflow.invoke(initial_state)
        return final_output["final_draft"]