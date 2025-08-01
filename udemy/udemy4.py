frase = 'p python é uma linguagem de programação' \
         'multiparadigma ' \
         'python foi criado por Guido van Rossum .'

i = 0
while i < len(frase):
    letra_atual = frase[i]
    quantas_letras = frase.count(letra_atual)
    i += 1

    print(f'A letra "{letra_atual}" aparece {quantas_letras} vezes.')
    