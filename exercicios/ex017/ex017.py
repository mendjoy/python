'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

'''n1=float(input('Digite o comprimento do cateto oposto:'))
n2=float(input('Digite o valor do comprimento do cateto adjacente:'))
h=(n1**2+n2**2)**1/2
print('A hipotenusa vai medir {}'.format(h))'''

import math
n1=float(input('Digite o comprimento do cateto adjacente:'))
n2=float(input('Digite o comprimento do cateto oposto:'))
h=math.hypot(n1,n2)
print('A hipotenusa vai medir {:.2f}'.format(h))


