#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
cont=n=0
while True:
    print('='*40)
    n=int(input('Quer ver a tabuada de qual número?:'))
    if n <0:
        break
    print('='*40)
    for c in range (0,11):
        count = +1
        print(f'{n} x {c} = {n*c}')
