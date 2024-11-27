# Web Honeypot

This project implements a simple honeypot using Python and Flask. The honeypot is designed to attract and log malicious traffic by simulating a vulnerable web application. It provides an interface to view incoming requests and store logs for analysis.

## Features
- Logs incoming GET and POST requests
- Web interface to view logs
- Stores logs for future analysis
- Simulates a vulnerable web server

## Logs 
- Date and time of the request
- Client IP Address
- Request Method(GET, POST, etc)
- Request Header
- Request Bodu(for POST Request)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/baradika/web-honeypot.git
   cd web-honeypot
2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Run the honeypot:**
   ```bash
   python3 honeypot.py
4. **Access the honeypot:**
   Open your browser and navigate to http://127.0.0.1:8080 to view the honeypot interface.

## Usage
- The homepage will display a message indicating that the server is running.
- The logs page (/logs) will display all captured requests.

## Example Requests
You can use curl or a similar tool to send requests to the honeypot:
- **GET Request / POST Request**

  
```bash
$ curl http://127.0.0.1:8080  /  $ curl -X POST http://127.0.0.1:8080/honeypot -d "Test data"
