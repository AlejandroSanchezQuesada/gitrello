from flask import Flask, request
from flask_cors import CORS
from database.database import init_db
from services import TrelloServices, GithubServices

app = Flask(__name__)
CORS(app)
#cors = CORS(app, resources={r"/webhook": {"origins": "https://trello.com"}})

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/gitrello'
init_db(app)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.route("/")
def hello_world():
    return "<p>Gitrello App</p>"

# Endpoint that listens the webhooks
@app.route('/', methods=['POST'])
def webhook():
    return TrelloServices.process_json(request.json)


@app.route('/latest_webhook', methods=['GET'])
def get_latest_webhook():
    return TrelloServices.get_latest_webhook()
