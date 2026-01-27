class Pessoa():
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome} - {self.profissao}, {self.idade} anos'
    
    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, me chamo {self.nome} e sou {self.profissao}!'
        else:
            return f'Olá, me chamo {self.nome}!'
    


pessoa = Pessoa('Amanda', 32, 'Fisioterapeuta')
print(vars(pessoa))

print(pessoa.saudacao)

pessoa.aniversario()
print(vars(pessoa))
