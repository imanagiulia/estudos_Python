from exercicios.ex115.lib.interface import cabeçalho


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>5} anos')
    finally:
        a.close()


def cadastrar(arq, n='Desconhecido', i=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro na abertura do arquivo!')
    else:
        try:
            a.write(f'\n{n};{i}')
        except:
            print('Erro ao adicionar os dados no arquivo!')
        else:
            print(f'Novo registro {n} adicionado!')
            a.close()