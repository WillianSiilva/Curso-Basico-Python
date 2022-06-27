numero = int(input('\nDigite um número para ser mostada o seu fatorial - '))
for c in range(numero, 1, -1):
    print(c, end=' × ')
    numero *= c - 1

print('1 = {}'.format(numero))

