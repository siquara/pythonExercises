#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

personInformations = {}

personInformations["nome"] = str(input('Digite o nome: '))
inputYear = int(input('Digite o ano de nascimento: '))

age =  datetime.now().year - inputYear
personInformations["idade"] = age

inputCTPS = int(input('Digite o número da sua carteira de trabalho (0 não tem): '))

if inputCTPS > 0:
    inputYearCtps = int(input('Digite o ano de Contratação: '))
    inputSalary = float(input('Digite seu salário R$ '))

    retirementYear = inputYearCtps + 35
    retirementAge = retirementYear - inputYear

    personInformations["CarteiraDeTrabalho"] = inputCTPS
    personInformations["salario"] = inputSalary
    personInformations["Ano de Contratacao"] = inputYearCtps
    personInformations["Idade de aposentadoria"] = retirementAge

print(personInformations)

for k, v in personInformations.items():
    print(f'{k}: {v}')