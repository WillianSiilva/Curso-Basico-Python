from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for i in n:
    print(f' {i} ', end='') #Para não quebrar linha, é só colocar ,end='' no fim.
print(f'\nO maior valor sorteado foi {max(n)}')#Para quebrar linha, é só colocar \n np inicio.
print(f'O menor valor sorteado for {min(n)}')


