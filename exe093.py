dados = dict()
gols = list()

dados['Nome'] = input('Nome do Jogador: ')
tot = int(input('Quantas partidas: '))
for i in range(0, tot):
    gol = int(input(f'  Quantos gols ele fez na partida {i+1}? '))
    gols.append(gol)
dados['gols'] = gols[:]
dados['total'] = sum(gols)
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados["Nome"]} jogou {tot} partidas')
for i in range(0, tot):
    print(f'    => Na partida {i+1}, fez {dados["gols"][i]} gols')
print(f'Foi um toal de {dados["total"]} gols')
