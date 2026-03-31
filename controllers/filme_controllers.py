from models.filme_models import filme  # Importa o modelo filme
from db import db  # Importa a conexão com o banco de dados
import json
from flask import make_response, request

# Função para obter todos os filmes
def get_filmes():
    filmes = filme.query.all()  # Busca todos os filmes no banco de dados
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de filmes.',
            'dados': [filme.json() for filme in filmes]  # Converte os objetos de filme para JSON
        }, ensure_ascii=False, sort_keys=False)  # Mantém caracteres especiais corretamente formatados
    )
    response.headers['Content-Type'] = 'application/json'  # Define o tipo de conteúdo como JSON
    return response

# Função para obter um filme específico por ID
def get_filme_by_id(filme_id):
    filme = filme.query.get(filme_id)  # Busca o filme pelo ID

    if filme:  # Verifica se o filme foi encontrado
        response = make_response(
            json.dumps({
                'mensagem': 'filme encontrado.',
                'dados': filme.json()  # Converte os dados do filme para formato JSON
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que o tipo da resposta seja JSON
        return response
    else:
        # Se o filme não for encontrado, retorna erro com código 404
        response = make_response(
            json.dumps({'mensagem': 'filme não encontrado.', 'dados': {}}, ensure_ascii=False),
            404  # Código HTTP 404 para "Não encontrado"
        )
        response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
        return response

# Função para criar um novo filme
def create_filme(filme_data):
    # Se os dados forem válidos, cria o novo filme
    novo_filme = filme(
        titulo=filme_data['titulo'],
        genero=filme_data['genero'],
        duracao=filme_data['duracao'],
        lancamento=filme_data['lancamento'],
        diretor=filme_data['diretor'],
    )
    
    db.session.add(novo_filme)  # Adiciona o novo filme ao banco de dados
    db.session.commit()  # Confirma a transação no banco

    # Resposta de sucesso com os dados do novo filme
    response = make_response(
        json.dumps({
            'mensagem': 'filme cadastrado com sucesso.',
            'filme': novo_filme.json()  # Retorna os dados do filme cadastrado
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
    return response
