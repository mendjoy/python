#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
import math
n=int(input('Digite um número inteiro:'))
print('''Escolha um das bases abaixo para conversão
[1] converter para binário
[2] converter para octal')
[3] converter para hexadecimal''')
n1=int(input('Sua opção:'))
if n1==1:
    print('O número {} convertido para binario é {}'.format(n,bin(n)[2:]))
elif n1==2:
    print('O numero {} convertido para octal é {}'.format(n,oct(n)[2:]))
elif n1==3:
    print('O numero {} convertido para hexadecimal é {}'.format(n,hex(n)[2:]))
else:
    print('Opção invalida')
