from time import sleep

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i > f:
        p = -p
    for n in range(i, f+1, p):
        print(f'{n} ', end='', flush=True)
        sleep(0.5)

    print('FIM!')
    print('-=' * 25)


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Final: '))
pas = int(input('Passo: '))

contador(ini, fim, pas)