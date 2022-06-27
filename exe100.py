from random import randint
def sorteio(lista):
    for i in range (0, 5):
        num = randint(0, 10)
        lista.append(num)
    print(f'Somando os valores da lista:', end='')

def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {numeros}, temos {soma}')


numeros = list()
sorteio(numeros)
print(f'{numeros} PRONTO!')
somapar(numeros)

