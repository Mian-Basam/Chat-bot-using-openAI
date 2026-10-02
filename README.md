# Flask GPT Chatbot

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0-black.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-gpt--5--mini-412991.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A Flask web app that wraps the OpenAI API in a simple chat interface. Each question is sent along with the previous turns, so answers stay in context, and every exchange is saved to SQLite so you can browse the history.

## Features

- Context-aware replies: prior messages are sent with each request
- Conversation history page backed by SQLite (Flask-SQLAlchemy)
- Jinja2 templates with a lightweight CSS theme
- API key loaded from environment variables, never hard-coded
- Dockerfile for a reproducible Python 3.12 environment

## Project structure

```
ChatbotUsingFlask/
├── app.py                 # Entry point
├── .env.example           # Copy to .env and add your key
└── website/
    ├── __init__.py        # App factory, DB setup (database.db is created on first run)
    ├── routes.py          # Routes and OpenAI call
    ├── models.py          # Result model for chat history
    ├── static/mainpage.css
    └── templates/         # base, history, response_view
Dockerfile
requirements.txt
```

## Getting started

```bash
git clone https://github.com/Mian-Basam/Chat-bot-using-openAI.git
cd Chat-bot-using-openAI
pip install -r requirements.txt

cd ChatbotUsingFlask
cp .env.example .env        # then set OPENAI_API_KEY
flask run --host=0.0.0.0
```

Open http://127.0.0.1:5000.

### With Docker

```bash
docker build -t flask-chatbot .
docker run -p 5000:5000 --env-file ChatbotUsingFlask/.env flask-chatbot
```

## Tech stack

Python · Flask · Flask-SQLAlchemy · SQLite · OpenAI Python SDK · Jinja2 · Docker

## License

[MIT](LICENSE)
