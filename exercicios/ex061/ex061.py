#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('='*40)
print('Termos de uma pregressão aritimetica')
print('='*40)
primeiro=int(input('Digite o primeiro termo:'))
razao=int(input('Digite a razão:'))
termo=primeiro
count=1
while count <=10:
    print('{}-'.format(termo),end=' ')
    termo=termo+razao
    count= count+1
print('FIM')



