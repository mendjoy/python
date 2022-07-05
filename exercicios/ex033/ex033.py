#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
import time
n1=int(input('Digite um número:'))
n2=int(input('Digite outro número:'))
n3=int(input('Digite mais um número:'))
print('-=-'*20)
print('...Analisando os numeros {}, {}, {}...'.format(n1,n2,n3))
print('-=-'*20)
time.sleep(3)
#Verificando quem é menor
menor=n1
if n2<n1 and n2<n3:
   menor=n2
if n3<n1 and n3<n2:
    menor=n3
#Analisando o maior número
maior=n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
print ('O menor valor digitado foi:{} e o maior valor digitado foi:{}'.format(menor, maior))

