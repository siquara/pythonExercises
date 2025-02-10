# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.


times_brasileirao_2025 = (
    'Atlético-MG', 'Bahia', 'Botafogo', 'Ceará', 'Corinthians',
    'Cruzeiro', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio',
    'Internacional', 'Juventude', 'Mirassol', 'Palmeiras', 'Red Bull Bragantino',
    'Santos', 'São Paulo', 'Sport', 'Vasco da Gama', 'Vitória'
)


print(f'Os 5 primeiros times são: {times_brasileirao_2025[0:5]}\n'
      f'Os 4 últimos são: {times_brasileirao_2025[-4:]}\n'
      f'Times em Ordem Alfabética: {sorted(times_brasileirao_2025)}\n'
      f'o Vitória está na {times_brasileirao_2025.index('Vitória') + 1}º posição\n')

