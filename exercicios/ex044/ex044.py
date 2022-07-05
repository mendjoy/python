#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
valor=float(input('Qual o valor do produto?:'))
print('''Escolha a forma de pagamento:
[1]A vista dinheiro/cheque 
[2]A vista no cartão
[3]2x no cartão
[4]3x ou mais no cartão''')
opção=(int(input('Qual a sua opção?:')))
if opção==1:
    print('O valor a ser pago com desconto de 10% será de: R${:.2f}'.format(valor-(valor*10/100)))
elif opção==2:
    print('O valor a ser pago com 5% de desconto será de R${:.2f}'.format(valor-(valor*5/100)))
elif opção==3:
    print('O valor a ser pago em 2x será de R${:.2f} em cada parcela'.format(valor/2))
elif opção==4:
    parcelas=float(input('Quantas parcelas?'))
    n1=valor+(valor*20/100)
    n2=n1/parcelas
    print('O valor a ser pago em {}x com 20% de juros será de R${:.2f} em cada parcela'.format(parcelas,n2))
else:
    print('opção invalida, escolha novamente')