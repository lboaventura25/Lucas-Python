# Calculadora

# Dicionário de operadores
operators = {
    "+": lambda x, y: x + y, 
    "-": lambda x, y: x - y, 
    "*": lambda x, y: x * y, 
    "x": lambda x, y: x * y, 
    "/": lambda x, y: x / y,
    "÷": lambda x, y: x / y,
    "^": lambda x, y: x ** y,
    "**": lambda x, y: x ** y,
}

expr = input("expr> ")
expr = (expr
        .replace('+', ' + ')
        .replace('-', ' - ')
        .replace('/', ' / ')
        .replace('*', ' * '))

x, op, y = expr.split()  # separa a expressao nos espacos
op = operators[op]       # 
result = op(float(x), float(y))
print('O resultado é', result)

# cos(x) = x**0/0! - x**2/2! + x**4/4! - x**6/6! + ...
from math import pi

x = pi / 4

def cos(dg):
    x = pi * dg / 180
    return sum_to_convergence(
        (-1)**(n // 2) * x**n / fat(n) 
        for n in even_numbers()
    )
    
print(cos(45))