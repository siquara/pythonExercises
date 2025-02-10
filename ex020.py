#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.


quantInput = int(input(f'Quantos valores você quer digitar? '))
listValores = []

for c in range(1, quantInput + 1):
    valor = int(input(f'Digite o {c}º valor: '))
    if listValores.count(valor) == 0:
        listValores.append(valor)

print(f'Foram digitados {quantInput} números\n'
      f'Foram  adicionados {len(listValores)} valores\n'
      f'Lista de valores: {listValores}\n')

if listValores.count(5):
    print(f'O Número 5 foi digitado\n')
else:
    print('Nenhum o Número 5 não foi digitado')

