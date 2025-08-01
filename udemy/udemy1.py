qtd_linhas = 5
qtd_colunas = 5

linha = 1 
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f"({linha}, {coluna})", end=" ")
        coluna += 1
    print()  # Nova linha após cada linha completa
    linha += 1