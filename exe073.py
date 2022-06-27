tabela = ('Corinthians', 'Santos', 'Avaí', 'América-MG','Bragantino', 'São Paulo', 'Atlético-MG', 'Botafogo', 'Internacional',
'Coritiba', 'Cuiabá', 'Athletico-PR','Palmeiras', 'Flamengo','Fluminense','Goiás','Ceará','Juventude','Atlético-GO','Fortaleza')
print('--'*30)
print(f'Lista de time: {tabela}')
print('--'*30)
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print('--'*30)
print(f'Os 4 últimos são: {tabela[16:]}')
print('--'*30)
print(sorted(tabela)) #A função sorted, coloca as coisas em ordem, neste caso em ordem alfabetica.
print('--'*30)
print(f' O Ceara está na {tabela.index("Ceará")+1}º posição')


