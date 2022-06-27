pessoas = dict()
mulheres = dict()
dados = list()
soma = 0

while True:
    pessoas.clear()
    pessoas['Nome'] = input('Nome: ')
    pessoas['Sexo'] = input('Sexo [M/F]: ')
    if pessoas['Sexo'] not in 'MmFf':
        print('Por favor, digite apenas M ou F.')
        pessoas['Sexo'] = input('Sexo [M/F]: ')
    pessoas['Idade'] = int(input('Idade: '))
    soma +=pessoas['Idade']
    dados.append(pessoas.copy())
    cond = input('Quer continuar [S/N]? ')
    if cond not in 'NnSs':
        print('Por favor, digitar apenas S ou N.')
        cond = input('Quer continuar [S/N]? ')
    if cond in 'Nn':
        break
media = soma / len(dados)
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for i in dados:
    if i['Sexo'] in 'Ff':
        print(f' {i["Nome"]}', end=' ')
print()
print('D) Lista das pessoas que estão acima da média: ', end='')
for i in dados:
    if i['Idade'] > media:
        print(f'{i["Nome"]}', end=' ')



