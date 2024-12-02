
def voto(anoNasc):
    from datetime import datetime
    idade = datetime.now().year - anoNasc

    if idade < 16:
        return f'Com {idade} anos : NEGADO'
    elif  16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos : OPCIONAL'
    else:
        return f'Com {idade} anos : OBRIGATÓRIO'


anoNascimento = int(input('Em que ano vc nasceu? '))

print(voto(anoNascimento))


