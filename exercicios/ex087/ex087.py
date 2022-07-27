#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maiorv = somatc = 0

for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))
print('+-' * 30)
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c] :^5}]', end= '')
        if matriz[l][c] % 2 == 0:
            somapar = somapar + matriz[l][c]
    print()
print('+-' * 30)
print(f'A soma dos valores pares é: {somapar}')

for l in range (0, 3):
    somatc = somatc + matriz [l][2]
print(f'A soma dos valores da terceira colune é: {somatc}')

for c in range (0,3):
    if c == 0:
        maiorv = matriz[1][c]
    elif matriz[1][c] > maiorv:
        maiorv = matriz[1][c]
print(f'O maior valor da segunda linha é: {maiorv}')
