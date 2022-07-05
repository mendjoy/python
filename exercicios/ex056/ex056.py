somaidade=0
medidade=0
maioridadehomem=0
nomemaisvelho=' '
totmulher20=0
for p in range (1,5):
    print('-'*10,c,'º','PESSOA','-'*10)
    nome=str(input('Nome:')).strip()
    idade=int(input('Idade:'))
    sexo=str(input('Sexo [F/M]:')).strip()
    somaidade=somaidade+idade
    if  p ==1 and sexo in 'Mm':
        maioridadehomem=idade
        nomemaisvelho=nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem=idade
        nomemaisvelho=nome
    if sexo in 'Ff' and idade <20:
        totmulher20+=1
medidade=somaidade/4
print('A média de idade do grupo é {}.'.format(medidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomemaisvelho))
print('Ao todo {} mulheres com menos de 20 anos.'.format(totmulher20))
