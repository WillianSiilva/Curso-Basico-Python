lista = list()
while True
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado....')
    else:
        print('Valor duplicado. Não vou adicionar...')
    c = input('Quer continuar? [S/N]: ').upper().strip()[0]
    if c in 'N':
        break
print(f'Você digitou os valores {lista}')
