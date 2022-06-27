from random import randint

cont = 0

while True:
    pc = randint(0, 10)
    n = int(input('Diga um valor: '))
    s = input('[P/I]: ').upper().strip()[0]
    soma = n + pc
    if soma % 2 != 0:
        l = 'IMPAR'
    else:
        l = 'PAR'
    if l[0] != s:
        print(f'Você jogou {n} e o computador {pc}. Total de {soma}. DEU {l}')
        print('-' * 30)
        break
    print(f'Você jogou {n} e o computador {pc}. Total de {soma}. DEU {l}')
    print('VOCÊ GANHOU!')
    print('Vamos jogar novamente...')
    cont +=1
print('Você perdeu!')
print(f'GAME OVER. Você ganhou {cont} vezes')
