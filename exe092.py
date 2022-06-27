from datetime import datetime #Biblioteca usada para importar ano atual
dados = dict()
dados['Nome'] = input('Nome: ')
dados['Idade'] = (datetime.now().year - int(input('Ano de nascimento: '))) #Como usar o ano atual
dados['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Anocontr'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (dados['Anocontr'] + dados['Idade'] + 35)-datetime.now().year
print('-=' * 30)
for k, v in dados.items():
    print(f'    -{k} tem o valor de {v}')

