from random import randint
from time import sleep
pc = randint(0, 5)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if num == pc:
    print(f'PARABÉNS! Você conseguiu me vencer')
else:
    print(f'GANHEI! Eu pensei no número {pc} e não no {num}')
