#ponte com o banco de dados

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_url = 'postgresql://postgres:postgres@localhost:5432/db_escola'

engine = create_engine(database_url) #motor que faz a ponte entre o PostgreSQL e FastAPI

session_local = sessionmaker(bind=engine) # 'fábrica de conexões'

Base = declarative_base() #classe base do sqlalchemy que permite o rastreamento e dita como as tabelas reais serão criadas no PostgreSQL