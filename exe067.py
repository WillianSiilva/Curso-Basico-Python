while True:
    n = int(input('Digite qual valor da tabuada: '))
    print('--'*30)
    if n < 0:
        break
    for i in range (1,11):
        print(f'{n} x {i} = {n*i}')
    print('--' * 30)
print('O programa da tabuada foi encerrado.')

