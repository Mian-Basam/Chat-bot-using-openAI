from flask import Blueprint, render_template, request
from .models import Result
from openai import OpenAI
import os

# Define the Blueprint FIRST before any other code
routes = Blueprint('routes', __name__)

# --- Global history ---
historyData = []

# Initialize OpenAI client directly
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- GPT query function ---
def ask(question, chat_log=None):
    """
    Ask GPT a question with optional previous chat log for context.
    """
    # Use the globally initialized client
    if client is None:
        return "Sorry, the AI service failed to initialize."
    
    # Build messages list
    messages = []
    if chat_log:
        for item in chat_log:
            role = "user" if "float-right" in item.messagetype else "assistant"
            messages.append({"role": role, "content": item.message})

    messages.append({"role": "user", "content": question})

    try:
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=messages
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"OpenAI API Call Error: {e}")
        return "Sorry, I'm experiencing an issue connecting to the AI service."

# --- Flask routes ---
@routes.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        query = request.args.get('query')
        if not query:
            return render_template('response_view.html', results=historyData)

        # Send previous history to GPT
        response_text = ask(query, chat_log=historyData)

        # Create Result objects for display
        queryMessage = Result(
            time="This Time",
            messagetype="other-message float-right",
            message=query
        )
        responseMessage = Result(
            time="This Time", 
            messagetype="my-message",
            message=response_text
        )

        # Update history
        dataList = [queryMessage, responseMessage]
        historyData.extend(dataList)

        return render_template('response_view.html', results=historyData)

    else:
        # POST: show full history
        return render_template('history.html', results=historyData)