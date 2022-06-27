dados = dict()
gols = list()
jogadores = list()
while True:
    dados.clear()
    gols.clear()
    dados['Nome'] = input('Nome do Jogador: ')
    tot = int(input('Quantas partidas: '))
    for i in range(0, tot):
        gol = int(input(f'  Quantos gols ele fez na partida {i+1}? '))
        gols.append(gol)
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    jogadores.append(dados.copy())
    cond = input('Quer continuar [S/N]? ')
    if cond in 'Nn':
        break
print('-='*30)
print('cod', end='')
for i in dados.keys():
    print(f'{i:<10}', end='')
print()
print('-'*30)
for k,v in enumerate(jogadores):
    print(f'{k:>0} ', end='')
    for d in v.values():
        print(f'{str(d):>10}', end='')
    print()