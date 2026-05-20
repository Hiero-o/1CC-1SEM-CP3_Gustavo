temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]


def media_temp(sala):
    media = sum(temperaturas[sala]) / len(temperaturas[sala])
    return media


def quantidade_critico(sala):
    contador = 0

    for temperatura in temperaturas[sala]:
        if temperatura >= 33:
            contador += 1

    return contador


for i in range(len(temperaturas)):
    print(f"Sala {i+1}")
    print(f"Média de temperaturas: {media_temp(i)}")
    print(f"Registros críticos: {quantidade_critico(i)}")
    print()