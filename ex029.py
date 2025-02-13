#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


inputName = str(input('Digite o nome do jogador: '))
inputMatch = int(input(f'Digite quantas partidas {inputName} jogou: '))

goals = []

for partida in range(inputMatch):
    goalsInput = int(input(f'Digite a quantidade de gols na {partida + 1}ª partida: '))
    goals.append(goalsInput)

totalGoals = sum(goals)

dictPlayer = {
    'nome': inputName,
    'quantidade de Partidas': inputMatch,
    'gols por partidas': goals,
    'total de Gols': totalGoals,
}
print(dictPlayer)

for partida in enumerate(goals, start=1):
    print(f'Na {partida[0]}ª partida {inputName} fez {partida[1]} gols.')

