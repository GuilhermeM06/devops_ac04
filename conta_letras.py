def conta_letras(palavra: str) -> dict:
    ocorrencias = {}
    for letra in palavra:
        if letra not in ocorrencias:
            ocorrencias[letra] = 0
        ocorrencias[letra] += 1
    return ocorrencias


print(conta_letras('abacate'))
