# ToneCraft AI ✍️
> Your words, elevated. — Powered by Qubrid AI × GLM-4.7

## What it does

Paste any text. Pick a tone. GLM-4.7 rewrites it and explains every change — making you a better writer in the process.

Six tones: **Executive · Casual · Persuasive · Academic · Marketing · Diplomatic**

## Setup

```bash
uv venv
source .venv/bin/activate
uv sync
cp .env.example .env   # add your QUBRID_API_KEY
streamlit run app.py
```

### Fallback (pip)
```bash
pip install -r requirements.txt
```

## Features

- Side-by-side comparison (original vs rewritten)
- Diff stats: word count change, readability delta
- Explanation of every change made
- Full session history in SQLite sidebar
- Load any past rewrite without re-calling the API
- Download rewrite reports as `.txt`
- Stormy Morning dark theme

## Project structure

```
tonecraft-ai/
├── app.py                  # Streamlit entry point
├── backend/
│   ├── api_client.py       # Qubrid API calls (GLM-4.7)
│   └── parser.py           # JSON parsing + diff stats
├── database/
│   └── db.py               # SQLite — init, CRUD, stats
├── frontend/
│   ├── components.py       # All UI render functions
│   └── styles.py           # Stormy Morning CSS
├── config/
│   └── settings.py         # Constants, tones, prompts
├── .env.example
├── pyproject.toml
└── requirements.txt
```

## Powered by

- GLM-4.7-FP8 (Z.ai / Zhipu AI) via Qubrid AI API
- Streamlit · SQLite · uv
