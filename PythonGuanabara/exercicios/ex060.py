num = int(input('Digite o núemro que deseja saber o fatorial: '))
fatorial = 1
while num != 1:
    print('{} x '.format(num), end='')
    fatorial *= num
    num -= 1
    if num == 1:
        print('{} = {}'.format(num, fatorial))
