#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

#n=(int(input('Digite um numero entre 0 e 9999:')))
#n=str(n)
#print('Analisando o numero {}...'.format(n))
#print('Unidade:{}'.format(n[3]))
#print('Dezena:{}'.format(n[2]))
#print('Centena:{}'.format(n[1]))
#print('Milhar:{}'.format(n[0]))

n=(int(input('Digite um numero entre 0 e 9999:')))
print('Analisando o numero {}...'.format(n))
u=n//1%10
d=n//10%10
c=n//100%10
m=n//1000%10
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar:{}'.format(m))


