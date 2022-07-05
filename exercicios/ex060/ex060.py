#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
from math import factorial
n=int(input('Digite um número para calcular o seu fatorial:'))
f=factorial(n)
c=n

while c > 0:
    print( c,' x ' if c >1 else '=', end='' )
    c-=1

