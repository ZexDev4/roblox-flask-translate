from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

LARA_API = "https://webapi.laratranslate.com/translate/segmented"

@app.route("/", methods=["POST"])
def translate():
    data = request.json
    if not data or "q" not in data or "target" not in data:
        return jsonify({"error": "Missing 'q' or 'target'"}), 400

    payload = {
        "q": data["q"],
        "source": "",
        "target": data["target"],
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

    try:
        response = requests.post(LARA_API, json=payload, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500


# Vercel membutuhkan objek callable bernama "app" di root file
