
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from CI/CD Pipeline - Version 2"

@app.route("/student")
def student():
    return {
        "name": "Student",
        "course": "Cloud Computing and DevOps"
    }

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
