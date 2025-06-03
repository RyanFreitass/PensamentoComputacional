from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine('sqlite:///meubanco.db')
Session = sessionmaker(bind=db)
session = Session()


Base = declarative_base()

#tabelas
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo


#Livros
class Livro(Base):
    __tablename__ = "livros"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    qtde_paginas = Column("qtde_paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id"))

    def __init__(self, titulo, qtde_paginas, dono):
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.dono = dono



Base.metadata.create_all(bind=db)

# "CRUD"


# C -- CREATE
'''usuario = Usuario(nome="Ryan", email="ryanfreitas@gmail.com", senha="123456")
session.add(usuario)
session.commit()'''


# R -- READ
'''lista_usuarios = session.query(Usuario).all()'''
usuario_ryan = session.query(Usuario).filter_by(email="ryanfreitas@gmail.com").first()
print(usuario_ryan)
print(usuario_ryan.nome)
print(usuario_ryan.email)
'''livro = Livro(titulo="Harry Potter", qtde_paginas=210, dono=usuario_ryan.id)
session.add(livro)
session.commit()'''


# U -- UPDATE
'''usuario_ryan.nome = "Ryan Freitas"
session.add(usuario_ryan)
session.commit()'''


# D -- DELETE
session.delete(usuario_ryan)
session.commit()