from sqlalchemy import create_engine, Column, String, Integer, Text, Date, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
# Cria a base declarativa
Base = declarative_base()

# Define a classe para a tabela
class Administrador(Base):
    __tablename__ = 'tbl_administrador'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_completo = Column(String(200), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    rg = Column(String(20), nullable=False)
    cpf = Column(String(20), nullable=False)
    telefone = Column(String(20), nullable=False)
    ativo = Column(Boolean, nullable=False)
    email = Column(String(200), nullable=False)
    senha = Column(String(200), nullable=False)
    experiencia = Column(Text, nullable=False)

    

