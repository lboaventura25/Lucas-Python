L = []
N = []

for x in range(10):
    L.append(input('Digite um número: '))

for i in range(10):
    N.append(i + (5 * i))
    L[i] = N[i]

for l in range(10):
    print('N[{}] = {} ***** L[{}] = {}'.format(l, N[l], l, L[l]))
