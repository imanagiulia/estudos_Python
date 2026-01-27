from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Fast Food')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_japones.alternar_estado()
restaurante_mexicano.receber_avaliacao('Rodrigo', 8)
restaurante_mexicano.receber_avaliacao('Lais', 4)
restaurante_mexicano.receber_avaliacao('Giovanna', 2)


def main():
    Restaurante.listar_restaurantes()

    # restaurante_praca = Restaurante('', '')
    # restaurante_praca._nome = 'Praça'
    # restaurante_praca.alternar_estado()


    # restaurante_praca._categoria = 'Italiana'

    # print(restaurante_praca._nome)

    # if restaurante_praca.ativo:
    #     print('O restaurante está ativo!')
    # else:
    #     print('O restaurante está desativado!')


    # restaurante_praca._nome = 'Bistrô'

    # restaurante_pizza = Restaurante('', '')
    # restaurante_pizza._nome = 'Pizza Place'
    # restaurante_pizza._categoria = 'Fast Food'

    # print(restaurante_pizza._categoria)


    # print(vars(restaurante_praca))
    # print(f'Nome: {restaurante_praca._nome} - Categoria: {restaurante_praca._categoria}')

    # categoria = restaurante_praca._categoria
    # print(categoria)

    # restaurante_japa = Restaurante('Sushi em casa', 'Japonês')
    # print(vars(restaurante_japa))

    # print(restaurante_pizza)
    # print(restaurante_praca)
    # print(restaurante_japa)

    # Restaurante.listar_restaurantes()

    # mani = Restaurante('Mani Manioca', 'Cozinha contemporânea', True)
    # mani.michelin = 1
    # print(vars(mani))

if __name__ == '__main__':
    main()