from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhooks/answer", methods=["GET", "POST"])
def answer_call():
    ncco = [
        {
            "action": "talk",
            "voiceName": "Amy",
            "text": "Hello! This is your AI agent. Please speak after the beep."
        }
    ]
    return jsonify(ncco)

@app.route("/webhooks/events", methods=["POST"])
def events():
    print("Event:", request.json)
    return ("", 204)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
