lista_convidados = set()

while True:
    convidado = input("Digite o nome do convidado: ").lower()

    if convidado == 'sair':
        break

    lista_convidados.add(convidado.capitalize())


print(f'Convidados confirmados: {lista_convidados}')
