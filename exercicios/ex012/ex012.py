preço=float(input('Quanto custa o produto? R$'))
novo=preço-(preço*5/100)
print('O produto custava R${} e com 5% de desconto passou a custar R$ {}'.format(preço,novo))