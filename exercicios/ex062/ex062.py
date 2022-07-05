#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print('='*40)
print('Termos de uma progressão aritmetica')
print('='*40)
primeiro=int(input('Primeiro termo:'))
razao=int(input('Razão:'))
termo=primeiro
count=1
total=0
mais=10
while mais !=0:
    total=total+mais
    while count<=total:
        print('{}-'.format(termo),end=' ')
        termo = termo + razao
        count = count + 1
    print('PAUSA')
    mais=int(input('Quantos temos voce quer mostrar a mais?:'))
    if mais ==0:
        print('acabou')
print('Progressão finalizada com {} termos mostrados'.format(total))



