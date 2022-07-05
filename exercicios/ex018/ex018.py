'''Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''
import math
n=float(input('Digite um angulo:'))
s=math.sin(math.radians(n))
c=math.cos(math.radians(n))
t=math.tan(math.radians(n))
print('O angulo de {} tem o SENO de {:.2f}'.format(n,s))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(n,c))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(n,t))
