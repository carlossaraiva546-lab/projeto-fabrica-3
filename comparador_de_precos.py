produto = input("nome do produto: ")
nome_mercado1 = input("nome do primeiro mercado: ")
preco_produto1 = float(input("preço do primeiro produto: "))

nome_mercado2 = input("nome do segundo mercado: ")
preco_produto2 = float(input("preço do segundo mercado: "))

nome_mercado3 = input("nome do terceiro mercado: ")
preco_produto3 = float(input("preço do terceiro produto: "))

if preco_produto1 < preco_produto2 and preco_produto1 < preco_produto3:
    print(f"{produto}, {nome_mercado1}, {preco_produto1}")

elif preco_produto2 < preco_produto1 and preco_produto2 < preco_produto3:
    print(f"{produto},{nome_mercado2},{preco_produto2}")

else:
    print(f"{produto},{nome_mercado3},{preco_produto3}")