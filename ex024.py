quantInput = int(input(f'Quantos números você quer cadastrar? '))
numbers = [ ]
for c in range(1, quantInput + 1):
    numberInput = int(input(f'Digite o {c}º número: '))
    numbers.append(numberInput)
    print("-------")

pares = [num for num in numbers if num % 2 == 0]
impares = [num for num in numbers if num % 2 == 1]

print(f'pares: {pares}')
print(f'impares: {impares}')



