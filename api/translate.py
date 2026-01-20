from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

LARA_API = "https://webapi.laratranslate.com/translate/segmented"

@app.route("/api/translate", methods=["POST"])
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

    try:
        response = requests.post(LARA_API, json=payload, headers=headers)
        print (response.text)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
