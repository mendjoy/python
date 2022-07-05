#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#eu programa deverá realizar a operação solicitada em cada caso.

n1=int(input('Digite o primero valor:'))
n2=int(input('Digite o segundo valor:'))
opção=0
while opção != 5:
    print('''.........Escolha uma opção abaixo............. 
    [1] somar
    [2] multiplicar
    [3] maior 
    [4] novos números
    [5] sair do programa''')
    opção=int(input('Qual a sua escolha?:'))
    if opção ==1:
        soma=n1+n2
        print('A soma entre {} e {} é {}'.format(n1,n2,soma))
        print('**' * 40)
    elif opção ==2:
        mult=n1*n2
        print('A multiplicação entre {} e {} é {}'.format(n1,n2,mult))
        print('**' * 40)
    elif opção ==3:
        if n1>n2:
            maior=n1
        else:
            maior=n2
        print('Entre os números {} e {} o maior é {}'.format(n1, n2, maior))
        print('**' * 40)
    elif opção ==4:
        print('Informe os números novamente:')
        n1=int(input('Primeiro valor:'))
        n2=int(input('Segundo valor:'))
        print('**' * 40)
    elif opção ==5:
        print('.......FIM......')
    else:
        print('opção invalida, tente novamente')
        print('**' * 40)


