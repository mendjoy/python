#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
from time import sleep
itens=('PEDRA','PAPEL','TESOURA')
computador=randint(0,2)
print('VAMOS JOGAR JOKEN PÔ?')
print('Escolha uma opção:')
print('''[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogador=int(input('Qual a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('=-'*15)
print('O computador escolheu {}'.format(itens[computador]))
print('Você escolheu {}'.format(itens[jogador]))
print('=-'*15)
if computador ==0: #O computador jogou pedra
    if jogador ==0:
        print('EMPATE')
    elif jogador ==1:
       print('VOCÊ VENCEU')
    elif jogador ==2:
        print('O COMPUTADOR VENCEU')
    else:
        print('Jogada invalida')
elif computador ==1: #O computador jogou papel
    if jogador ==1:
        print('EMPATE')
    elif jogador ==0:
        print('O COMPUTADOR VENCEU')
    elif jogador==2:
        print('VOCE VENCEU')
    else:
        print('Jogada invalida')
elif computador ==2: #O computador jogou tesoura
    if jogador ==2:
        print('EMPATE')
    elif jogador ==0:
        print('VOCE VENCEU')
    elif jogador ==1:
        print('O COMPUTADOR VENCEU')


