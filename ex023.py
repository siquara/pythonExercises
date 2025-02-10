#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

# perguntar o que seria list comprehension


quantInput = int(input(f'Quantas pessoas você quer cadastrar? '))
groupPeople=[]
maior_peso = menor_peso = 0

for c in range(1, quantInput + 1):
    nome = str(input(f'Digite o nome da {c}ª pessoa: '))
    peso = float(input(f'Digite o peso da: '))
    print("-------")
    groupPeople.append([nome, peso])

    if maior_peso == 0 or peso > maior_peso:
        maior_peso = peso
    if menor_peso == 0 or peso < menor_peso:
        menor_peso = peso


#Entender melhor como funciona esse filtro.
pessoas_mais_pesadas = [pessoa[0] for pessoa in groupPeople if pessoa[1] == maior_peso]
pessoas_mais_leves = [pessoa[0] for pessoa in groupPeople if pessoa[1] == menor_peso]

print(f'Foram cadastrados {len(groupPeople)} pessoas')

print(f'\nPessoas mais pesadas (peso: {maior_peso} kg):')
for nome in pessoas_mais_pesadas:
    print(f'- {nome}')

print(f'\nPessoas mais leves (peso: {menor_peso} kg):')
for nome in pessoas_mais_leves:
    print(f'- {nome}')


