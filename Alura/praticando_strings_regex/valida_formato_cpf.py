import re

def valida_formato_CPF():
    padrao_CPF = r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b'
    cpf = input('Digite um CPF: ')

    resultado = re.search(padrao_CPF, cpf)

    if resultado:
        return 'CPF válido!'
    else:
        return 'CPF inválido!'
    
print(valida_formato_CPF())