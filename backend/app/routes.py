from flask import Blueprint, jsonify

# Criar o blueprint para as rotas
routes = Blueprint('routes', __name__)

# Exemplo de rota
@routes.route('/')
def index():
    return jsonify({"message": "Bem-vindo à API da Oficina!"})
