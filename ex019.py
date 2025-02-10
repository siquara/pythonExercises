#rie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente


quantInput = int(input(f'Quantos valores você quer digitar? '))
listValores = []

for c in range(1, quantInput):
    valor = int(input(f'Digite o {c}º valor: '))
    if listValores.count(valor) == 0:
        listValores.append(valor)

maximo = max(listValores)
minimo = min(listValores)

print(f'O maior valor digitado foi {maximo} e o menor valor digitado foi {minimo}\n'
      f'Lista completa: {sorted(listValores)}')