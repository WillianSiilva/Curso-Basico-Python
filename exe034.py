salario = float(input('Qual é o salário? R$'))
if salario > 1250:
    aumento = (salario * 0.10) + salario
else:
    aumento = (salario * 0.15) + salario
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora')