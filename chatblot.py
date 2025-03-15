import os
import json
import pandas as pd
from flask import Flask, request, jsonify, render_template

# Initialize Flask App
app = Flask(__name__)

# Load Policy Dataset
def load_policy_data():
    try:
        df = pd.read_csv("government_policies.csv")
        policy_dict = {row["Policy Name"].lower(): row["Description"] for _, row in df.iterrows()}
        return policy_dict
    except FileNotFoundError:
        return {}

government_policies = load_policy_data()

# Chatbot Logic
def generate_response(user_query):
    user_query = user_query.lower()
    
    # Check for direct policy match
    for policy, description in government_policies.items():
        if policy in user_query:
            return description
    
    return "Sorry, I couldn't find any relevant policy information. Please refine your query."

# Serve UI
@app.route("/")
def home():
    return render_template("index.html")

# Chat API Endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_query = data.get("query", "").strip()
    
    if not user_query:
        return jsonify({"error": "Query cannot be empty"}), 400
    
    response = generate_response(user_query)
    return jsonify({"response": response})

# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
