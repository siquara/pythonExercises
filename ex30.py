#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média


while True:
    try:
        inputQuant = int(input('Quantas pessoas você quer cadastrar? '))
        if inputQuant > 0:
            break
        else:
            print('O número deve ser maior que zero!')
    except ValueError:
        print('DIGITE UM NÚMERO INTEIRO VÁLIDO!')


def validadeSex(nome):
    while True:
        sexo = input(f'Qual sexo de {nome}? [F/M/I] ').upper()
        if sexo in ['F', 'M', 'I']:
            return sexo
        print('Digite um valor válido! (F, M ou I)')

def validadeAge(nome):
    while True:
        try:
            idade = int(input(f'Qual idade de {nome}? '))
            if idade >=0:
                return idade
        except ValueError:
            print('Digite um número válido para a idade.')

def MediaCalc(idade):
    total = len(idade)
    media = sum(idade) / total
    return media

people = []

for person in range(1, inputQuant + 1):
    nome = str(input(f'Digite o Nome da {person}ª pessoa: ')).capitalize()

    sexo =validadeSex(nome)
    idade = validadeAge(nome)

    personDic = {
        'nome': nome,
        'sexo': sexo,
        'idade': idade,
    }
    people.append(personDic)
    print('-=' * 30)


print(people)

print(f'Foram cadastradas {len(people)} pessoas')


peopleAge = [person['idade'] for person in people]
media = MediaCalc(peopleAge)

print(f'Média de idade é {media} anos')

women = []
peolpleAgeMax = []
for person in people:
    if person['sexo'] == 'F':
        woman = person['nome']
        women.append(woman)
    if person['idade'] > media:
        peolpleAgeMax.append(person['nome'])

print(f'As mulheres cadastradas são {women}')

print(f'Pessoas com idade acima da média: {peolpleAgeMax}')
