n = ((int(input('Digite um numero: '))),
     (int(input('Digite um numero: '))),
     (int(input('Digite um numero: '))),
     (int(input('Digite um numero: '))))
print(f'O valor 9 apareceu {n.count(9)} vezes') #count cálcula quantas vezes o valor escolhido apareceu na tupla
if 3 in n:
    print(f'O valor 3 apareceu {n.index(3)+1}º posição') #index mostra em qual índice da tupla está o valor solicitado
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram ', end='')
for i in n:
    if i % 2 == 0:
        print(i, end='')
