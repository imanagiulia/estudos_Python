import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# cursor.execute(
#     """
#         INSERT INTO estudantes(nome, idade) 
#         VALUES (?, ?)
#     """,

#     ('Maria', 67)
# )

cursor.execute(
    """
        INSERT INTO disciplinas(nome_disciplina, id_estudante) 
        VALUES (?, ?)
    """,

    ('Estatística', 2)
)

conn.commit()
conn.close()