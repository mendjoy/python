km=float(input('Quantos Km você percorreu com o carro?'))
d=float(input('Quantos dias você ficou com o carro?'))
t=(km*0.15)+(d*60)
print('Você deve pagar R${}'.format(t))