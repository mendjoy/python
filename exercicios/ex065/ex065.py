#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
n=count=soma=0
n2='Ss'
maior= 0
menor=0
while n2 in 'Ss':
    n = int(input('Digite um número:'))
    soma = soma + n
    count = count + 1
    n2 = str(input('Quer continuar [S/N]?:')).upper().strip()[0]
    if count ==1:
        maior=menor=n
    else:
        if n > maior:
            maior=n
        elif n < menor:
            menor=n
print('Foram digitados {} valores e a média entre eles é {}'.format(count,soma/count))
print('O maior valor foi:{} e o menor:{}'.format(maior,menor))

print(f'A soma vale {s}')