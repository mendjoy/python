#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('='*30)
print('DEZ TEMOS DE UMA PROGRESSÃO ARITIMETICA')
print('='*30)
primeiro=int(input('Digite o primeiro termo:'))
razão=int(input('Digite a razão:'))
decimo= primeiro +(10-1)*razão
for c in range(primeiro,decimo+razão,razão):
    print('{}'.format(c),end=' ')

