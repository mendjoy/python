#Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
print('='*40)
print('...SEQUENCIA DE FIBONACCI...')
print('='*40)
n=int(input('Quantos termos voce quer mostar?:'))
t1=0
t2=1
print('='*40)
print('{}-{}'.format(t1,t2),end='')
count=3
while count <=n:
    t3=t1+t2
    print('-{}'.format(t3),end='')
    t1=t2
    t2=t3
    count = count + 1