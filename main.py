from flask import Flask, jsonify
import random

app = Flask(__name__)

def validador():
    # Tupla com valores, True para autorizado e False para negado
    valores = (True, False)
    return random.choice(valores)  # Retorna o booleano de forma aleatória

@app.route('/')
def index():
    AUTORIZADO = validador()
    return jsonify({
        'status': 'ok' if AUTORIZADO else 'falha',
        'message': 'autorizado' if AUTORIZADO else 'negado'
    }), 200 if AUTORIZADO else 403  # 200 para autorizado, 403 para negado

if __name__ == "__main__":
    app.run(debug=True, port=5000)
