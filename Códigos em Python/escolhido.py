import random

student1 = str(input('Digite o nome do aluno 1: '))
student2 = str(input('Digite o nome do aluno 2: '))
student3 = str(input('Digite o nome do aluno 3: '))
student4 = str(input('Digite o nome do aluno 4: '))

lista = [student1, student2, student3, student4]
escolhido = random.shuffle(lista)

print("A ordem de apresentação será {}.".format(lista))

