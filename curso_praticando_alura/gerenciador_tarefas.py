def adicionar_tarefa(lista):
    tarefa = input('Digite a tarefa: ')
    lista.append(tarefa)
    
    return 'Tarefa adicionada com sucesso!'

def remover_tarefa(lista):
    if len(lista) == 0:
        return 'ERRO: Nenhuma tarefa a ser removida!'
    
    vizualizar_tarefa(lista)

    try:
        item = int(input('Digite o número da tarefa a ser removida: '))
        lista.pop(item)
    except ValueError:
        print('ERRO: Entrada inválida! Digite um número')
    except IndexError:
        print(f'ERRO: Número inválido! Digite um número entre 0 e {len(lista) - 1}')

    return 'Tarefa removida com sucesso!'

def vizualizar_tarefa(lista):
    cont = 0

    print('+++' * 10)

    print('Suas tarefas: ')
    for tarefa in lista:
        print(f'[{cont}] - {tarefa}')
        cont += 1

    print('+++' * 10)

def gerenciador(lista):
    while True:
        op = int(input("""Qual operação você deseja realizar? 
                        [1] -  Adicionar tarefa
                        [2] -  Visualizar tarefa
                        [3] -  Remover tarefa
                        [4] -  Sair
                        Escolha uma opção: """))
        match op:
            case 1:
                print(adicionar_tarefa(lista))
            case 2:
                vizualizar_tarefa(lista)
            case 3:
                print(remover_tarefa(lista))
            case 4:
                print('Saindo do gerenciador de tarefas. Até mais!')
                break
            case _:
                print('ERRO: Opção inválida! Escolha uma opção entre 1 e 4.')

