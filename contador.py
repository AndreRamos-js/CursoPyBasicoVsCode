
"""
contador = 0

while contador < 20:
    contador = contador + 1
    print(contador)

print('Acabou!')
"""

contador = 0

while contador <= 100:
    contador = contador + 1
    
    if contador == 6:
        continue

    if contador >= 10 and contador <= 27:
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou!')
