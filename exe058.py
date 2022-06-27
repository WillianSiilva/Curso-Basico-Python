from random import randint # Função que escolhe um número dentro de um intervalo entre ()
pc = randint(0, 10)
cont = 1
print('Sou seu computador.... ')
print('''Acabei de pensar em um número entre 0 e 10 
Será que você consegue advinhar qual foi?''')
num = int(input('Qual é seu palpite? '))
while num != pc:
    if num < pc:
        print('Mais... Tente mais uma vez:')
        num = int(input('Qual é o seu palpite? '))
    elif num > pc:
        print('Menos... Tente mais uma vez:')
        num = int(input('Qual é o seu palpite? '))
    cont += 1
print(f'Acertou com {cont} tentativas. PARABÉNS!')