from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
# Allow CORS only from the frontend origin
CORS(app, origins=["http://localhost:3000"])

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message sent"}), 400
    response = model.generate_content(user_input)
    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(debug=True)
@app.route('/', methods=['GET'])
def home():
    return "Gemini Chatbot Backend is running."
