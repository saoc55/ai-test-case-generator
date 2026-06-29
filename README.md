# ai-test-case-generator

[![CI](https://github.com/saoc55/ai-test-case-generator/actions/workflows/ci.yml/badge.svg)](https://github.com/saoc55/ai-test-case-generator/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.14-blue)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3-green)](https://langchain.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

AI-powered CLI tool that generates structured test cases from natural language feature descriptions using LangChain + Claude Haiku with a local RAG knowledge base (ChromaDB + sentence-transformers).

---

## What It Does

Paste in a feature description → get structured, ready-to-use test cases in BDD (Gherkin) or tabular Markdown format. A RAG layer backed by ChromaDB retrieves similar prior examples to keep output consistent and well-formatted.

```bash
python cli.py generate "User can log in with valid email and password" --format bdd
```

```gherkin
Feature: User Authentication

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters a valid email and password
    And clicks the Login button
    Then the user is redirected to the dashboard
    And a welcome message is displayed

  Scenario: Login fails with invalid password
    Given the user is on the login page
    When the user enters a valid email and incorrect password
    And clicks the Login button
    Then an error message "Invalid credentials" is displayed
    And the user remains on the login page
```

---

## Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.14.2 |
| LLM orchestration | LangChain 0.3 |
| LLM | Anthropic Claude Haiku (claude-haiku-4-5) |
| Vector store | ChromaDB (local) |
| Embeddings | sentence-transformers all-MiniLM-L6-v2 (local) |
| CLI | Click |
| Testing | Pytest + pytest-mock |
| CI | GitHub Actions |

---

## Architecture

```
Feature description (text input)
        │
        ▼
  rag_retriever.py  ──── ChromaDB (seed examples)
        │
        ▼ (top-3 similar examples)
  prompt_templates.py
        │
        ▼ (augmented prompt)
  llm_client.py (Claude Haiku via LangChain + langchain-anthropic)
        │
        ▼
  Structured test cases (BDD or tabular)
```

---

## Project Structure

```
ai-test-case-generator/
├── generator/
│   ├── llm_client.py         # LangChain ChatAnthropic setup
│   ├── embedder.py           # sentence-transformers + ChromaDB
│   ├── rag_retriever.py      # Retrieves similar examples
│   ├── prompt_templates.py   # BDD and tabular prompt templates
│   └── pipeline.py           # Orchestration: retrieve → augment → generate
├── knowledge_base/
│   ├── seed_data/            # Example test cases for RAG
│   └── ingest.py             # Seeds ChromaDB from seed_data/
├── tests/
│   ├── test_pipeline.py
│   ├── test_prompt_templates.py
│   └── test_rag_retriever.py
├── cli.py
├── .env.example
└── requirements.txt
```

---

## Setup

### 1. Clone and install
```bash
git clone https://github.com/saoc55/ai-test-case-generator.git
cd ai-test-case-generator
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure
```bash
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

### 3. Seed the knowledge base
```bash
python cli.py ingest
```

---

## Usage

### Generate BDD test cases (Gherkin)
```bash
python cli.py generate "User can reset password via email link" --format bdd
```

### Generate tabular test cases (Markdown table)
```bash
python cli.py generate "User can transfer funds between accounts" --format table
```

### Save output to file
```bash
python cli.py generate "User can register with a new email" --format bdd --output output/registration_tests.md
```

### Options
```
Options:
  --format [bdd|table]   Output format (default: bdd)
  --output PATH          Save output to file (default: stdout)
  --model TEXT           LLM model override (default: claude-haiku-4-5)
  --help                 Show this message and exit.
```

---

## Running Tests

```bash
pytest tests/ -v
```

All tests mock LLM calls — no API key required. Embeddings use sentence-transformers locally.

---

## Test Coverage

| Module | Test file | Tests |
|--------|-----------|-------|
| `pipeline.py` | `test_pipeline.py` | BDD generation, tabular generation, string output |
| `prompt_templates.py` | `test_prompt_templates.py` | Variable interpolation, format selection, fallbacks |
| `rag_retriever.py` | `test_rag_retriever.py` | List return type, n_results cap, empty result handling |

---

## Portfolio Context

This is Project 3 of a 6-project QA automation portfolio:

| # | Project | Stack |
|---|---------|-------|
| 1 | [playwright-e2e-framework](https://github.com/saoc55/playwright-e2e-framework) | JS, Playwright, GitHub Actions |
| 2 | [api-testing-suite](https://github.com/saoc55/api-testing-suite) | Python, Pytest, Requests |
| **3** | **ai-test-case-generator** | **Python, LangChain, Claude Haiku, ChromaDB, sentence-transformers** |
| 4 | java-bdd-framework | Java, Cucumber, RestAssured |
| 5 | rag-qa-chatbot | Python, LangChain, ChromaDB |
| 6 | trading-strategy-tester | Python, IBKR API |

Projects 1 and 2 tested the same Parabank application — UI with Playwright, then the underlying REST API with Pytest. This project automates the test case writing step itself.

---

## License

MIT
