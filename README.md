<div align="center">

<!-- HEADER BANNER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1a1a2e,50:16213e,100:0f3460&height=200&section=header&text=Ivanti%20Doc%20Engine&fontSize=48&fontColor=e94560&fontAlignY=38&desc=Multi-Agent%20Technical%20Documentation%20Automation&descAlignY=58&descSize=16&descColor=a8b2d8" width="100%"/>

<!-- BADGES -->
<p>
  <img src="https://img.shields.io/badge/Python-3.14+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-1.45.0-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/LangGraph-0.0.30-2ECC71?style=for-the-badge&logo=graphql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Gemini_2.5_Flash-Google_AI-4285F4?style=for-the-badge&logo=google&logoColor=white"/>
  <img src="https://img.shields.io/badge/ChromaDB-Vector_Store-1A2B3C?style=for-the-badge&logo=databricks&logoColor=white"/>
</p>

<p>
  <img src="https://img.shields.io/badge/Status-Active-success?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat-square"/>
</p>

<br/>

> **Reconcile document variations and eliminate content drift** by cross-referencing baseline PDF manuals with live engineering pipeline updates — automatically, accurately, at scale.

<br/>

</div>

---

## 🔴 The Problem

Engineering teams ship fast. Documentation doesn't keep up.

Every sprint introduces new parameters, deprecated endpoints, and architectural shifts — but the system manual stays frozen in the past. Technical writers spend hours manually hunting down what changed, where it lives in the existing docs, and how to rewrite it without breaking context.

**This engine eliminates that entire process.**

---

## ⚡ What It Does

```
Upload PDF Manual  →  Vectorize Structure  →  Fetch Sprint Deltas  →  Map Changes  →  Export Draft
```

The pipeline ingests your baseline documentation, semantically understands its structure, pulls raw engineering changes from ADO/Confluence, and generates a precise Markdown revision log — pinpointing exactly which sections need to be updated and how.

**Zero hallucination. Deterministic output. Downloadable in seconds.**

---

## 🖥️ Interface Preview

<div align="center">
<table>
<tr>
<td align="center">

**Pipeline Controls**
- 🔑 API credentials auto-loaded
- 🎯 Sprint scope configuration
- 📋 4-step operational pipeline display
- 📄 PDF baseline uploader

</td>
<td align="center">

**Output Delivery**
- 📝 Rendered Markdown revision log
- 💾 `.md` file download
- 📄 `.docx` file download
- ✅ Section-level change mapping

</td>
</tr>
</table>
</div>

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    LANGGRAPH STATE MACHINE               │
│                                                         │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────┐ │
│   │   PHASE 1    │───▶│   PHASE 2    │───▶│ PHASE 3  │ │
│   │ RAG Ingestion│    │  Extraction  │    │ Drafting │ │
│   └──────────────┘    └──────────────┘    └──────────┘ │
│          │                   │                  │       │
│     PDF Upload          ADO / Confluence    RAG Query  │
│     Chunking            Sprint Deltas       + Merge    │
│     ChromaDB            Categorization      Output     │
└─────────────────────────────────────────────────────────┘
                                                    │
                              ┌─────────────────────┤
                              ▼                     ▼
                         Markdown Log          .docx Draft
```

### Phase 1 — RAG Ingestion *(The Foundation)*
The baseline PDF manual is uploaded, chunked, and vectorized using `gemini-embedding-001`. Embeddings are stored in a local **ChromaDB** vector database that preserves the document's structural hierarchy.

### Phase 2 — Extraction & Analysis *(Agent Node 1)*
The **Release Analyzer Agent** connects to ADO and Confluence to fetch raw sprint deltas. It sanitizes and categorizes every change into:
- 🏛️ Architectural variations
- ⚙️ Parameter updates
- 🐛 Bug documentation entries

### Phase 3 — Contextual Mapping & Drafting *(Agent Node 2)*
The **Documentation Drafter Agent** queries the vector database with the sanitized delta summary. It merges historical context with incoming changes to generate **pinpoint insertion instructions** — telling you exactly where in the document each change belongs and how to word it.

### Phase 4 — Delivery
Outputs a UI-rendered Markdown log and generates downloadable `.md` + `.docx` files for immediate team handoff.

---

## ✨ Key Capabilities

| Capability | Detail |
|---|---|
| 🛡️ **Zero-Hallucination Drafting** | Every output is strictly grounded in the uploaded baseline PDF via RAG — nothing is fabricated |
| 🔄 **Deterministic Workflow** | LangGraph state machine prevents agent loops and enforces strict sequential logic |
| 🧠 **Modern Embeddings** | Built on Google's unified `gemini-embedding-001` for high-accuracy semantic search |
| 🖥️ **Interactive Dashboard** | Reactive Streamlit frontend built for immediate team adoption |
| 📦 **Multi-Format Export** | Native `.md` and `.docx` generation — compatible with MadCap Flare, Word, and Confluence |

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|---|---|
| **Language** | Python 3.14+ |
| **Frontend** | Streamlit 1.45.0 |
| **AI Orchestration** | LangGraph 0.0.30 · LangChain 0.3 |
| **LLM** | Google Gemini 2.5 Flash |
| **Embeddings** | `gemini-embedding-001` |
| **Vector Store** | ChromaDB |
| **Document Processing** | PyPDF · python-docx |

</div>

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/doc_updater_project.git
cd doc_updater_project
```

### 2. Create a Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:

```env
# Required
GEMINI_API_KEY=your_actual_api_key_here

# Optional — for live ADO & Confluence integration
ADO_ORGANIZATION=your_org
ADO_PROJECT=your_project
ADO_PAT=your_personal_access_token
CONFLUENCE_URL=https://your-domain.atlassian.net
CONFLUENCE_API_TOKEN=your_confluence_token
```

### 5. Launch the App
```bash
streamlit run app.py
```

The dashboard opens automatically in your default browser.

---

## 💡 Usage

```
1. Set Sprint Scope    →   Enter target milestone in the left sidebar
                           e.g. "Sprint 24 - Core Infrastructure Upgrades"

2. Upload Baseline     →   Drop your current system manual as a .pdf file

3. Trigger Pipeline    →   Click "Trigger Documentation Update Pipeline"

4. Review & Export     →   Read the generated revision log, then download
                           the .md or .docx file for final team review
```

---

## 🔮 Roadmap

- [ ] **Live API Integration** — Transition `custom_tools.py` from mock data to Atlassian Python API and Azure DevOps REST API
- [ ] **Advanced PDF Chunking** — Preserve complex table structures and multi-column layouts during ingestion
- [ ] **GitHub/GitLab PR Generation** — Auto-create pull requests to documentation repositories on pipeline completion
- [ ] **Confluence Direct Push** — Write approved changes back directly to Confluence pages

---

## 👤 Author

<div align="center">

**C Vishnu Vardhan**
*AI/ML Engineer & Technical Writer*

Bridging the gap between complex software engineering workflows and clear, scalable technical documentation.

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com)

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f3460,50:16213e,100:1a1a2e&height=100&section=footer" width="100%"/>

*Built with precision. Engineered for scale.*

</div>
