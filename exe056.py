si = 0
tp = 0
maior = 0
tm = 0
nomei = ''
for c in range(1, 5):
    print('-'* 8, f'{c}ºPESSOA','-'* 8)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    si += idade
    tp += 1
    if c == 1:
        nomei = nome
        maior = idade
    elif idade > maior and nome != nomei and sexo == 'M':
        maior = idade
        nomei = nome
    if sexo == 'F' and idade < 20:
        tm += 1
media = si / tp
print()
print(f'A média de idade do grupo é de {media} anos')
print(f'O Homem mais velho tem {maior} anos e se chama {nomei}')
print(f'Ao todo são {tm} mulheres com menos de 20 anos')