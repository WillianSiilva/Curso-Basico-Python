def voto(num=0):
    from _datetime import datetime  # -> Imortar a biblioteca dentro da função economiza espaço na memória.
    idade = datetime.now().year - ano
    if idade < 16:
        return f'Com {idade} anos: {"Não vota"}'
    elif 16 < idade < 18:
        return f'Com {idade} anos: {"Voto opicional"}'
    elif 18 < idade < 65:
        return f'Com {idade} anos: {"Voto obrigatório"}'
    else:
        return f'Com {idade} anos: {"Voto opicional"}'


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
