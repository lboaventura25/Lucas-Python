##################
# Calculadora
##################

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
    "%": lambda x, y: y * (x / 100),
}

# Pergunta a expressão para o usuário
expr = input("expr> ")

# Adiciona espaço em volta dos operadores
for key in operators:
    expr = expr.replace(key, ' ' + key + ' ')
    
# Separa a expressao nos espacos
x, op, y = expr.split()  

# Recupera o operador a partir do símbolo
op = operators[op] 

# Calcula o resultado e exibe para o usuário
result = op(float(x), float(y))
print('O resultado é', result)
