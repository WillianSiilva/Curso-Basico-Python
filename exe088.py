from random import randint

cont = 0
lista = list()
tudo = list()

n = int(input('Quantos jogos você quer que eu sorteie?: '))

for i in range(1, n+1):
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >= 6:
            break
    tudo.append(lista[:])
    print(tudo[i])

