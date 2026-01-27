class Livro():
    livros = []

    def __init__(self, titulo='', autor='Não informado', ano_publicacao=0):
        self._titulo = titulo.title()
        self._autor = autor.capitalize()
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'{self._titulo}, escrito por {self._autor} foi publicado no ano de {self._ano_publicacao}'
    
    def __repr__(self):
        return f'{self._titulo}'
    
    def devolver(self):
        self._disponivel = True
    
    def emprestar(self):
        self._disponivel = False
    

    def exibir_disponibilidade(self):
        if self._disponivel:
            return f'{self._titulo} está disponível!'
        else:
            return f'{self._titulo} não está disponível!'
        
    @staticmethod    
    def verificar_disponibilidade(ano):
        lista_livros = [livro for livro in Livro.livros if livro._ano_publicacao == ano and livro._disponivel == True]
        return lista_livros

    

