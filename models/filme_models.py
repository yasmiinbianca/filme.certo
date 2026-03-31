# Importa o objeto db de 'db', que fornece as funcionalidades do SQLAlchemy para interagir com o banco de dados
from db import db  

# Define a classe filme que representa a tabela 'filmes' no banco de dados
class filme(db.Model):  
    # Define o nome da tabela no banco de dados
    __tablename__ = 'filmes'  

    # Define as colunas da tabela 'filmes'
    id = db.Column(db.Integer, primary_key=True)  
    titulo = db.Column(db.String(80), nullable=False)  
    genero = db.Column(db.String(80), nullable=False)  
    duracao = db.Column(db.Integer, nullable=False)  
    lancamento = db.Column(db.Integer, nullable=False) 
    diretor = db.Column(db.String(80), nullable=False)  

    # Método para retornar os dados do filme como um dicionário
    def json(self):  
        return {
            'id': self.id,  # ID do filme
            'titulo': self.titulo,  # Modelo do filme
            'genero': self.genero,  # Marca do filme
            'duracao': self.duracao,  # Ano do filme
            'lancamento': self.lancamento,
            'diretor': self.diretor
        }
