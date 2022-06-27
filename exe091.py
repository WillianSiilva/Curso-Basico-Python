from random import randint
from operator import itemgetter

jogo = {'jogador1' : randint(1, 6),
        'jogador2' : randint(1, 6),
        'jogador3' : randint(1, 6),
        'jogador4' : randint(1, 6)}
# Essa parte do código gerará um dicinário com os números selecionados aleatoriamente através do randint()

ranking = list() #Para organizar o ranking, ele criou uma lista.
print('Valores sorteados')

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #Ele usou o mod itemgetter para poder usar as duas chaves na solução
print('-='*30)
print('  == RANKING DOS JOGADORES ==')
for v, i in enumerate(ranking):
    print(f'  {v+1}º lugar: {i[0]} com {i[1]}. ')