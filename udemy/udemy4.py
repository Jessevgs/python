
frase = 'O rato roeu a roupa do rei de Roma'

i = 0
while i < len(frase):
    letra_atual = frase[i]
    quantas_letras = frase.count(letra_atual)
    i += 1

    print(f'A letra "{letra_atual}" aparece {quantas_letras} vezes.')
    