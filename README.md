# AI Document Assistant (LLM-based)

## Overview
The **AI Document Assistant** is a lightweight Generative AI application that allows users to analyze business documents and ask natural language questions about their content.  
The system answers questions **strictly based on the selected document** and provides structured responses with supporting text excerpts.

This project demonstrates how Large Language Models (LLMs) can be applied to real-world enterprise use cases such as document analysis, knowledge retrieval, and decision support.

---

## Key Features
- 📂 Select and analyze different business documents
- 🤖 Ask natural language questions about document content
- 📌 Answers are **grounded in the document**
- 🧾 Structured output:
  - Short answer
  - Key details (bullet points)
  - Relevant text excerpts from the document
- ⚠️ Automatic handling of long documents (context size limitation)
- 🔐 Secure API key handling via environment variables

---

## Example Use Cases
This project is intentionally designed to be **generic and reusable** across industries:

- **Pharmaceutical / Healthcare**
  - Supply chain documentation
  - Regulatory and compliance documents
- **Automotive / Manufacturing**
  - Quality management processes
  - Technical or audit documentation
- **General Business**
  - Company overviews
  - Internal process descriptions

---

## Project Structure

genai-document-assistant/
│── app.py
│── requirements.txt
│── .env # not committed (API key)
│── sample_docs/
│ │── general_company_overview.txt
│ │── pharma_supply_chain.txt
│ │── automotive_quality_process.txt
│── README.md
│── .gitignore



---

## Technologies Used
- **Python**
- **OpenAI API (LLM)**
- `python-dotenv` for secure environment variable handling

---

## How It Works
1. The application lists available `.txt` documents from the `sample_docs` folder.
2. The user selects a document via a simple CLI menu.
3. The user asks a question related to the document.
4. The LLM generates a response based **only on the document content**.
5. The answer is returned in a structured and traceable format.

---

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/genai-document-assistant.git
cd genai-document-assistant

2. Create and activate a virtual environment
python -m venv .venv

Windows (PowerShell):
.\.venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt


4. Configure the API key
OPENAI_API_KEY=your API KEY  (Never commit your API Key)


Running the Application

## Demo (CLI)
Example flow:
1. Select a document from the list (e.g., `pharma_supply_chain.txt`)
2. Ask a question
3. Receive a structured answer with supporting excerpts

Example question:
- *Which regulatory requirements are mentioned in the document?*
## Notes
- The application uses a context size limit to avoid excessive token usage for long documents.
- Answers are designed to be document-grounded. If the information is not found, the assistant should respond accordingly.

.\.venv\Scripts\python.exe app.py

You will be prompted to:

  1. Select a document

  2. Ask a question about the document


Sample Questions

What are the main challenges in the pharmaceutical supply chain?

Which regulatory requirements are mentioned in the document?

What are the key priorities of the company described?

Limitations & Future Improvements

Currently supports .txt documents only

No semantic search or vector embeddings yet

CLI-based interface

Planned Enhancements

PDF document support

Vector search with embeddings

Web interface (Streamlit)

Source highlighting per answer

Multi-document comparison

Why This Project

This project was built to demonstrate:

Practical application of Generative AI

Prompt design and response structuring

Safe and controlled use of LLMs in enterprise contexts

Readiness for junior-level AI/ML roles with a focus on applied AI

Author

Willy Wandji
Junior Generative AI Engineer
Berlin, Germany