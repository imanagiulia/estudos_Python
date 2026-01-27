class Cliente():
    def __init__(self, nome, cpf, idade):
        self.nome = nome 
        self.cpf = cpf
        self.idade = idade
        self.ativo = True


cliente_1 = Cliente('Marluce', 12345678910, 19)
cliente_2 = Cliente('Jão', 12332678910, 24)
cliente_3 = Cliente('Maria', 12345671510, 36)