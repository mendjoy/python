#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
import time
import math
n=int(input('Digite um número qualquer:'))
n1=n%2
print('-=-'*20)
print('...Analisando o número: {}...'.format(n))
print('-=-'*20)
time.sleep(3)
if n1==1:
    print('O numero {} é IMPAR!'.format(n))
else:
    print('O número {} é PAR!'.format(n))

