
numero = input('Vou dobrar o número que for digitado: ')

try:
    numero_float = float(numero)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

veloc_carro_passou_radar1 = velocidade > RADAR_1
carro_multado_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

if veloc_carro_passou_radar1:
    print('O carro passou da velocidade máxima')

if veloc_carro_passou_radar1 and carro_multado_radar1:
    print('Carro multado no radar 1')
