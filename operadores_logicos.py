entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = 'laptop'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print('lap' not in senha_digitada)
print('lap' in senha_digitada)
