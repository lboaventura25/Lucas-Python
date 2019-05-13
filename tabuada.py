num = int(input('Digite um número para ver sua tabuada: '))

print('-' * 12)

for i in range(10):
    d = i + 1
    print('{} x {:2} = {}'.format(num, d, (num * d)))

print('-' * 12)

