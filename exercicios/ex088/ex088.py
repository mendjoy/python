#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
lista = list()
tot=1
jogos = list()
print('-' * 40)
print ('          JOGA DA MEGASENA       ')
print('-' * 40)

vezesjogos = int(input('Quantas vezes você quer sortear?:'))
while tot <= vezesjogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-' * 40)
print(f'     SORTEANDO {vezesjogos} JOGO(s)     ')
print('-' * 40)
for i, l  in enumerate (jogos):
    print(f' Jogo {i + 1}: {l}')
    sleep(1)
print('*********BOA SORTE!********')

