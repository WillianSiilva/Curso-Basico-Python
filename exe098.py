from time import sleep
def contagem(a, b, c):
    print('-=' * 30)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    for i in range(a, b+1, c):
        print(i, end=' ')
        sleep(0.5)
    print('FIM!')

contagem(1, 10, 1)
contagem(10, 0, -2)
print('-='*30)
print('Agora é a sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
print('-='*30)
print(f'Contagem de {a} até {b} de {c} em {c}')
contagem(a, b, c)




