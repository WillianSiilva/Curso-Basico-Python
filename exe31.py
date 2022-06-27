km = float(input('Qual a distância da viagem em Km?: '))
if km <= 200:
    valor1 = km * 0.50
    print(f'Você está preste a começar uma viagem de {km} Km.')
    print(f'E o preço da sua passagem é de R${valor1:.2f}')
else:
    valor1 = km * 0.45
    print(f'Você está preste a começar uma viagem de {km} Km.')
    print(f'E o preço da sua passagem é de R${valor1:.2f}')