def saudacao(nome: str, cidade: str):
    return f"Olá, {nome.capitalize()}! Bem-vinda ao sistema da cidade de {cidade.capitalize()}."

nome = input('Digite seu nome: ')
cidade = input('Digite sua cidade: ')

print(saudacao(nome, cidade))