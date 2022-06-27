frase = input('Digite uma frase: ').strip().upper() # Com o strip eliminamos os espaços do inicio e fim
palavras = frase.split() # com split ele separa a frase em palavras, eliminando os espaços da frase (Coleção)
junto = ''.join(palavras) # Juntar todas as palavras sem espaços ou o que tiver dentro das aspas
inverso = ''
for letra in range(len(junto) -1, -1, -1): # a f len() retorna a quantidade da lista
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if junto != inverso:
    print(' Essa frase não é palíndromo')
else:
    print('Essa frase é um palíndromo')
