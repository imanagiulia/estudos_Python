# escrever em um arquivo com a função open()
with open('teste.txt',  'w') as f: # write
    f.write('Olá, mundo!')

with open('teste.txt', 'a') as f:
    f.write('Outra coisa') # append

# lendo um arquivo com a função open()
with open('teste.txt', 'r') as f: # read
    conteudo = f.read()
print(conteudo)


