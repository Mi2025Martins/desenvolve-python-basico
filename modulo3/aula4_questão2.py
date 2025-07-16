#Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários. 
#Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5. 
#O programa deve imprimir uma mensagem correspondente à classificação do filme:
#Se a avaliação for 5, imprima "Excelente!"
#Se a avaliação for 4, imprima "Muito Bom!"
#Se a avaliação for 3, imprima "Bom!"
#Se a avaliação for 2, imprima "Regular."
#Se a avaliação for 1, imprima "Ruim."

# Entrada do usuário
nota_avaliacao = int(input("Avalie o filme de 1 a 5, sendo 1 ruim, 2 regular, 3 bom, 4 muito bom e 5 excelente: "))

# Verificação da nota e exibição da avaliação
if nota_avaliacao == 5:
    print("Você avaliou o filme como: Excelente")
elif nota_avaliacao == 4:
    print("Você avaliou o filme como: Muito Bom")
elif nota_avaliacao == 3:
    print("Você avaliou o filme como: Bom")
elif nota_avaliacao == 2:
    print("Você avaliou o filme como: Regular")
elif nota_avaliacao == 1:
    print("Você avaliou o filme como: Ruim")
else:
    print("Nota inválida! Por favor, digite um número de 1 a 5.")