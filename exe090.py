dados = dict()
dados['nome'] = input('nome: ')
dados['média'] = float(input((f'média do {dados["nome"]}: ')))
if dados['média'] >= 7:
    dados['situação'] = 'Aprovado'
elif 5 <= dados['média'] < 7:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado'
print('-='*30)
for k,v in dados.items():
    print(f'   -{k} é igual a {v}')



