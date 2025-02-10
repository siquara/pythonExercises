#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


quantInput = int(input(f'Quantos valores você quer digitar? '))
listValores = []

for c in range(1, quantInput):
    valores = int(input(f'Digite o {c}º valor: '))
    listValores.append(valores)

maximo = max(listValores)
minimo = min(listValores)

print(f'O maior valor digitado foi {maximo} e o menor valor digitado foi {minimo}\n'
      f'Lista completa: {listValores}')