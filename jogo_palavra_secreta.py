


palavra_secreta = 'python'
letras_acertadas = ''

while True:
    letra_digitada = input('Digite uma letra: ')
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue
    if not letra_digitada.isalpha():
        print('Digite apenas letras!')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    for letra in palavra_secreta:
        if letra in letras_acertadas:
            print(letra)
        else:
            print('*')
