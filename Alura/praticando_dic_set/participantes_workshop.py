participantes = { 

    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

} 

aluno_a_remover = input('Nome do aluno a ser removido: ').capitalize()

for workshop, nomes in participantes.items():
    nomes.discard(aluno_a_remover)

print('Lista atualizada: ')
for workshop, nomes in participantes.items():
    print(f'- {workshop}: {nomes}')