def leitaInt(msg):
    ok = False
    Valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leitaInt('Digite um número: ')
print(f'Você digitou o número {n}')