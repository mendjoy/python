#Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
n=soma=count=0
while True:
    n=int(input('Digite um número [999 para parar]:'))
    if n ==999:
        break
    soma = soma + n
    count = count + 1
print(f'Foram digitados {count} números e a soma entre eles é: {soma}.')

