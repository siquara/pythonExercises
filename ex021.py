#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter
# apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.


quantInput = int(input(f'Quantos valores você quer digitar? '))
listValores = []
listPares = []
listImpares = []

for c in range(1, quantInput + 1):
    valor = int(input(f'Digite o {c}º valor: '))
    if listValores.count(valor) == 0:
        listValores.append(valor)
        if valor % 2 == 0:
            listPares.append(valor)
        else:
            listImpares.append(valor)

print(f'Todos os valores digitados: {listValores}\n'
      f'Os valores pares: {listPares}\n'
      f'Os valores impares: {listImpares}')