from flask import Flask, jsonify, request
from flask_cors import CORS
from services import services

app = Flask(__name__)
CORS(app)
#cors = CORS(app, resources={r"/webhook": {"origins": "https://trello.com"}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.route("/")
def hello_world():
    return "<p>Gitrello actualizado</p>"



#esta es la url que escucha los post de los webhooks
@app.route('/', methods=['POST'])
def webhook():
    return services.process_json(request.json)

    

@app.route('/latest_webhook', methods=['GET'])
def get_latest_webhook():
    return services.get_latest_webhook()