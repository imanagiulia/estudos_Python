
def ficha(n='', g=0):
    if n == '':
        return f'O jogador(a) <desconhecido> marcou {g} gols.'
    elif g == 0:
        return f'O(A) jogador(a) {n} marcou 0 gol.'
    else:
        return f'O(A) jogodar(a) {n} marcou {g} gols.'


nome = input('NOME JOGADOR(A): ').capitalize()
gols = input('NÚMERO DE GOLS JOGADOR(A): ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

print(ficha(nome, gols))

