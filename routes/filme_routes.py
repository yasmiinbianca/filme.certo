from flask import Blueprint, request  
from controllers.filme_controllers import get_filmes, create_filme

# Define um Blueprint para as rotas de "filme"
filme_routes = Blueprint('filme_routes', __name__)  

# Rota para listar todos os filmes (GET)
@filme_routes.route('/filme', methods=['GET'])
def filmes_get():
    return get_filmes()

# Rota para criar um novo filme (POST)
@filme_routes.route('/filme', methods=['POST'])
def filmes_post():
    return create_filme(request.json)

