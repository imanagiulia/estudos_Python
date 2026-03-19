
def validador_url(url: str):
    url.lower().strip()
    valido = ['https://', '.com']
    inicio_url = url[:8]
    final_url = url[-4:]

    if inicio_url == valido[0] and final_url == valido[1]:
        return "URL válida!"
    else:
        return "URL inválida!"
    

url = input('Digite a URL para validação: ')

print(validador_url(url))

    