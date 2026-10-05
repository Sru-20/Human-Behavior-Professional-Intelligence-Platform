# Behaviour Guide

Behaviour Guide is an evidence-aware chatbot project for helping people navigate real-life behavioural situations with clear, practical guidance. It will ground answers in retrieved sources, cite its evidence, and be honest when evidence is insufficient.

## Setup

1. Create and activate a Python 3.11 virtual environment in `backend`.
2. Install dependencies with `pip install -r requirements.txt`.
3. Copy `.env.example` to `.env` and add configuration values as needed.
4. Start the API with `uvicorn app.main:app --reload` from `backend`.
5. Run tests with `pytest` from `backend`.
6. Open `http://127.0.0.1:8000/health` to check the API.
