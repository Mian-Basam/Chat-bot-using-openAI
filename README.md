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
ChatbotUsingFlask/  <br>
│-- app.py      &nbsp;&nbsp;&nbsp;           # Main entry point for Flask app   <br>
│-- .env        &nbsp;&nbsp;&nbsp;           # Environment variables (contains OPENAI_API_KEY)   <br>
│-- website/   <br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │-- __init__.py &nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;       # Flask app initialization   <br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │-- routes.py    &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;      # Flask routes & chatbot logic   <br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │-- models.py    &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;       # Data models (Result object for chat history)   <br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │-- database.db   &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;      # SQLite database (if used for persistence)   <br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │-- static/   <br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │-- mainpage.css  &nbsp;&nbsp;&nbsp;   # Styling   <br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │-- templates/   <br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        │-- base.html   <br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        │-- history.html   <br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        │-- response_view.html   <br>
<br>

## Requirments.txt
Flask==2.3.3    <br>
Flask-SQLAlchemy==3.0.5   <br>
openai==1.3.0   <br>
python-dotenv==1.0.0   <br>
requests==2.31.0   <br>

## Run the Flask App
flask run --host=0.0.0.0
By default, the app will be available at http://127.0.0.1:5000/.
