inp = int(input('Digite um número inteiro: '))


def calcNumber(num):
    dobro = num * 2
    triplo = num * 3
    raiz = num ** (1/2)
    return (
        print(f'o dobro de {num} é {dobro}'),
        print(f'o triplo de {num} é {triplo}'),
        print(f'a raiz  quadra de {num} é {raiz}')
    )

calcNumber(inp)