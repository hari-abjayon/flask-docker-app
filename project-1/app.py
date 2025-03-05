import os
from flask import Flask, request
import datetime
 
app = Flask(__name__)
 
LOG_DIR = "/app/logs"
LOG_FILE = os.path.join(LOG_DIR, "logs.txt")
 
# Ensure the logs directory exists
os.makedirs(LOG_DIR, exist_ok=True)
 
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