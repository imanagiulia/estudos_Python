# arquivo responsável por criar a conexão com o banco de dados

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_url = "postgresql://'':''@localhost/" #usuario, senha, nome do db

engine = create_engine(database_url) # faz a comunicação do db com o fastAPI

session_local = sessionmaker(bind=engine) # conexão temporária com o db

Base = declarative_base() # cria os modelos/entidades