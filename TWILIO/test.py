from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/audio')
def serve_audio():
    return send_from_directory('static', 'chala-ja-bsdk.mp3', mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(port=3000)