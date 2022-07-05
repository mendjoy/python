#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
n=str(input('Digite uma frase:')).strip().upper()
print('A letra "A" aparece {} vezes'.format(n1.count('A')))
print('A letra "A" aparece na primeira vez na posição: {}'.format(n.find('A')+1))
print('A ultima letra "A" aparece na posição:{}'.format(n.rfind('A')+1))