#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa=float(input('Qual o valor da casa?:'))
comp=float(input('Qual o salario do comprador?'))
fin=float(input('Quantos anos de financiamento?'))
n1=casa/(fin*12)
print('Para pagar uma casa de R${} em {} anos, a prestação será de R${:.2f}'.format(casa,fin,n1))
n2=(comp*30/100)
if n1>n2:
    print('Emprestimo NEGADO')
elif n1<n2:
    print('Emprestimo APROVADO')

