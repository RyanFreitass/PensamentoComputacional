from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.models import Usuario, Base

# Conectar ao banco
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session() 

def criar_usuario(nome: str, idade: int, ) -> Usuario:
    # Criar novo usuário
    novo_usuario = Usuario(nome=nome, idade=idade)
    # Adicionar à sessão
    session.add(novo_usuario)
    # Salvar no banco
    session.commit()
    return novo_usuario


def buscar_todos_usuarios() -> list[Usuario]:
    try:
        usuarios = session.query(Usuario).all()
    except Exception as e:
        print(e)
        usuarios = []
    return usuarios

def buscar_usuarios_por_nome(nome: str) -> list[Usuario]:
    try:
        usuarios = session.query(Usuario).filter_by(nome=nome).all()
    except Exception as e:
        print(e)
        usuarios = []
    return usuarios



if __name__ == '__main__':
    print("Meu primeiro banco de dados!")
    novo_usuario = criar_usuario(nome="Ryan", idade=18)
    print(novo_usuario)
    
    # imprime todos os usuarios cadastrados
    for usuario in buscar_todos_usuarios():
        print(usuario)