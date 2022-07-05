#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconside
# rando o flag).
n=0
count=0
soma=0
while n != 999:
    n = int(input('Digite um número [999 para parar]:'))
    count = count +1
    soma=soma+n
    if n == 999:
        print('...ACABOU...')
print('A soma dos {} termos é: {}'.format(count-1,soma-999))

