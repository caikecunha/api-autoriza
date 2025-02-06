from flask import Flask, jsonify
import random

app = Flask(__name__)

def validador():
    # Tupla com valores, True para autorizado e False para negado
    valores = (True, False)
    return random.choice(valores)  # Retorna o booleano de forma aleatória

# Endpoint que retorna autorizado ou negado aleatoriamente
@app.route('/')
def index():
    AUTORIZADO = validador()
    return jsonify({
        'status': 'ok' if AUTORIZADO else 'falha',
        'message': 'autorizado' if AUTORIZADO else 'negado'
    }), 200 if AUTORIZADO else 403  # 200 para autorizado, 403 para negado

# Endpoint que sempre retorna autorizado
@app.route('/sempre-autorizado')
def sempre_autorizado():
    return jsonify({
        'status': 'ok',
        'message': 'autorizado'
    }), 200

# Endpoint que sempre retorna negado
@app.route('/sempre-negado')
def sempre_negado():
    return jsonify({
        'status': 'falha',
        'message': 'negado'
    }), 403

if __name__ == "__main__":
    app.run(debug=True, port=5000)
