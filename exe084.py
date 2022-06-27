dados = list()
pessoas = list()
cont = maior = menor = 0

while True:
    dados.append(input('Qual o seu nome: '))
    dados.append(float(input('Qual é o seu peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] >= maior:
            maior = dados[1]
        if dados[1] <= menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    cont+=1
    r = input('Quer continuar? [S/N] ')
    if r in 'Nn':
        break
print(f'Foram cadastradas o total de {cont} pessoas')
print(f'O maior pesso foi de {maior:.2f}Kg ', end='')
for v in pessoas:
    if v[1] == maior:
        print(f'{v[0]}...', end='')
print()
print(f'O menor peso foi de {menor:.2f}Kg ', end='')
for v in pessoas:
    if v[1] == menor:
        print(f'{v[0]}...', end='')
print()
