#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.
listan=[]
n=0
pares=[]
impares=[]
while True:
    n=int(input('Digite um número:'))
    resp = str(input('Quer continuar? [S/N]:')).upper().strip()[0]
    if resp not in 'SN':
        resp = str(input('Opação invalida, digite novamente. Quer continuar? [S/N]:')).upper().strip()[0]
    if resp in 'N':
        break
    if n % 2 ==0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Os números pares digitados foram: {pares}.')
print(f'Os números impares digitados foram:{impares}.')
listan=(pares + impares)
print(f'Todos os números digitados foram: {listan}.')
