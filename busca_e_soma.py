def search(lista, numero):
    """
    Esta função procura dois números na lista cuja soma seja igual a um número dado.

    Parâmetros:
    - lista: lista de números inteiros
    - numero: número inteiro para o qual a soma dos dois números deve ser igual

    Retorna:
    - Tupla com os dois números cuja soma é igual a 'numero', ou None se nenhum par for encontrado
    """

    # Percorre a lista para encontrar os números
    for n in range(len(lista)):
        for i in range(n+1, len(lista)):
            # Verifica se a soma de n e i é igual a numero
            if lista[n] + lista[i] == numero:
                return lista[n], lista[i]  # Retorna os números encontrados

    # Se nenhum par for encontrado, retorna None
    return None

# Lista de números e número alvo
lista = [2, 6, 3, 9, 4]
numero = 11

# Chama a função e imprime os resultados
resultado = search(lista, numero)
if resultado:
    print(f"Os números {resultado[0]} e {resultado[1]} têm a soma igual a {numero}.")
else:
    print("Nenhum par de números encontrado.")




def search(lista, numero):
    """
    Esta função procura dois números na lista cuja soma seja igual a um número dado.

    Parâmetros:
    - lista: lista de números inteiros
    - numero: número inteiro para o qual a soma dos dois números deve ser igual

    Retorna:
    - Tupla com os dois números cuja soma é igual a 'numero', ou None se nenhum par for encontrado
    """

    # Conjunto para armazenar os números já vistos
    numeros_vistos = set()

    for n in lista:
        complemento = numero - n

        # Verifica se o complemento já foi visto
        if complemento in numeros_vistos:
            return n, complemento

        # Adiciona o número atual ao conjunto de números vistos
        numeros_vistos.add(n)

    # Se nenhum par for encontrado, retorna None
    return None

# Lista de números e número alvo
lista = [2, 6, 3, 9, 4]
numero = 11

# Chama a função e imprime os resultados
resultado = search(lista, numero)
if resultado:
    print(f"Os números {resultado[0]} e {resultado[1]} têm a soma igual a {numero}.")
else:
    print("Nenhum par de números encontrado.")
