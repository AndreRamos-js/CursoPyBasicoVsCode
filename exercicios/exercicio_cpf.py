"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
"""

# Fatia o numero do CPF para obter apenas os 9 primeiros digitos
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

# Converte o digito para int e faz uma conta multiplicando cada digito por 10 e depois soma todos os resultados
resultado_1 = 0
for digito in nove_digitos:
    resultado_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -=1

''' Multiplica o resultado por 10 e pega o resto da divisão por 11.
    O resultado será o primeiro digito do CPF, caso o resultado seja maior ou igual a 9 o número será 0.
'''
digito_1 = (resultado_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

print(digito_1)

# Obter o 2º digito do CPF #
dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

# Converte o digito para int e faz uma conta multiplicando cada digito por 11 e depois soma todos os resultados
resultado_2 = 0
for digito in dez_digitos:
    resultado_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -=1

''' Multiplica o resultado por 10 e pega o resto da divisão por 11.
    O resultado será o primeiro digito do CPF, caso o resultado seja maior ou igual a 9 o número será 0.
'''
digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

print(digito_2)

# Faz a validação do CPF
cpf_valido = f'{nove_digitos}{digito_1}{digito_2}'

if cpf == cpf_valido:
    print(f'{cpf} é válido!')
else:
    print('CPF Inválido!')
