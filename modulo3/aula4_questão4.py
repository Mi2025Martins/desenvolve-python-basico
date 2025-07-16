# Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. 
# Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo 
# com as seguintes regras:
#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg


#Entrada
distancia = int(input("Distancia da entrega (em quilometros):"))
peso =int(input("Peso do pacote (em quilogramas):"))

# Cálculo do valor por kg com base na distância
if distancia <= 100:
    preco_por_kg = 1.00
elif distancia <= 300:
    preco_por_kg = 1.50
else:
    preco_por_kg = 2.00

# Cálculo do frete básico
valor_frete = peso * preco_por_kg

# Taxa adicional para pacotes com peso acima de 10 kg
if peso > 10:
    valor_frete += 10.00

# Resultado
print(f"Valor do frete: R${valor_frete:.2f}")