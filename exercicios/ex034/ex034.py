#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
n=float(input('Qual o salário do funcionario em reais?'))
if n>1250.00:
    n1=n*10/100
    print('O funcionario receberá 10% de aumento, ou seja R${:.2f} e passara a receber R${:.2f}'.format(n1,n+n1))
if n<=1250.00:
    n2=n*15/100
    print('O funcionario receberá 15% de aumento, ou seja R${:.2f} e passará a receber R${:.2f}'.format(n2,n+n2))
