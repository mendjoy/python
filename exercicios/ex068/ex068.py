#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele
# conquistou no final do jogo.
from random import randint
print('*'*40)
print('...JOGO DO PAR OU IMPAR...')
print('*'*40)
jogador=computador=v=0
while True:
    jogador=int(input('Diga um valor:'))
    print('-'*40)
    computador=randint(0,11)
    total=computador+jogador
    tipo=' '
    while tipo not in 'PI':
        tipo= str(input('Par ou impar [P/I]?:')).upper().strip()[0]
    print(f'voce jogou {jogador} e o computador jogou {computador} a soma entre os dois foi:{total}')
    if tipo =='P':
        if total %2==0:
            print('VOCE GANHOU!')
            v+=1
        else:
            print('VOCE PERDEU!')
            break
    elif tipo == 'I':
        if total %2==1:
            print('VOCE VENCEU!')
            v+=1
        else:
            print('VOCE PERDEU!')
            break
    print('...Vamos jogar novamente...')
print('Voce venceu {} vezes'.format(v))



#
