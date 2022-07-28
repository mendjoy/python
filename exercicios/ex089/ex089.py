ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar [S/N]?: '))
    if resposta in 'Nn':
        break
print('-'*40)
print(f'{"Nº":<4} {"Nome:":<10}{"Média:":>8}')
print('-'*40)
for i, a in enumerate (ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 40)
    opc = (int(input('Mostrar notas de qual aluno? (999 interrompe): ')))
    if opc == 999:
        print('...Finalizando...')
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são: {ficha[opc][1]}')

print('...Até mais!...')


