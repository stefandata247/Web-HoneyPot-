#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify, render_template
import datetime
import os

app = Flask(__name__)

# Log file to save incoming requests
LOG_FILE = "honeypot_logs.txt"

# Ensure log file exists
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        f.write("")

def log_request(data):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {data}\n")

@app.route('/honeypot', methods=['GET', 'POST'])
def honeypot():
    # Log the incoming request
    data = {
        "method": request.method,
        "data": request.data.decode('utf-8'),
        "ip": request.remote_addr,
        "user_agent": request.headers.get('User-Agent'),
        "timestamp": datetime.datetime.now().isoformat()
    }
    
    log_request(data)
    
    # Basic response
    return "You've been caught in a honeypot!", 200

@app.route('/logs', methods=['GET'])
def logs():
    with open(LOG_FILE, "r") as log_file:
        logs = log_file.readlines()
    return render_template('logs.html', logs=logs)

@app.route('/')
def home():
    return "<h1>Welcome to the Honeypot</h1><a href='/logs'>View Logs</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # Change port if necessary


# In[ ]:




