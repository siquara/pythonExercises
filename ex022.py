#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
# se a expressão passada está com os parênteses abertos e fechados na ordem correta.


quantInput = str(input(f'Digite a Expressão: '))

expression = list(quantInput)


left = expression.count("(")
right = expression.count(")")

if left == right:
    print('A expressão tem a quantidade correta de parenteses')
else:
    print("Expressão invalida")



