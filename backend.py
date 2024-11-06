# backend.py
from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def hello_user():
    # TODO: Get user_id from query parameters with a default of "Guest"
    user_id = request.args.get("user_id", "Guest")
    instance = socket.gethostname()
    # TODO: Customize the message to include a unique message or student identifier
    return f"Hello, {user_id}! This response is from instance {instance}."

if __name__ == '__main__':
    # TODO: Change the port if needed (default is 5001)
    app.run(host='0.0.0.0', port=5001)
