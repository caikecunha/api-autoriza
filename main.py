from flask import Flask, jsonify
import random

app = Flask(__name__)

def validador():
    # Sorteia um número entre 1 e 10, caso o número seja PAR retorna True como autorizado
    NUMERO = random.randint(1, 10)
    return NUMERO % 2 == 0  # Retorno booleano, True (par) ou False (ímpar)

@app.route('/')
def index():
    AUTORIZADO = validador()
    return jsonify({
        'status': 'ok' if AUTORIZADO else 'falha',
        'message': 'autorizado' if AUTORIZADO else 'negado'
    }), 200 if AUTORIZADO else 403  # 200 para autorizado, 403 para negado

if __name__ == "__main__":
    app.run(debug=True, port=5000)
