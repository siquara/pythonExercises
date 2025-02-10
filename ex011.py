
numbers = []

for c in range(1,7):
    numInput = int(input(f'Digite o nº{c}: '))

    if numInput % 2 == 0:
        numbers.append(numInput)


print(f' A soma dos números pares é {sum(numbers)}')
