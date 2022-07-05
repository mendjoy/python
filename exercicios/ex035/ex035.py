#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
from time import sleep
n1=float(input('Digite o comprimento de uma reta em cm:'))
n2=float(input('Digite o comprimento de outra reta em cm:'))
n3=float(input('Digite o comprimento de mais uma reta em cm:'))
print('-=-'*20)
print('...Analisando as 3 retas...')
print('-=-'*20)
sleep(3)
if n1<n2+n3 and n2+n3 and n3<n1+n2:
    print('Os seguimentos acima PODEM FORMAR UM TRIANGULO')
else:
    print('Os seguimentos abaixo NÃO PODEM FORMAR UM TRIANGULO')