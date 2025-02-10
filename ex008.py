import random


computerNumber = random.randint(1,5)

def compareNumbers(num1, num2):
    while True:
        if num1 == num2:
            print('Parabéns, você acertou!')
            break
        else:
            print('Você errou. Tente novamente...')
            num2 = int(input('Digite o número que eu pensei: '))


userNumber = int(input('Digite o número que eu pensei: '))
compareNumbers(computerNumber, userNumber)
