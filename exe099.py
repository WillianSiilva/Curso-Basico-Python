def maior(* num):
    cont = 0
    ma = 0
    print('\nAnalisando os valores passados')
    for valor in num:
        print(f'{valor}', end=' ')
        cont +=1
        if cont == 0:
            ma = valor
        else:
            if valor > ma:
                ma = valor
    print(f'Formam passados {cont} valores ao todo.')
    print(f'O maior valor informado foi {ma}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

