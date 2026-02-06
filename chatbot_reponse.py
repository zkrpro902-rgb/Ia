import requests

API_KEY = "WCTIoWiG8Uw5gRb3zIzconuTL5KXZyGS"  # À remplacer
API_URL = "https://api.mistral.ai/v1/chat/completions"

def chatbot_reponse(question):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {
        "model": "mistral-tiny",  # ou "mistral-small", etc.
        "messages": [{"role": "user", "content": question}]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]
