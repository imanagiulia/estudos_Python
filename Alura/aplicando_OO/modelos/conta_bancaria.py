class ContaBancaria():
    
    def __init__(self, nome='', saldo=0):
        self._titular = nome 
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Essa conta pertence à {self._titular} e possuí um saldo de R$ {self._saldo:.2f}'
    
    def ativar_conta(self):
        self._ativo = True
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo
        


conta = ContaBancaria('Giovanna Reis', 25000)

conta_2 = ContaBancaria('Gabriella Medvedovisky', 50000)
conta_2.ativar_conta() 

print((conta.ativo))
print((conta_2.ativo))

print(conta.titular)
