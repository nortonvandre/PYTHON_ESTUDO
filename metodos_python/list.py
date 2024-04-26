# Definindo uma lista
lista = [1, 2, 3, 4, 5]

# Funções embutidas
print("Funções embutidas:")
print("list():", list())  # Retorna uma lista vazia
print("len():", len(lista))  # Retorna o número de elementos na lista
print("max():", max(lista))  # Retorna o maior elemento da lista
print("min():", min(lista))  # Retorna o menor elemento da lista
print("sum():", sum(lista))  # Retorna a soma dos elementos da lista

# Métodos de objeto
print("\nMétodos de objeto:")
print("append():", lista.append(6))  # Adiciona um elemento ao final da lista
print("clear():", lista.clear())  # Remove todos os elementos da lista
print("copy():", lista.copy())  # Retorna uma cópia da lista
print("count():", lista.count(3))  # Retorna o número de ocorrências de um elemento na lista
print("extend():", lista.extend([7, 8, 9]))  # Adiciona os elementos de uma lista ao final da lista
print("index():", lista.index(5))  # Retorna o índice do primeiro elemento com o valor especificado
print("insert():", lista.insert(2, 10))  # Insere um elemento em uma posição específica
print("pop():", lista.pop())  # Remove e retorna o último elemento da lista
print("remove():", lista.remove(4))  # Remove o primeiro elemento com o valor especificado
print("reverse():", lista.reverse())  # Inverte a ordem dos elementos na lista
print("sort():", lista.sort())  # Ordena os elementos da lista em ordem crescente

# Manipulação de lista
print("\nManipulação de lista:")
# Adicionando elementos à lista
lista.append(6)  # Adiciona 6 ao final da lista
print("Após adicionar 6:", lista)

# Removendo elementos da lista
lista.remove(3)  # Remove o primeiro elemento com valor 3
print("Após remover 3:", lista)

# Fatiando a lista
sublista = lista[1:4]  # Obtém uma sublista dos elementos de índice 1 a 3 (exclusivo)
print("Sublista de índice 1 a 3:", sublista)

# Modificando elementos da lista
lista[0] = 10  # Modifica o primeiro elemento para 10
print("Após modificar o primeiro elemento para 10:", lista)

# Acessando elementos da lista por índice
print("O terceiro elemento da lista é:", lista[2])  # Acessa o terceiro elemento da lista

# Acessando elementos da lista por índice negativo (a partir do final)
print("O último elemento da lista é:", lista[-1])  # Acessa o último elemento da lista

# Invertendo a ordem dos elementos na lista
lista.reverse()
print("Após inverter a ordem dos elementos:", lista)

# Ordenando os elementos da lista em ordem crescente
lista.sort()
print("Após ordenar os elementos em ordem crescente:", lista)

# Adicionando diferentes tipos de dados em uma lista
lista_com_diferentes_tipos = [1, 2.5, "três", True, [4, 5, 6]]
print("\nLista com diferentes tipos de dados:", lista_com_diferentes_tipos)

# Iterando sobre uma lista usando loops
print("\nIterando sobre a lista usando loops:")
for item in lista_com_diferentes_tipos:
    print(item)

# Compreensão de lista
print("\nCompreensão de lista:")
nova_lista = [x * 2 for x in lista]
print("Nova lista dobrando os elementos:", nova_lista)

# Funções de ordem superior
print("\nFunções de ordem superior:")

# Utilizando a função map para calcular o quadrado de cada elemento da lista
quadrados = list(map(lambda x: x**2, lista))
print("Quadrados dos elementos da lista:", quadrados)

# Utilizando a função filter para filtrar os números pares da lista
pares = list(filter(lambda x: x % 2 == 0, lista))
print("Números pares da lista:", pares)

# Utilizando a função reduce para calcular a soma dos elementos da lista
from functools import reduce
soma = reduce(lambda x, y: x + y, lista)
print("Soma dos elementos da lista:", soma)

# Operações de conjunto com listas
print("\nOperações de conjunto com listas:")

# Calculando a união de duas listas usando operações de conjunto
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
print("União:", list(set(lista1) | set(lista2)))

# Calculando a interseção de duas listas usando operações de conjunto
print("Interseção:", list(set(lista1) & set(lista2)))

# Calculando a diferença entre duas listas usando operações de conjunto
print("Diferença:", list(set(lista1) - set(lista2)))

# Ordenação personalizada
print("\nOrdenação personalizada:")

# Ordenando uma lista de nomes em ordem crescente de comprimento
nomes = ["Ana", "João", "Carlos", "Maria"]
print("Lista de nomes em ordem crescente de comprimento:", sorted(nomes, key=len))

# Slicing avançado
print("\nSlicing avançado:")
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Elementos ímpares:", lista[1::2])  # Começa no índice 1 e pula de 2 em 2
print("Elementos pares em ordem reversa:", lista[::2][::-1])  # Pega os elementos pares e inverte a ordem

# Manipulação de listas aninhadas
print("\nManipulação de listas aninhadas:")
lista_aninhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Primeiro elemento da primeira lista:", lista_aninhada[0][0])  # Acessa o primeiro elemento da primeira lista

# Desempacotamento de listas
print("\nDesempacotamento de listas:")
x, y, z = [1, 2, 3]
print("x:", x)
print("y:", y)
print("z:", z)
