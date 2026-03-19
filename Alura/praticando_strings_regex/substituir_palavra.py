def substitur_palavra():
    texto = input('Digite o texto a ser revisado: ').lower().split()
    palavra = input('Digite a palavra que deseja substituir: ').lower()
    nova_palavra = input(f"Digite por qual palavra '{palavra}' será substituída: ").lower()

    texto_alterado = str(texto).replace(palavra, nova_palavra)

    return texto_alterado

print(substitur_palavra())
