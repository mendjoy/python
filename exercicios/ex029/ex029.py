#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
v=int(input('Qual a velocidade atual do carro?'))
if v>80:
    print('Você esta acima do limite de velocidade!')
    v1=v-80
    print('Você será multado em R${:.2f}'.format(v1*7.00))
else:
    print('Dirija com segurança! tenha um bom dia!')
