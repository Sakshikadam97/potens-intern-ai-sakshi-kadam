# Customer Support Triage Agent

## Project Overview

This project implements an AI-powered Customer Support Triage Agent using Google Gemini.

The agent receives customer support tickets in free-text format, analyzes the issue, assigns a category and priority, selects the appropriate support tool, and returns a structured JSON response.

The system uses an LLM-driven approach where Gemini decides:
- Ticket category
- Priority level
- Next action/tool

---

# Features

## 1. Free Text Ticket Input

The agent accepts customer issues written in natural language.

Example:

"Unable to login after password reset"

---

## 2. Ticket Classification

The agent classifies tickets into the following categories:

- Account Access
- Billing
- Technical Issue
- Complaint
- Feature Request
- General Query

---

## 3. Priority Assignment

The agent assigns priority levels:

### P0 - Critical

Examples:
- Security breach
- Production outage
- Complete system failure

### P1 - High Priority

Examples:
- Login failure
- Payment problems
- Major technical issues

### P2 - Normal Priority

Examples:
- Feature requests
- General questions
- Minor complaints

---

# Architecture

```
Customer Ticket
        |
        v
 FastAPI Endpoint
        |
        v
 Gemini AI Agent
        |
        |
  -----------------
  |       |       |
lookup  search  draft
tool    tool    tool
  |
  v
Structured JSON Response
        |
        v
Output JSON File
```

---

# Project Structure

```
potens-intern-ai-sakshi-kadam

│
├── agent.py              # Gemini agent logic
├── app.py                # FastAPI API
├── ui.py                 # Streamlit interface
├── tools.py              # Support tools
├── prompts.py            # System prompt
├── models.py             # Data models
│
├── data/
│   └── tickets.json      # Sample ticket data
│
├── examples/
│   ├── input1.txt
│   ├── output1.json
│   └── ...
│
├── outputs/
│   └── Generated responses
│
├── tests/
│   └── test_agent.py
│
├── requirements.txt
├── .env
└── README.md
```

---

# Technologies Used

- Python
- Google Gemini API
- FastAPI
- Streamlit
- JSON
- Pydantic
- Python-dotenv

---

# Installation

## 1. Clone Repository

```
git clone <repository-url>
```

Move into project folder:

```
cd potens-intern-ai-sakshi-kadam
```

---

## 2. Create Virtual Environment

```
python -m venv venv
```

Activate environment.

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

# Environment Setup

Create a file:

```
.env
```

Add Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

---

# Running the Application

## Start FastAPI Server

Run:

```
uvicorn app:app --reload
```

API will run at:

```
http://127.0.0.1:8000
```

---

## API Documentation

Open:

```
http://127.0.0.1:8000/docs
```

Example request:

```json
{
"text":"Unable to login after password reset"
}
```

Example response:

```json
{
"category":"Account Access",
"priority":"P1",
"next_tool":"lookup_tool"
}
```

---

# Streamlit User Interface

Run:

```
streamlit run ui.py
```

The interface allows users to enter support tickets and view:

- Category
- Priority
- Selected tool
- Reasoning
- Tool output
- Trace steps

---

# Available Tools

## 1. lookup_tool

Purpose:

Provides FAQ/help information.

Used for:

- Login problems
- Password reset
- Account access issues


---

## 2. search_tool

Purpose:

Searches previous similar support tickets.

Used for:

- Billing issues
- Payment problems
- Similar cases


---

## 3. draft_tool

Purpose:

Creates customer response drafts.

Used for:

- Complaints
- General communication
- Customer replies


---

# Agent Workflow

1. Customer submits support ticket.

2. Gemini analyzes the ticket.

3. Gemini selects:
   - Category
   - Priority
   - Appropriate tool

4. Selected tool executes.

5. Agent returns structured JSON.

6. Response is saved in outputs folder.

---

# Output Format

Example:

```json
{
"category":"Account Access",
"priority":"P1",
"next_tool":"lookup_tool",
"reasoning":"Customer has login problem",
"why":"Account access issue requires password guidance",
"trace":[
"Received customer ticket",
"Classified category",
"Assigned priority",
"Selected tool"
],
"tool_output":"Reset Password Guide"
}
```

---

# Testing

Run tests:

```
pytest
```

Test cases include:

- Account access issues
- Billing problems
- Feature requests
- Security issues
- General queries

---

# Examples

The examples folder contains 10 sample customer tickets.

Each example includes:

Input:

```
input1.txt
```

Expected output:

```
output1.json
```

Examples cover:

- Login problems
- Payment issues
- Server failures
- Feature requests
- Complaints

---

# Design Decisions

## LLM-Based Decision Making

Gemini is used to decide:

- Ticket category
- Priority
- Tool selection

This avoids hard-coded keyword routing.

---

## Structured Output

JSON format is used because it is:

- Easy to read
- API friendly
- Easy to test

---

# Limitations

- Depends on Gemini API availability.
- LLM responses may vary slightly.
- Search tool currently uses simple similarity matching.

---

# Future Improvements

Possible improvements:

- Add embedding-based ticket search.
- Add confidence score.
- Add human escalation tool.
- Improve evaluation metrics.
- Add database storage.
- Add authentication.

---

# AI Usage Log

AI assistance was used for:

- Designing agent architecture.
- Creating prompts.
- Debugging API integration.
- Improving tool selection logic.
- Generating test examples.
- Improving documentation structure.

The final implementation was reviewed and modified manually.

---

# Author

Sakshi Kadam

AI/ML Internship Project