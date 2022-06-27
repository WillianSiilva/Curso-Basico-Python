valorcasa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual é o seu salário? R$ '))
anos = int(input('Em quantos anos você vai pagar a casa? '))
prestacao = valorcasa / (anos *12)
condicao = salario * 0.3
print(f'Para comprar uma casa de {valorcasa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}!')
if prestacao <= condicao:
    print('PARABENS! Você acaba de comprar a sua casa!')
else:
    print('Emprestimo negado!')
    