num = [[], []]

for i in range(1,8):
    n = (int(input(f'Digite o {i}º número: ')))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print(f'Todos os valores {num}')
num[0].sort() # Se não separar pos listas, ele alinha tudo e o resultado sai errado
num[1].sort()
print(f'Os números pares são {num[0]}')
print(f'Os números impares são {num[1]}')