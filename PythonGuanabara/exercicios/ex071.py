# notas disponiveis = 50, 20, 10, 1
""" minha resolução
print('=' *15)
print('   NAJU BANK')
print('=' *15)
notas50 = notas20 = notas10 = notas1 = 0
valorSacar = int(input('Qual o valor que você deseja sacar: '))
if valorSacar % 50 == 0:
    notas50 = valorSacar // 50
    valorSacar -= notas50 * 50
elif valorSacar % 50 != 0:
    notas50 = valorSacar // 50
    valorSacar = valorSacar % 50
if valorSacar % 20 == 0:
    notas20 = valorSacar // 20
    valorSacar -= notas20 * 20
elif valorSacar % 20 != 0:
    notas20 = valorSacar // 20
    valorSacar = valorSacar % 20
if valorSacar % 10 == 0:
    notas10 = valorSacar // 10
    valorSacar -= notas10 * 10
elif valorSacar % 10 != 0:
    notas10 = valorSacar // 10
    valorSacar = valorSacar % 10
if valorSacar % 1 == 0:
    notas1 = valorSacar // 1
    valorSacar -= notas10 * 1
elif valorSacar % 1 != 0:
    notas1 = valorSacar // 1
    valorSacar = valorSacar % 1

print(f'''Você receberá:
{notas50} notas de 50
{notas20} notas de 20
{notas10} notas de 10
{notas1}  notas de 1''')

"""
# resolução guanabara
print('=' *15)
print('   NAJU BANK')
print('=' *15)

valor = int(input('Valor que você deseja sacar: R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de {ced} reais')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break
