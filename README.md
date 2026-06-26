Here is a highly professional, structured, and visually impressive `README.md` file for your project. It includes placeholder badges, a clear architecture breakdown, and setup instructions to make it stand out on a platform like GitHub.

You can copy and paste this directly into a `README.md` file in your root folder.

---

```markdown
# 🤖 Multi-Agent Technical Documentation Automation Engine

![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.45.0-FF4B4B.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-0.0.30-success.svg)
![Gemini API](https://img.shields.io/badge/Google_Gemini-2.5_Flash-orange.svg)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Store-1A2B3C.svg)

An end-to-end, multi-agent AI pipeline designed to automate the reconciliation of engineering release notes with existing technical documentation. By cross-referencing incoming Azure DevOps (ADO) and Confluence deltas against a baseline PDF manual, this system mitigates content drift and eliminates manual tracking.

---

## 📖 Overview

Technical writing and engineering teams often face a disconnect between fast-paced release cycles and static documentation updates. This project bridges that gap by deploying autonomous AI agents that read raw engineering tickets, summarize the technical changes, and intelligently map them to the exact sections of a system's existing user manual or architecture guide.

**The result?** A clean, precise Markdown revision log and a downloadable Word Document draft, generated in seconds without LLM hallucination.

---

## 🏗️ System Architecture

The pipeline leverages a deterministic state machine via **LangGraph** to ensure agents act sequentially and consistently.

1. **Phase 1: RAG Ingestion (The Foundation)**
   - Uploads a baseline PDF manual.
   - Chunks and vectorizes the structural layout using `gemini-embedding-001`.
   - Stores the embeddings in a local `ChromaDB` vector database.
2. **Phase 2: Extraction & Analysis (Agent Node 1)**
   - Simulates a connection to ADO & Confluence spaces to fetch raw sprint deltas.
   - The **Release Analyzer Agent** sanitizes the raw data, categorizing changes into architectural variations, parameter updates, and bugs.
3. **Phase 3: Contextual Mapping & Drafting (Agent Node 2)**
   - The **Documentation Drafter Agent** queries the vector database using the sanitized delta summary.
   - Merges the historical context with the new changes to generate pinpoint insertion instructions.
4. **Phase 4: Delivery**
   - Outputs a UI-rendered Markdown log.
   - Generates downloadable `.md` and `.docx` files for immediate team handoff.

---

## ✨ Key Features

* **Zero-Hallucination Drafting:** Strictly grounded in the uploaded baseline PDF using Retrieval-Augmented Generation (RAG).
* **Deterministic Workflow:** LangGraph orchestration prevents agent loops and ensures a strict step-by-step logic path.
* **Modern Embedding Models:** Built on Google's unified `gemini-embedding-001` infrastructure for highly accurate semantic search.
* **Interactive Frontend:** A sleek, reactive Streamlit dashboard built for immediate user adoption.
* **Multi-Format Export:** Natively supports `.md` and `.docx` generation for easy integration into existing drafting workflows (like MadCap Flare or Word).

---

## 🛠️ Tech Stack

* **Language:** Python
* **Frontend:** Streamlit
* **AI Orchestration:** LangGraph, LangChain 0.3
* **LLM & Embeddings:** Google GenAI (`gemini-2.5-flash`, `gemini-embedding-001`)
* **Vector Database:** ChromaDB
* **Document Processing:** PyPDF, python-docx

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/doc_updater_project.git](https://github.com/yourusername/doc_updater_project.git)
cd doc_updater_project

```

### 2. Create a Virtual Environment

It is highly recommended to use a virtual environment to prevent dependency conflicts.

```bash
python -m venv venv

```

* **Windows:** `venv\Scripts\activate`
* **Mac/Linux:** `source venv/bin/activate`

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Configure Environment Variables

Create a file named exactly `.env` in the root directory and add your Google Gemini API key:

```env
GEMINI_API_KEY=your_actual_api_key_here

# (Optional for future live API connections)
ADO_ORGANIZATION=your_org
ADO_PROJECT=your_project
ADO_PAT=your_personal_access_token
CONFLUENCE_URL=[https://your-domain.atlassian.net](https://your-domain.atlassian.net)
CONFLUENCE_API_TOKEN=your_confluence_token

```

### 5. Run the Application

```bash
streamlit run app.py

```

*The Streamlit interface will automatically launch in your default web browser.*

---

## 💡 Usage Guide

1. **Configure Sprint Target:** In the left sidebar, enter the target engineering milestone or sprint scope (e.g., "Sprint 24 - Core Infrastructure").
2. **Upload Baseline Document:** Upload your current system manual or documentation as a `.pdf` file.
3. **Trigger Pipeline:** Click the primary action button to begin the ingestion and extraction process.
4. **Review & Download:** Review the suggested edits generated on-screen and download the resulting Markdown or Word Document for final manual review.

---

## 🔮 Future Roadmap

* [ ] Transition `custom_tools.py` from mock data to live Atlassian Python API and Azure DevOps REST API connections.
* [ ] Implement advanced chunking strategies to preserve complex table structures from original PDFs.
* [ ] Add direct GitHub/GitLab PR generation for automated deployment to documentation repositories.

---

## 👤 Author

**C Vishnu Vardhan** *AI/ML Engineer & Technical Writer* Passionate about bridging the gap between complex software engineering workflows and clear, scalable technical documentation.

```

```
