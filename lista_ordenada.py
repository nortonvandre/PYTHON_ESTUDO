lista = [1,4,2,7,3]
lista_ordenada = []

for num in lista: #percorre os numeros dentro da lista
    # if not lista_ordenada:
    #     lista_ordenada.append(num) adiciona o primeiro numero assim iniciando o loop
    for i in range(len(lista_ordenada)): # loop com range da lista ordenada
        if num > lista_ordenada[i]:
            lista_ordenada.insert(i,num)
            break
    else:
        lista_ordenada.append(num) #adiciona o primeiro numero assim iniciando o loop(pode-se usar um if para iniciar tambem)

 