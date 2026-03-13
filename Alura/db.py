import sqlite3 


def conectar():
    conn = sqlite3.connect('escola.db')
    return conn

def criar_tabela_estudante():
    conn = conectar()
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
    
    conn.commit()
    conn.close()

def criar_tabela_matriculas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS matriculas(
                id INTEGER PRIMARY KEY,
                nome_disciplina TEXT,
                id_estudante INTEGER,
                FOREIGN KEY (id_estudante) REFERENCES estudantes(id)
            )
        """
    )

    conn.commit()
    conn.close()

def criar_estudante(nome, idade):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
            INSERT INTO estudantes(nome, idade)
            VALUES (?, ?)
        """,

        (nome, idade)
    )

    conn.commit()
    conn.close()

def listar_estudantes():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT * FROM estudantes
        """
    )

    estudantes = cursor.fetchall()

    for estudante in estudantes:
        print(estudante)

    conn.commit()
    conn.close()

def criar_matricula(nome_disciplina, id_estudante):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
            INSERT INTO matriculas(nome_disciplina, id_estudante)
            VALUES (?, ?)
        """,
        (nome_disciplina, id_estudante)
    )

    conn.commit()
    conn.close()

def listar_matriculas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT * FROM matriculas
        """
    )

    matriculas = cursor.fetchall()
    
    for matricula in matriculas:
        print(matricula)

    conn.commit()
    conn.close()

def listar_mariculas_nome_estudante():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT m.id, e.nome, m.nome_disciplina
            FROM matriculas as m
            JOIN estudantes as e 
            ON m.estudante_id = e.id
        """
    )

    matriculas = cursor.fetchall()
    
    for matricula in matriculas:
        print(matricula)

    conn.commit()
    conn.close()