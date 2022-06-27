dados = list()
alunos = list()

while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: ' ))
    dados.append(nome)
    dados.append(n1)
    dados.append(n2)
    alunos.append(dados[:])
    dados.clear()
    cond = input('Quer continuar? [S/N}: ')
    if cond in 'Nn':
        break
for pos in range(0, len(alunos)):
    print(pos, alunos[pos, pos])