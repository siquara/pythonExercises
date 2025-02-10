inp = int(input('Digite um número inteiro: '))


def calcNumber(num):
    ant = num -1
    suc = num + 1
    return print(f'o número digitado é {num} o antencessor desse número é {ant} e o sucessor é {suc}')

calcNumber(inp)