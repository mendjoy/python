#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
n=str(input('Digite seu nome completo:')).strip()
n1=n.split()
print('O seu primeiro nome é:{}'.format(n1[0]))
print('O seu ultimo nome é:{}'.format(n1[len(n1)-1]))