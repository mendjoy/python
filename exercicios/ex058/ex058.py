#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep
computador=randint(0,10)
print('='*40)
print('...Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('='*40)
jogador=int(input('Em que número eu pensei?'))
print('='*40)
print('...PROCESSANDO...')
print('='*40)
sleep(1)
acertou=False
tentativas=0
while not acertou:
    tentativas=tentativas +1
    if jogador==computador:
        acertou=True
    else:
        if jogador > computador:
              jogador=int(input('Menos... Digite novamente:'))
        if jogador < computador:
            jogaddor=int(input('mais... Digite novamente:'))
print('Parabens, voce venceu e acertou com {} tentativas'.format(tentativas))