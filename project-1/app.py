import os
from flask import Flask, request
import datetime

app = Flask(__name__)

# Set log file to be inside project-1/logs.txt
LOG_FILE = os.getenv("LOG_FILE", "project-1/logs.txt")

# Ensure the project-1 directory exists (not needed unless writing new files)
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def log_message(message):
    with open(LOG_FILE, "a") as file:
        file.write(f"{datetime.datetime.now()} - {message}\n")

@app.route("/")
def home():
    log_message("Home page accessed")
    return "Hello, World! Logs are now persistent!"

@app.route("/log", methods=["POST"])
def log():
    data = request.json.get("message", "No message provided")
    log_message(data)
    return {"status": "logged", "message": data}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
