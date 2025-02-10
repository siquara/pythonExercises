# Estruturas de Repetição

num = int(input(f'Digite um número: '))
pares = []
for c in range(0, num):
   decrement = num - c

   if decrement % 2 == 0:
       pares.append(decrement)

print(f'Os números pares até {num} são : {pares}')