primeiro = int(input('Primeiro numero:'))
segundo = int(input('Segundo numero: '))
if primeiro > segundo:
    print(f'O primeiro valor é maior')
elif segundo > primeiro:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais!')
