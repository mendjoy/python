'''Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem'''
import random
n1=str(input('Digite o nome do primeiro aluno:'))
n2=str(input('Digite o nome do segundo aluno:'))
n3=str(input('Digite o nome do terceiro aluno:'))
n4=str(input('Digite o nome do quarto aluno:'dcdc))
lista=[n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem para a apresentação dos trabalhos é: {}'.format(lista))



