#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

time=('CORINTHIANS', 'PALMEIRAS','SÃO PAULO', 'ATLÉTICO-MG','BOTAFOGO','SANTOS','FLUMINENSE','CORITIBA','AMÉRICA-MG',
     'AVAI','INTERNACIONAL','ATHLETICO-PR','BRAGANTINO',
      'FLAMENGO','GOIAS','CUIÁBA', 'ATLÉTICO-GO','JUVENTUDE','CEARÁ SC','FORTALZEA')
print('=-'*30)
print(f'Lista de times do Brasileirão 2022:{time}')
print('=-'*30)
print(f'Os 5 primeiros colocados são:{time[0:5]}')
print('=-'*30)
print(f'Os ultimos 4 colocados são: {time[-4:]}')
print('=-'*30)
print(f'Os times em ordem alfabetica:{sorted(time)}')
print('=-'*30)
print(f'O time Juventude está na posição: {time.index("JUVENTUDE")+1}')
