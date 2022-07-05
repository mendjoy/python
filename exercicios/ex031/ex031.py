#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
d=int(input('Qual a distancia da sua viagem em Km?'))
if d<=200:
    print('A sua passagem vai custar R${:.2f}'.format(0.5*d))
else:
    print('A sua passagem vai custar R${:.2f}'.format(0.45*d))
