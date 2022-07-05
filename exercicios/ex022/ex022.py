#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome=str(input('Digite o seu nome completo:')).strip()
print('Analisando seu nome...')
print('O seu nome com todas as letras maiusculas é {}'.format(nome.upper()))
print('O seu nome com todas as letras minusculas é {}'.format(nome.lower()))
print('O seu nome completo possui {} letras'.format(len(nome)-nome.count(' ')))
print('O seu primeiro nome possui {} letras'.format(len(nome[:5])))
print('O seu primeiro nome possui {} letras'.format(nome.find(' ')))
separa=nome.split()
print('O seu primeiro nome possui {} letras'.format(len(separa[0])))
