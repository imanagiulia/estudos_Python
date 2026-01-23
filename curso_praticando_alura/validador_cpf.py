def verificar_numeros_cpf(cpf):
    if not cpf.isdigit():
        return "Erro: O CPF deve conter apenas números."
    
    qtd_num = len(cpf)

    if qtd_num != 11:
        return "Erro: O CPF deve ter exatamente 11 dígitos."
    
    return 'CPF válido'
    
