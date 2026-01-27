class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return (f'Nome: {self.nome} | Artista: {self.artista} | Duração: {self.duracao}')

musica_1 = Musica('Relicário', 'ANAVITÓRIA', 245 )

musica_2 = Musica('Clareou', 'Pixote', 243)

musica_3 = Musica('Nike e shortinho', 'Marvvila', 241)


print(musica_1)
print(musica_2)
print(musica_3)