from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from Sheehan ECS Container!"
    })

if __name__ == "__main__":
    # Listen on all ports
    app.run(host="0.0.0.0", port=5000)
