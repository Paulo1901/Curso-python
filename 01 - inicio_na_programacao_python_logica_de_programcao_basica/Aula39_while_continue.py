"""

while continue

"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print(f'Não mostreo numero {contador}')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    if contador == 39:
        print('Não mostrar mais')
        continue

    print(contador)

    if contador == 40:
        break 

print('Acabou!')