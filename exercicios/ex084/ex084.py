#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
temp=[]
princ=[]
maior=menor=0
while True:
    temp.append(str(input('Nome:')))
    temp.append(float(input('Peso:')))
    if len(princ) ==0:
        maior=menor=temp[1]
    else:
        if temp[1] > maior:
            maior=temp[1]
        if temp[1] < menor:
            menor=temp[1]
    princ.append(temp[:])
    temp.clear()
    resp=str(input('Quer continuar?[S/N]')).upper().strip()[0]
    if resp not in 'SN':
        resp = str(input('Opção invalida, digite novamente. Quer continuar?[S/N]')).upper().strip()[0]
    if resp in 'N':
        break
print('-='*30)
print(f'Os dados foram: {princ}.')
print(f'Ao todo foram cadastradas {len(princ)} pessoas.')
for p in princ:
    if p[1] ==



