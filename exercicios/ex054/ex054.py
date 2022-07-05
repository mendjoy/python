#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
totamaior=0
totamenor=0
for c in range (1,8):
    atual=date.today().year
    nasc=int(input('Digite o {}ºano de nascimento:'.format(c)))
    idade = atual - nasc
    if idade>=18:
        totamaior=totamaior+1
    else:
        totamenor=totamenor+1
print('Ao todo {} pessoas atingiram a maioridade'.format(totamaior))
print('Ao todo {} não atingiram a maioridade'.format(totamenor))


