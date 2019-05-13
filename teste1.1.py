def soma_dos_quadrados(n):
    """Soma os valores 1 + 2*2 + 3*3 + ... + n*n."""
    if n<=0:
        return 0
    else:
        sum = 0
        for i in range(n+1):
            sum = sum + i**2
        return sum

lay = soma_dos_quadrados(100)

"""Verifica se a função foi implementada corretamente."""
assert soma_dos_quadrados(10) == 385
assert soma_dos_quadrados(100) == 338350
assert soma_dos_quadrados(-42) == 0
print('Parabéns!')
print(lay)