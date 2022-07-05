#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
valores=[]
cont=0
cont5=0
while True:
    cont=cont+1
    valores.append(input('Digite um valor:'))
    resp = str(input('Quer continuar?[S/N]:')).upper().strip()[0]
    if resp not in 'SN':
        resp = str(input('Resposta invalida. Quer continuar?[S/N]:')).upper().strip()[0]
    if valores== 5:
        cont5=cont5+1
    if resp == 'N':
        break
print('-='*20)
valores.sort(reverse=True)
print(f'voce digitou {len(valores)} números.')
print(f'Os valores digitados de forma decrescente são: {valores}')
    if 5 in valores:
        print('O valor 5 está na lista')
    else:
        print('O valor 5 não está na lista')
