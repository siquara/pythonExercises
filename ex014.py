#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


userNumber = int(input("Digite um número inteiro entre 0 e 20: "))

numbers = ("zero", "um", "dois", "três", "quatro", "cinco", "seis","sete", "oito", "nove", "dez", "onze", "doze",
             "treze","quatorze", "quinze", "dezesseis", "dezesete", "dezoito", "dezenove", "vinte")

while userNumber < 0 or userNumber > 20:
    print('NÚMERO INVÁLIDO! Digite um número no intervalo entre 0 e 20!!!!')
    userNumber = int(input("Digite um número inteiro entre 0 e 20: "))

print(f"O número {userNumber} em extenso é {numbers[userNumber]}")