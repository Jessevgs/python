# primeiro codigo

numero = (input("Digite um numero: "))

if numero == float(numero):
    print("O numero nao é inteiro")


    
if numero % 2 == 0:
    print("O numero é par")
else:
    print("O numero é ímpar")



Nome = input("Digite seu nome: ")
if len(Nome) <= 4:
    print("Seu nome é muito curto")
elif len(Nome) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")



entrada = (input("Digite a hora: "))
try:
    hora = int(entrada)
    if hora < 0 and hora <= 11:
        print("Bom dia")
    elif hora >= 12 and hora <= 18:
        print("Boa tarde")
    elif hora >= 18 and hora <= 24:
        print("Boa noite")
    raise ValueError("Hora inválida")

except ValueError:
    print("por favor, digite uma hora válida entre 0 e 24")
    
