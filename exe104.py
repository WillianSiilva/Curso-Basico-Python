def ficha(nome = '<desconhecido>', gol = 0):
    print(f'O jogador {nome} fez {gol} gols no campeonato')


nome = input("Nome do jogador: ")
g = input("Quantidade de gols: ")
if g.isnumeric():
    g = int(g)
else:
    g = 0

if nome.strip() == '':
    ficha(gol=g)
else:
    ficha()



