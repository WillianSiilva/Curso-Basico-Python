palavra = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
           'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for i in palavra:
    print(f'\nNa palavra {i} temos ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')

