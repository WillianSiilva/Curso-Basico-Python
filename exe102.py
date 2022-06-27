def fatorial(n, show=False):
    """
    ->>> Calcula o fatorial de um número:
    :param n: O número a ser calculado
    :param show: (Opicional) Mostrar ou não a conta
    :return: O valor do Fatorial de umnúmero n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f'{f}'


n=int(input('Qual o valor: '))
print(fatorial(n, True))
help(fatorial)