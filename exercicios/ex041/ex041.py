#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER
from datetime import date
nasci=int(input('Qual o ano de nascimento do atleta?:'))
idade=(date.today().year)-nasci
print('O atleta possui {} anos'.format(idade))
if idade <=9:
    print('O atleta faz parte da categoria MIRIM')
elif idade >9 and  idade <=14:
    print('O atleta faz parte da categoria INFANTIL')
elif idade >14 and idade <=19:
    print('O atleta faz parte da categoria JUNIOR')
elif idade >19 and idade <25:
    print('O atleta faz parte da categoria SÊNIOR')
elif idade > 25:
    print('O atleta faz parte da categoria MASTER')

