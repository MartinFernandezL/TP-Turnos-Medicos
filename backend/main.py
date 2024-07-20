from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Paciente, Doctor, CitaMedica


app = Flask(__name__)
port = 5000
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://martin:martin@localhost:5432/tpintro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def hello_world():
    return 'Hello world!'

if __name__ == '__main__':
    print('Starting server...')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)
    print('Started...')