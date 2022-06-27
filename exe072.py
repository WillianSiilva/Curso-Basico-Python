numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
          'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' )

n = int(input('Digite um numero: '))

while n not in range(0,21):
    n = int(input('Tente novamente. Digite um número: '))
print(f'Você digitou o número {numero[n]}')
