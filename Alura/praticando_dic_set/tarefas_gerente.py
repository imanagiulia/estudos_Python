equipe_a = set(input('Equipe_a = ').split(', '))
equipe_b = set(input('Equipe_b = ').split(', '))

listas_unificadas = equipe_a.union(equipe_b)

print('Suas tarefas:')
for tarefa in listas_unificadas:
    print(f'- {tarefa}')

tarefa_a_remover = input('Qual tarefa deseja remover da lista de tarefas: ').lower().strip()
if tarefa_a_remover in listas_unificadas:
    listas_unificadas.remove(tarefa_a_remover)
    print('Tarefa excluída com sucesso!')

print('Suas tarefas:')
for tarefa in listas_unificadas:
    print(f'- {tarefa}')
