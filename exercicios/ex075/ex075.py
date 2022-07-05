#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
# em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

num = (int(input('Digite um número:')),
    int(input('Digite outro número:')),
    int(input('Digite mais um número:')),
    int(input('Digite o ultimo  número:')))
print(f'Você digitou os números:{num}')
print(f'O número 9 foi digitado {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na posição: {num.index(3)+1}')
for n in num:
    if n% 2 ==0:
        print(f'Os números par(es) são:{n}')

