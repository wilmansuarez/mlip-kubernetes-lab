from flask import Flask, request
import itertools
import requests

app = Flask(__name__)

# 🔄 TODO: Agregar las URLs del backend para distribuir tráfico en round-robin
BACKEND_SERVERS = [
    "http://flask-backend-service:5001",  # Asegúrate de usar el nombre del servicio en Kubernetes
]

# Round-robin iterator para distribuir las solicitudes
server_pool = itertools.cycle(BACKEND_SERVERS)

@app.route('/')
def load_balance():
    backend_url = next(server_pool)
    user_id = request.args.get("user_id", "Guest")
    response = requests.get(f"{backend_url}/", params={"user_id": user_id})
    return response.text

if __name__ == '__main__':
    # Puedes cambiar el puerto si es necesario
    app.run(host='0.0.0.0', port=8080)
