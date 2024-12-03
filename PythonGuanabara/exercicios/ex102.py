
def fatorial(n=1, mostrar=0):
    tot = 1
    num = n
    if mostrar:
        print(f'Fatorial de {n}: ', end='')
        while n != 0:
            print(f' {n} ', end='')
            if n > 1:
                print('x', end='')
            tot *= n
            n-=1
        print(f'= {tot}', end='')
    else:
        while n >= 1:
            tot *= n
            n-=1
        print(f'{num}! = {tot} ')


print(fatorial(5, True))