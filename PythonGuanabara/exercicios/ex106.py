from time import sleep


def funçãoOuBiblioteca():
    while True:
        print('\033[30m\033[42m~' *25)
        print('Sistema de ajuda pyHELP')
        print('~' *25)

        resp = input('\033[mFunção ou biblioteca: ').lower()
        if resp == 'fim':
            print('\033[41m Até logo!')
            break
        else:
            print(f'\033[45m-' *40)
            print(f'Acessando documentação do comando {resp}')
            print(f'-' *40)
            sleep(1)
            print('\033[46m')
            help(f'{resp}')


funçãoOuBiblioteca()