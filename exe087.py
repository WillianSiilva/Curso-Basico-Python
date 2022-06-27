matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = soma3 = soma2 = maior = 0

for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input(f'Digite os valores da matriz [{i}, {c}]: '))
        if matriz [i][c] % 2 == 0:
            somapar += matriz[i][c] # Para calcular o valor dos números pares.

for i in range(0, 3):
    for c in range(0, 3):
        print(f' [{matriz[i][c]:^5}]', end=' ') # Para centralizar o valor, usar ^, e para determinar a quant de casa, use o 5.
    print() # Imprimindo o resultado da matriz utilizando for

print(f'A soma de todos os valores pares é: {somapar}')

for i in range(0, 3):
    soma3 += matriz[i][2] # Estrutura for para calcular o valor da 3º Coluna
print(f'A soma dos valores da terceira coluna é: {soma3}')

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c] # Estrutura for para calcular qual número é maior na segunda coluna,
        # como era necessário descobrir apenas uma linha, utilizei um for só

print(f'O maior valor da 2º linha é {maior}')
