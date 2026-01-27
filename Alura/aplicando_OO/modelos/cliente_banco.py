import conta_bancaria
class ClienteBanco():
    def __init__(self, nome='', cpf=0, idade=0, sexo='Não informado', estado_civil='Não informado'):
        self.nome = nome.title()
        self.cpf = cpf
        self.idade = idade
        self.sexo = sexo.upper()
        self.estado_civil = estado_civil.upper()

        @classmethod
        def criar_conta(cls, titular, saldo_inicial):
            conta = conta_bancaria.ContaBancaria(titular, saldo_inicial)


clinte = ClienteBanco('Viviane siqueira', 12345678910, 46, 'Feminino', 'Casada')
clinte_2 = ClienteBanco('alanis guillen', 54345678910, 28, 'Feminino')
clinte_3 = ClienteBanco('helena Rizzo', 12345428910, 36)

print(vars(clinte))
print(vars(clinte_2))
print(vars(clinte_3))