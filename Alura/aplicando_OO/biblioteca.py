from modelos.livro import Livro

livro_1 = Livro('A hora da estrela', 'Clarice Lispector', 2001)
livro_2 = Livro('A última festa', 'Fulano', 2021)
livro_3 = Livro('Lista de convidados', 'Raphael Montes', 2019)
livro_4 = Livro('A empregada', 'Frieda ', 2023)

livro_1.emprestar()

livros_disponiveis = Livro.verificar_disponibilidade(2021)
print(livros_disponiveis)

