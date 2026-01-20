import requests
from flask import Flask, request, jsonify

# Vercel expects "app" variable
app = Flask(__name__)

LARA_API = "https://webapi.laratranslate.com/translate/segmented"

@app.route("/", methods=["POST"])
def translate():
    data = request.get_json(force=True)
    q = data.get("q")
    target = data.get("target")
    if not q or not target:
        return jsonify({"error": "Missing q or target"}), 400

    payload = {
        "q": q,
        "source": "",
        "target": target,
        "instructions": [],
        "style": "faithful",
        "adapt_to": [],
        "glossaries": [],
        "content_type": "text/plain"
    }

    headers = {
        "Content-Type": "application/json",
        "x-lara-client": "Webapp",
        "Origin": "https://app.laratranslate.com"
    }

    response = requests.post(LARA_API, json=payload, headers=headers)
    print (response.text)
    return jsonify(response.json())
