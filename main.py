from flask import Flask, jsonify
import random

app = Flask(__name__)

def validador():
    NUMERO = random.randint(1, 10)
    return NUMERO % 2 == 0

@app.route('/')
def index():
    AUTORIZADO = validador()
    return jsonify({
        'status': 'ok' if AUTORIZADO else 'falha',
        'message': 'autorizado' if AUTORIZADO else 'negado'
    })

app.run(debug=True)
