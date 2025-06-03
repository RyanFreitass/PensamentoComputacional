"""
 - Projeto: Sistema de Cadastro de Usuários.
 - IENH - 2025/01
 - Aluno/Autor: Ryan Vitor Freitas

Arquivo que contem classes que representam os modelos
de banco de dados

Classes:
 - Usuario: Representa a tabela de usuários no banco de dados.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base para nossos modelos
Base = declarative_base()

class Usuario(Base):
    """
    Classe que representa a tabela 'usuarios' no banco de dados.
    Atributos:
        id (int): ID do usuário, chave primária.
        nome (str): Nome do usuário (tamanho maximo de 50 caracteres).
        idade (int): Idade do usuário.
    """
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    idade = Column(Integer)
    

    def __repr__(self):
        return f"<Usuario(nome='{self.nome}', idade={self.idade})>"