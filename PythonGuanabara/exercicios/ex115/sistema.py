from time import sleep
from exercicios.ex115.lib.interface import *
from exercicios.ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


cabeçalho('SISTEMA ARQUIVO v1.0')
while True:
    resp = menu(['Ver Pessoas Cadastrada', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = input('Nome: ').capitalize()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('\033[36mSaindo do sistema... Até logo!\033[m')
        break
    else:
        print('\033[31m [ERRO] Digite uma opção válida!\033[m')
    sleep(0.7)


