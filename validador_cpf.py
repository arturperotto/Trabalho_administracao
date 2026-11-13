import re

def limpar_cpf(cpf: str) -> str:
    return re.sub(r"\D", "", cpf)

def validar_cpf(cpf: str) -> bool:
    cpf = limpar_cpf(cpf)

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    numeros = [int(digito) for digito in cpf]

    soma = sum(
        numero * peso
        for numero, peso in zip(numeros[:9], range(10, 1, -1))
    )

    resto = (soma * 10) % 11
    primeiro_digito = 0 if resto == 10 else resto

    if primeiro_digito != numeros[9]:
        return False

    soma = sum(
        numero * peso
        for numero, peso in zip(numeros[:10], range(11, 1, -1))
    )

    resto = (soma * 10) % 11
    segundo_digito = 0 if resto == 10 else resto

    if segundo_digito != numeros[10]:
        return False

    print(cpf)
    return True