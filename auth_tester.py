from flask import Flask, jsonify
import random

app = Flask(__name__)

VALORES_AUTORIZACAO = (True, False)

def validador_autoriza() -> bool:
    # Retorna aleatoriamente o booleano True (autorizado) ou False (negado)
    return random.choice(VALORES_AUTORIZACAO)

# Endpoint que retorna aleatoriamente
@app.route('/')
def index():
    AUTORIZADO = validador_autoriza()
    STATUS_CODE = 200 if AUTORIZADO else 403  # 200 para autorizado, 403 para negado

    return jsonify({
        'status': 'ok' if AUTORIZADO else 'falha',
        'message': 'autorizado' if AUTORIZADO else 'negado',
        'code': STATUS_CODE
    }), STATUS_CODE

# Endpoint que sempre retorna autorizado
@app.route('/sempre-autorizado')
def sempre_autorizado():
    return jsonify({
        'status': 'ok',
        'message': 'autorizado',
        'code': 200
    }), 200

# Endpoint que sempre retorna negado
@app.route('/sempre-negado')
def sempre_negado():
    return jsonify({
        'status': 'falha',
        'message': 'negado',
        'code': 403
    }), 403

if __name__ == "__main__":
    app.run(debug=True, port=5000)
