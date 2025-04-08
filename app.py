from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from Sheehan ECS Container."
    })

if __name__ == "__main__":
    # Listen on all interfaces so that it works in the Docker container
    app.run(host="0.0.0.0", port=5000)
