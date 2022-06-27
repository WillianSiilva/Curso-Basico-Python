import datetime
anoatual = datetime.date.today().year
c1 = 0
c2 = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}º pessoa nasceu? '))
    idade = anoatual - ano
    if idade >= 18:
        c1 += 1
    else:
        c2 += 1
print()
print(f'Ao todo tivemos {c1} pessoas maiores de idade')
print(f'E também tivemos {c2} pessoas menores de idade')



