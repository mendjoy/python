#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#quantas pessoas tem mais de 18 anos.
#quantos homens foram cadastrados.
#quantas mulheres tem menos de 20 anos.
cont=homem=mulher=tot18=0
while True:
    print('-'*40)
    print('...CADASTRE UMA PESSOA...')
    print('-'*40)
    idade=int(input('Idade:'))
    cont=cont+1
    sexo= ' '
    while sexo not in 'FM':
        sexo=str(input('Sexo:')).upper().strip()[0]
    if idade >=18:
        tot18+=1
    if sexo in 'M':
        homem=homem+1
    if sexo == 'F' and idade < 20:
        mulher=mulher+1
    continuar=' '
    while continuar not in 'SN':
        continuar=str(input('Quer continuar [S/N]?:')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Foram cadastradas {cont} pessoas. Dessas {tot18} pessoas são maiores de idade')
print(f'{mulher} são mulheres com menos de 20 anos.')
print(f'{homem} homens foram cadastrados.')

