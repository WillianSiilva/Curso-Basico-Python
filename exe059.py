from time import sleep

v1 = int(input('Digite um número: '))
v2 = int(input('Digite outro número: '))

opcao = 0

while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')

    opcao = int(input('Qual é a sua opção: '))

    if opcao == 1:
        soma = v1 + v2
        print(f'O resultado de {v1} + {v2} é {soma}')
    elif opcao == 2:
        multiplicacao = v1 * v2
        print(f'O resultado de {v1} x {v2} é {multiplicacao}')
    elif opcao == 3:
        if v1 > v2:
            print(f'Entre {v1} e {v2} o maior valor é {v1}')
        else:
            print(f'Entre {v1} e {v2} o maior valor é {v2}')
    elif opcao == 4:
        v1 = int(input('Digite um número: '))
        v2 = int(input('Digite outro número: '))
    elif opcao == 5:
        print('Finalizando...')
    elif opcao > 5:
        print('Opção invalida. Tente novamente')
    sleep(1)
    print('-=-' * 20)

print('Fim do Programa')


