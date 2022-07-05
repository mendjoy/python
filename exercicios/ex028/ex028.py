#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
n=randint(0,5) #Faz o computador 'PENSAR'
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-'*20)
n1=int(input('Em que número eu pensei?:')) #jogador tenta 'ADIVINHAR'
print('-=-'*20)
print('PROCESSANDO...')
sleep(3)
print('-=-'*20)
if n1==n:
    print('PARABÉNS!você acertou')
else:
    print('Você errou, eu venci!')
print('Eu pensei no número:{}'.format(n))
