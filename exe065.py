c = 'S'
soma = 0
cont = 0

while c == 'S':
    n = int(input('Digite um número: '))
    c = input('Quer continuar: [S/N]: ').upper()
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

media = soma / cont
print(f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')