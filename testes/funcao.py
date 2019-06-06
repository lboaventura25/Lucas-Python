def is_even(n):
    """
    Retorna True se o argumento for par.
    """
    return n % 2 == 0
        
def is_odd(n):
    """
    Retorna True se o argumento for ímpar.
    """
    return n % 2 != 0   
        
def sqrt(x):
    """
    Calcula a raiz quadrada de x.
    """
    r = 1
    for _ in range(200):
        r = 0.5 * (r + x/r) 
    return r
    
def fibo(n):
    """
    Retorna uma lista com os n primeiros numeros de 
    Fibonacci.
    """
    x, y = 0, 1
    numeros = [0, 1]
    for i in range(n - 2):
        x, y = y, x + y
        numeros.append(y)
        
    return numeros
    
def is_prime(n):
    """
    Retorna True se o n for primo
    """
    cont = 0
    for i in range(n):
        if (n % (i + 1)) == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False

def have_vowel(text):
    """
    Retorna True se a frase tiver pelo menos 5 vogais
    """
    cont = 0
    for ch in text:
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            cont += 1
    if cont >= 5:
        return True
    else:
        return False

def squared_list(lst):
    """
    Retorna o quadrado de cada termo da lista
    """
    square = []
    power = 0
    for i in lst:
        power = i**2
        square.append(power)
    return square

def add_of_squared_list(lst):
    """
    Retorna a soma dos elementos da lista ao quadrado
    """
    add = 0
    lsts = squared_list(lst)
    for i in lsts:
        add += i
    return add

def check(number, n):
    """
    Retorna True se houver o n no number
    """
    cont = 0
    mod = 0
    while number != 0:
        mod = number % 10
        if mod == n:
            cont += 1
        number /= 10
    if cont > 0:
        return True
    else:
        return False

def popular_words(text, lst):
    """
    Retorna a frequência dos termos de lst em text
    """
    cont = []
    lim = 0
    for key in lst:
        lim = 0
        if key in text:
            lim = text.count(key)
        if key.upper() in text:
            lim = text.count(key.upper())
        if key.lower() in text:
            lim = text.count(key.lower())
        cont.append(lim)
    return dict(zip(lst, cont))

def find_message(text):
    """
    Retorna a mensagem decifrada
    """
    lst = []
    message = str()
    for ch in text:
        if ch.isupper():  
            lst.append(ch)
    for ch in lst:
        message += ch
    return message

def checkio(*args):
    """
    Retorna a mensagem decifrada
    """
    maior = -101
    menor = 101
    inter = int(0)
    if not args:
        return 0
    for key in args:
        if key > maior:
            maior = key
        if key < menor:
            menor = key
    if type(menor) == float or type(maior) == float:
        return float(round(maior - menor, 3))
    if type(menor) == int and type(maior) == int:
        return int(maior - menor)