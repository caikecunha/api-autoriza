from flask import Flask, jsonify
import random

app = Flask(__name__)

VALORES_AUTORIZACAO = (True, False)

def validador_autoriza() -> bool:
    # Retorna aleatoriamente o booleano True (autorizado) ou False (negado)
    return random.choice(VALORES_AUTORIZACAO)

# Endpoint que retorna aleatoriamente
@app.route('/', methods=['GET'])
def index():
    SITUACAO_AUTORIZADO = validador_autoriza()
    STATUS_CODE = 200 if SITUACAO_AUTORIZADO else 403  # 200 para autorizado, 403 para negado

    return jsonify({
        'status': 'success' if SITUACAO_AUTORIZADO else 'fail',
        'authorization': SITUACAO_AUTORIZADO,
        'code': STATUS_CODE
    }), STATUS_CODE

# Endpoint que sempre retorna autorizado
@app.route('/sempre-autorizado', methods=['GET'])
def sempre_autorizado():
    return jsonify({
        'status': 'success',
        'authorization': True,
        'code': 200
    }), 200

# Endpoint que sempre retorna negado
@app.route('/sempre-negado', methods=['GET'])
def sempre_negado():
    return jsonify({
        'status': 'fail',
        'authorization': False,
        'code': 403
    }), 403

if __name__ == "__main__":
    app.run(port=5000)
