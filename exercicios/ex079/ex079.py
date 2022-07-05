#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores=list()
n=0
while True:
    n=int(input('Digite um valor:'))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não vou adicionar!')
    resp=str(input('Quer continuar?[S/N]:')).strip().upper()[0]
    if resp not in 'SN':
        resp=str(input('Opção invalida. Quer continuar?[S/N]:'))
    elif resp in 'N':
        break
print('-'*30)
valores.sort()
print(f'Os valores digitados em ordem crescente foram: {valores}')

