def primos(n: int) -> list:
    lst = []
    if n>1:
        for i in range(n+1):
            cont = 0
            for j in range(i+1):
                if i%(j+1)==0:
                    cont += 1
            if cont==2:
                lst.append(i)
        return lst
    elif n<=1:
        return lst

primos(50)

"Testes com alguns primos"
assert primos(13) == [2, 3, 5, 7, 11, 13]
assert primos(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
assert primos(1)  == []
print('Parabéns!')