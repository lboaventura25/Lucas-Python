def dobra(x):
        """Retorna o dobro do argumento"""
        return x + x

def add(x, y):
        return x + y

def mul(x, y):
        return x * y

def div(x, y):
        return x / y

def sub(x, y):
        return x - y

# Calculadora

# Dicionário de operadores
operators = {
        "+": add,
        "-": sub,
        "*": mul, 
        "/": div
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
