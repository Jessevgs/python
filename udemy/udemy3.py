
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print("Contagem interrompida no 6.")
        continue

    if  contador >= 10 and contador <= 27:
        print('nao vou mostrar o ', contador)
        continue

    print("Contador:", contador)

    if contador == 40:
        break
  
    
print("Fim.")
