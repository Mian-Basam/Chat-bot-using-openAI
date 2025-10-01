# Flask GPT-5 Chatbot  
![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)  
![Flask](https://img.shields.io/badge/flask-2.0+-black.svg)  
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--5-412991.svg)  
![License](https://img.shields.io/badge/license-MIT-green.svg)  
![Status](https://img.shields.io/badge/status-active-success.svg)  

This project is a Flask-based web application that integrates **OpenAI GPT-5** to create an interactive AI-powered chatbot. The application allows users to submit queries, receive intelligent responses, and maintain a full conversation history for context-aware interactions.  

---

## 🚀 Features  
- Flask backend with route handling (`routes.py`)  
- Integration with **OpenAI GPT-5** for natural language responses  
- Dynamic conversation history stored in memory  
- Templated frontend using **Jinja2** (`templates/`)  
- Basic CSS styling (`static/mainpage.css`)  
- Environment variable support with `.env` for secure API key management  

---

## 📂 Project Structure  
ChatbotUsingFlask/<br>
│<br>
├── app.py # Main entry point for Flask app <br>
├── .env # Environment variables (contains OPENAI_API_KEY)<br>
│<br>
└── website/<br>
├── init.py # Flask app initialization<br>
├── routes.py # Flask routes & chatbot logic<br>
├── models.py # Data models (Result object for chat history) <br>
├── database.db # SQLite database (if used for persistence) <br>
│
├── static/ <br>
│ └── mainpage.css # Styling <br>
│ <br>
└── templates/ <br>
├── base.html <br>
├── history.html <br>
└── response_view.html <br>



## Run the Flask App
flask run --host=0.0.0.0
By default, the app will be available at http://127.0.0.1:5000/.
