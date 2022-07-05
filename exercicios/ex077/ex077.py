#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras=('APRENDER','PROGRAMAR', 'LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR',
          'MERCADO','PROGRAMADOR','FUTURO')
contv=0
for item in palavras:
    print(f'\nNa palavra "{item}" temos:', end='')
    for letra in item:
        if letra in 'AEIOU':
            print(letra, end='')
