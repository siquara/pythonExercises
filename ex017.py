numbers = []

while len(numbers) < 5:
    userNumber = int(input('Digite um número: '))
    numbers.append(userNumber)


print(f'Números digitados: {numbers}\n'
      f'o valor 9 apareceu por {numbers.count(9)} vezes')
if 3 in numbers:
    print(f'O valor 3 apareceu na posição {numbers.index(3)}º')
else:
    print('o número 3 não foi digitado')