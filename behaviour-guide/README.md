# Behaviour Guide

Behaviour Guide is an evidence-grounded AI system designed to help users reason through and practise real-life communication, behavioural, professional, educational, and social situations. Examples include presentations, school or college, workplace communication, professional behaviour, talking to elders, coworker interactions, and difficult conversations.

## Setup

Requires Python 3.11.

From the project root, create and activate a virtual environment and install the backend requirements.

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
```

From the project root, start the server:

```bash
uvicorn backend.app.main:app --reload
```

Open `http://127.0.0.1:8000/health` to check the health endpoint. Run tests from the project root with `pytest`.
