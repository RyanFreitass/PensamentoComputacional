from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

'''
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    idade = Column(Integer)

    def __repr__(self):
        return f"<Usuario(nome='{self.nome})', idade={self.idade})>"
    

engine = create_engine('sqlite:///exemplo.db')
Base.metadata.create_all(engine)
'''

