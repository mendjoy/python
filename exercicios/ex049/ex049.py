#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n=(int(input('Digite um número para ver a sua tabuada:')))
for c in range(0,11):
    n1=n*c
    print('{} x {} ={}'.format(n,c,n1))