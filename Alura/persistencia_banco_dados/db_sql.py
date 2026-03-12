import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor() #necessário para poder fazer os scripts sql

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
    "INSERT INTO estudantes(nome, idade)\
    VALUES (?, ?)", ('Jãoa', 20)
)

conn.commit() # executa o comando

cursor.execute("SELECT * FROM estudantes")
print(cursor.fetchall())

conn.close() # fecha a conexão com o db