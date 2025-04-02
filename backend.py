from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def hello_user():
    user_id = request.args.get("user_id", "Guest")
    instance = socket.gethostname()
    
    return f"Hello, {user_id}! This response is from instance: {instance}"

if __name__ == '__main__':
    # Puedes cambiar el puerto si es necesario
    app.run(host='0.0.0.0', port=5001)
    