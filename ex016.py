#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem
# de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
numbers = []
for c in range(0, 5):
   sortedNumbers = numbers.append(randint(1,100))

max = max(numbers)
min = min(numbers)

print(numbers)
print(f'O maior valor é {max} e o menor é {min}')
