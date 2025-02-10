

numInput = int(input(f'Digite um número para calcular seu fatorial: '))

fatorial = 1
resultado = ""

for c in range(numInput, 0, -1):
    fatorial *= c
    resultado += f"{c} X " if c > 1 else f"{c} = {fatorial}"

print(resultado)