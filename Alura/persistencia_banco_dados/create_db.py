import sqlite3

conn = sqlite3.connect('escola.db') # cria o banco de dados caso não exista ou se conecta ao banco de dados caso ele já existaz

cursor = conn.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS estudantes(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            idade INTEGER
        )
    """
)

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS disciplinas(
            id INTEGER PRIMARY KEY,
            nome_disciplina TEXT,
            id_estudante INTEGER,
            FOREIGN KEY (id_estudante) REFERENCES estudantes(id)
        )
    """
)

conn.commit() # confirmação das alterações
conn.close() # encerrando a conexão com o db
