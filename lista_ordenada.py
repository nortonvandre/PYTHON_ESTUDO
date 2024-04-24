# Lista original e lista ordenada manualmente
lista = [1, 4, 2, 7, 3]
lista_ordenada = []

for num in lista:  # Percorre os números dentro da lista
    # Se você quiser iniciar a lista com um 'if'
    # if not lista_ordenada:
    #     lista_ordenada.append(num)

    for i in range(len(lista_ordenada)):  # Loop com range da lista ordenada
        if num < lista_ordenada[i]:  # Comparativo de número(lista) com número(lista_ordenada)
            lista_ordenada.insert(i, num)  # Insere o número no índice no momento em que ele for maior que o número na lista ordenada
            break
    else:
        lista_ordenada.append(num)  # Adiciona o primeiro número assim iniciando o loop(pode se tambem usar um if)

print("Lista ordenada manualmente:", lista_ordenada)

# Lista inicial
lista = [1, 4, 2, 7, 3]

# Loop para percorrer cada elemento da lista
for i in range(len(lista)):
    # Loop interno para comparar o elemento atual com os elementos seguintes
    for j in range(i+1, len(lista)):
        # Se o elemento atual for menor que o próximo elemento, trocamos os elementos
        if lista[i] < lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

# Imprime a lista ordenada em ordem decrescente
print(lista)


# Lista ordenada usando o método sort()
lista2 = [4, 2, 7, 3, 9]
lista2.sort()  # .sort() modifica a lista de forma ordenada, podendo usar .sort(reverse=True)
print("Lista ordenada com sort():", lista2)

# Lista ordenada usando o método sorted()
lista3 = [2, 10, 3, 1, 8]
lista_ordenada3 = sorted(lista3)  # sorted() ordena a lista sem modificar a lista original, podendo usar sorted(lista3,reverse=True)
print("Lista ordenada com sorted():", lista_ordenada3)
