# Não edite a lista de usuários
USUARIOS = [
    {
        'nome': 'Ada Lovelace',
        'emails': ['ada@gmail.co.uk', 'algo-ada@hotmail.com'],
        'nascimento': (1815, 12, 10),
        'senha': 'algoritmo',
    },
    {
        'nome': 'Alan Turing',
        'emails': ['turing@gmail.co.uk'],
        'nascimento': (1912, 6, 23),
        'senha': 'enigma',
    },
    {
        'nome': 'Grace Hopper',
        'emails': ['amazing-grace@usnavy.gov'],
        'nascimento': (1906, 12, 9),
        'senha': 'cobol',
    },
    {
        'nome': 'Donald Knuth',
        'emails': ['knuth@gmail.com', 'art-of-programming@caltech.edu'],
        'nascimento': (1938, 1, 10),
        'senha': 'LaTeX',
    },
]

def login(email, senha):
    """
    Retorna um usuário caso o e-mail e senha estejam corretos. Retorna None caso contrário.
    """
    cont = 0
    for key in USUARIOS:
        for i in USUARIOS[cont]['emails']:
            if i == email:
                if senha == USUARIOS[cont]['senha']:
                    return USUARIOS[cont]
        cont += 1
    return None


def recuperar_senha(email, nascimento):
    """
    Mostra a senha do usuário ou uma mensagem de erro caso o e-mail seja 
    inválido ou a data de nascimento não corresponda à correta.
    """
    cont = 0
    for key in USUARIOS:
        for i in USUARIOS[cont]['emails']:
            if email == i:
                if USUARIOS[cont]['nascimento'] == nascimento:
                    return 'A senha é "{}"'.format(USUARIOS[cont]['senha'])
        cont += 1
    return 'Data de nascimento ou e-mail inválidos'


"Testes para a função de login()"

assert login('turing@gmail.co.uk', 'enigma') == USUARIOS[1]
assert login('turing@gmail.co.uk', 'password-incorreto') is None
assert login('ada@gmail.co.uk', 'algoritmo') == USUARIOS[0]
print('Lucas você é o cara!')

"Testes para a função de login() - múltiplos e-mails"

assert login('knuth@gmail.com', 'LaTeX') == USUARIOS[-1]
assert login('art-of-programming@caltech.edu', 'LaTeX') == USUARIOS[-1]
assert login('art-of-programming@caltech.edu', 'latex') is None
print('Lucas você é o cara!')

"Testes para a função recuperar_senha() - casos de sucesso"

assert recuperar_senha('turing@gmail.co.uk', (1912, 6, 23)) == 'A senha é "enigma"'
assert recuperar_senha('amazing-grace@usnavy.gov', (1906, 12, 9)) == 'A senha é "cobol"'
print('Lucas você é o cara!')

"Testes para a função recuperar_senha() - casos de erro"

assert recuperar_senha('turing@gmail.co.uk', (1901, 2, 30)) == 'Data de nascimento ou e-mail inválidos'
assert recuperar_senha('bad@email.com.br', (1912, 6, 23)) == 'Data de nascimento ou e-mail inválidos'
print('Lucas você é o cara!')
