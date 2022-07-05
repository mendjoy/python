#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato
print('-'*40)
print('...LIQUIDAÇÃO...')
print('-'*40)
total=cont=caro=barato=menor=0
while True:
    produto=str(input('Nome do produto:'))
    preço=float(input('Preço:'))
    cont=cont+1
    total=total+preço
    resp=' '
    if preço >1000:
        caro=caro+1
    if cont ==1:
        menor=preço
        barato=produto
    else:
        if preço < barato:
            menor=preço
            barato=produto
    while resp not in 'SN':
        resp=str(input('Quer continuar? [S/N]:')).upper().strip()[0]
    if resp in 'N':
        break
print(f'O total da compra foi de R${total:.2f}.')
print(f'Temos{caro:.0f} produtos custando mais de R$1000.00.')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}.')


