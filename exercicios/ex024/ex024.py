#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

n=str(input('Digite o nome de uma cidade:')).strip()
print(n[:5].upper()== 'SANTO')
