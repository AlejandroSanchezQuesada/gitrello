from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
#cors = CORS(app, resources={r"/webhook": {"origins": "https://trello.com"}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.route("/")
def hello_world():
    return "<p>Gitrello actualizado</p>"

# Variable para almacenar el último webhook recibido
last_webhook = None

#esta es la url que escucha los post de los webhooks
@app.route('/', methods=['POST'])
def webhook():
    print("Ha entrado la petición");
    global last_webhook
    data = request.json
    
    
    print("la request es {request}")
    print("la request json es {request.json}")

    # Procesar el webhook recibido
    # Puedes agregar aquí la lógica para manejar los eventos del webhook

    # Actualizar last_webhook con el webhook recibido
    last_webhook = data

    # Imprimir el webhook en la consola
    print("Nuevo webhook recibido:")
    print(data)

    return jsonify({"message": "Webhook recibido correctamente"})

@app.route('/latest_webhook', methods=['GET'])
def get_latest_webhook():
    if last_webhook is None:
        return jsonify({"message": "No se ha recibido ningún webhook aún"})
    
    return jsonify(last_webhook)