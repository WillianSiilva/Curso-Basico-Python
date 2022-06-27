M18 = m20 = homem = 0
while True:
    idade = int(input('Qual a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Qual o seu sexo [F/M]: ').upper().strip()[0]
    c = ' '
    while c not in 'SN':
        c = input('Quer continuar [S/N]: ').upper().strip() [0]

    if sexo == 'F' and idade < 20:
       m20 +=1
    if idade > 18:
        M18 += 1
    if sexo == 'M':
        homem += 1
    if c == 'N':
        break
print(f'O total de pessoas com mais de 18 anos é {M18}')
print(f'A quantidade homens cadastrados foi de {homem}')
print(f'A quantidade de mulheres com menos de 20 anos é {m20}')
