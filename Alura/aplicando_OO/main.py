from modelos.livro import Livro

livro_1 = Livro('Lista de convidados', 'Raphael Montes', 2019)
livro_2 = Livro('A empregada', 'Frieda ', 2023)

for livro in Livro.livros:
    print('Livros cadastrados:')
    print(livro)
