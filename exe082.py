lista = list()
impares = list()
pares = list()
while True:
    n = (int(input('Digite um valor: ')))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r = input('Quer continuar: [S/N]: ')
    if r in 'Nn':
        break
print(f'A lista completa é: {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
