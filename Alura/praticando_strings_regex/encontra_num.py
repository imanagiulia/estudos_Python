def extrai_num(texto: str):
    validos = ['0','1','2','3','4','5','6','7','8','9']
    receita = []
    
    for car in texto:
        if car in validos:
            receita.append(car)
    
    return receita


descricao = extrai_num(input('Digite a descrição da receita: '))
print('O número da receita foi: ',end='')
for n in descricao: print(n, end='')
