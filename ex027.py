# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint

while True:
    try:
        inputQuant = int(input('Quantos jogadores você quer cadastrar? '))
        if inputQuant > 0:
            break
        else:
            print('O número deve ser maior que zero!')
    except ValueError:
        print('DIGITE UM NÚMERO INTEIRO VÁLIDO!')

players = []

for player in range(1, inputQuant + 1):
    numberSorted = randint(1, 7)
    playerName = str(input(f'Qual o nome do  {player}º jogador? '))
    print(f'O número sorteado do {player}º jogador foi {numberSorted}')
    print('-='*10)

    playersDict = {
        'nome': playerName,
        'numSorteado': numberSorted,
    }
    players.append(playersDict)


print('=='*20)

position = 1
sortedPlayers = sorted(players, key=lambda x: x["numSorteado"], reverse=True)

for i, player in enumerate(sortedPlayers, start=1):
    # Se não for o primeiro jogador e o número for diferente do anterior, atualiza a posição

    if i > 1 and player["numSorteado"] != sortedPlayers[i-2]["numSorteado"]:
        position = i

    print(f'o Jogador {player["nome"]} ficou em {position}º lugar com número {player["numSorteado"]}')
