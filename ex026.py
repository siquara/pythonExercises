#Faça um programa que leia nome e 3 notas do aluno, calcule a média, guardando também a situação em um dicionário. No final,
# mostre o conteúdo da estrutura na tela.

inputQuant=int(input('Quantos alunos você quer cadastrar ? '))
students = []

def mediaCalc(values):
    total = sum(values)
    calc = total/len(values)
    return calc

for student in range(1, inputQuant + 1):
    studentName = str(input(f'Digite o NOME do {student}º aluno: '))
    studentNotes = []
    for nota in range(1, 4):
        while True:
            note = float(input(f'Digite a {nota}ª nota do estudante {studentName}: '))
            if 0 <= note <= 10:
                studentNotes.append(note)
                break
            else:
                print('Erro: Digite uma nota entre 0 e 10!')


    media = mediaCalc(studentNotes)

    if media >= 6:
        situacao = 'APROVADO'
    else:
        situacao = 'REPROVADO'

    studentDict = {
        'nome': studentName,
        'notas': studentNotes,
        'media': round(media,2),
        'situacao': situacao
    }

    students.append(studentDict)
    print("---" *10)

for aluno in students:
    print(aluno)

