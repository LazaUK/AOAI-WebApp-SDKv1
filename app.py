from flask import Flask, request, jsonify, render_template
from azure.identity import DefaultAzureCredential, EnvironmentCredential, get_bearer_token_provider
from openai import AzureOpenAI
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']

    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(),
        "https://cognitiveservices.azure.com/.default"
    )

    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_API_BASE"),
        azure_ad_token_provider = token_provider,
        api_version = os.getenv("AZURE_OPENAI_API_VERSION")
    )
    
    response = client.chat.completions.create(
        model = os.getenv("AZURE_OPENAI_API_DEPLOY"),
        messages = [
            {"role": "system", "content": "You are a friendly chatbot"},
            {"role": "user", "content": question}
        ]
    )

    answer = response.choices[0].message.content
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)