


palavra_secreta = 'python'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue
    
    if not letra_digitada.isalpha():
        print('Digite apenas letras!')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''

    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    
    print(f'Palavra formada: {palavra_formada}')

    if numero_tentativas == 20:
        print(f'*' * 30)
        print('VOCÊ PERDEU!')
        print('O número de tentativas acabou.')
        print(f'A palavra secreta era: {palavra_secreta}')
        print(f'*' * 30)
        break

    if palavra_formada == palavra_secreta:
        print(f'*' * 30)
        print('PARABÉNS VOCê GANHOU!')
        print(f'A palavra secreta era: {palavra_secreta}')
        print(f'Tentativas: {numero_tentativas}')
        print(f'*' * 30)
        break
