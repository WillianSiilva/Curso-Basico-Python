lista = list()
cont = 0

while True:
    lista.append(int(input('Digite um valor: ')))
    r = input('Quer continuar? [S/N] ').upper().strip()[0]
    cont +=1
    if r in 'N':
        break
print(f'Você digitou {cont} elementos...')
lista.sort(reverse=True)
print(f'Os valores em ordem descrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
lista.sort(reverse=False)
print(lista)

