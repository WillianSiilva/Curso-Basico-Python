listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90) # Neste caso, pela forma que foi digitado, o item está nos numeros pares e os preços nos impares.
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')# Neste caso foi utilizado o simbolo ^para centralizar o texto dentro do espaço determinado (40)
print('-'*40)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')#O 30 é a quantidade de espaços que será ocupado, e o ponto foi para prencher esse espaços
    else:
        print(f'R${listagem[pos]:>6.2f}')#Para alinhar a direita, usamos esse sinal: > e o 6 é a quantidade de casa após o $ e o .2f e a quantidade casas decimais.
print('-'*40)