#Lista 1
lista = [10, 20, 30] #Define váriavel lista
print(lista[0], " = Número referenciavel ao conteúdo 'Lista'")

# Lista 2
listaDois = [[], 1, ["Teste"]]  # Define a variável listaDois com três elementos: uma lista vazia, um número e uma lista com uma string
for item in listaDois:  # Itera sobre cada elemento da lista listaDois
    print(item, "Do tipo ", type(item))
    itemDois = listaDois[2]  # Define itemDois como o terceiro elemento de listaDois, que é ["Teste"]
    print(itemDois, "Do tipo ", type(itemDois))
    print("O conteúdo de 'itemDois' é: ", itemDois[0])
    for item in itemDois:
        print(listaDois[2][0])  # Imprime o primeiro elemento de itemDois (ou seja, "Teste")

#Matriz
matriz = [] #Define a lista
for i in range(100):
    linha = []
    for j in range(100):
        linha.append(j)
    matriz.append(linha)
    #Se colocar a partir desse espaço ele mostra o append se desenvolvendo por lista
    #print(matriz)

#Se colocar neste espaço, irá exibir em uma única linha, uma vez que está fora do loop
#print(matriz)

#Desta forma, ele será exibido um abaixo do outro
#for linha in matriz:
    #print(linha)

# MatrizInput
matrizInput = []
numberColumn = 3  # Número de colunas
numberLine = 3  # Número de linhas
print("----------")
print("MatrizInput")
print("Processo de preenchimento da matriz")
print("Atenção! Este processo levará {} passos.".format(numberLine * numberColumn))

for k in range(numberLine):
    linhaMatrizInput = []
    print("-" * 30, "Linha = ", k + 1)
    for l in range(numberColumn):
        inputTemporario = input(f"---> Diga o {l + 1}° item da {k + 1}° linha: ")
        linhaMatrizInput.append(inputTemporario)  #Adiciona o valor inserido pelo usuário à linha
    matrizInput.append(linhaMatrizInput)  #Adiciona a linha completa à matrizInput

print("")
print("Matriz Resultante:")
for linha in matrizInput:
    print(linha)  # Imprime cada linha da matrizInput
