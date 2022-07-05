n=float(input('Qual o salario de um funcionário? R$'))
novo=n+(n*15/100)
print('Um funcionario que recebia R${}, com 15% de aumento passou a receber {:.2f}'.format(n,novo))