studentNumberCount = int(input('Defina a quantiade de estudantes: '))
notesGroup = []


def mediaCalc(num):
    total = sum(num)
    calc = total / studentNumberCount
    return calc


for i in  range(studentNumberCount):
    notes = float(input(f'Defina a nota do estudante nº{i + 1}: '))
    notesGroup.append(notes)



print(f'A média do grupo é {mediaCalc(notesGroup)}')