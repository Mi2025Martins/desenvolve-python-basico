#leitura das dimensões do terreno
comprimento = int(input("Comprimento do terreno (em metros):"))
largura =int(input("Largura do terreno (em metros):"))
#Leitura do preço por metro quadrado
preco_m2 = float(input("Digite o preço do metro quadrado (em R$):"))
#cálculo da área
area = comprimento*largura
#Cálculo do valor total
valor_total=area*preco_m2
#Impressão do resultado final
print(f"O terreno possui {area}m2 e custa R${valor_total:,.2f}".replace(",","x").replace(".",",").replace("x","."))