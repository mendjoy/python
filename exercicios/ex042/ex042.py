#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes
n1=float(input('Digite o comprimento de uma reta:'))
n2=float(input('Digite o comprimento de outra reta:'))
n3=float(input('Digite o comprimento de mais uma reta:'))
if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    print('Os seguimentos {}, {}, {}, podem formar um triangulo:'.format(n1,n2,n3),end=' ')
    if n1==n2==n3:
        print('EQUILATERO')
    if n1!=n2!=n3!=n1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('os seguimentos {}, {}, {}, não podem formar um triangulo')
