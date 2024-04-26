# Criando uma tupla
minha_tupla = (1, 2, 3, 4, 5)
print("Tupla:", minha_tupla)

# Acessando elementos da tupla
print("\nAcessando elementos da tupla:")
print("Primeiro elemento:", minha_tupla[0])  # Saída: 1
print("Último elemento:", minha_tupla[-1])  # Saída: 5

# Tentativa de modificação de elementos (não é permitido)
# minha_tupla[0] = 10  # TypeError: 'tuple' object does not support item assignment

# Desempacotamento de tupla
a, b, c, d, e = minha_tupla
print("\nDesempacotamento de tupla:")
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)

# Comprimento da tupla
print("\nComprimento da tupla:", len(minha_tupla))  # Saída: 5

# Contagem de ocorrências de um elemento
print("Contagem de ocorrências de 3:", minha_tupla.count(3))  # Saída: 1

# Encontrando o índice de um elemento
print("Índice do elemento 4:", minha_tupla.index(4))  # Saída: 3

# Tuplas podem conter diferentes tipos de dados
tupla_mista = (1, 'a', True, 3.14)
print("\nTupla mista:", tupla_mista)

# Concatenação de tuplas
outra_tupla = ('b', False)
tupla_concatenada = minha_tupla + outra_tupla
print("\nConcatenação de tuplas:", tupla_concatenada)

# Repetição de elementos em uma tupla
tupla_repetida = (1,) * 3
print("\nRepetição de elementos em uma tupla:", tupla_repetida)

# Convertendo uma lista em uma tupla
lista = [1, 2, 3]
tupla_convertida = tuple(lista)
print("\nConvertendo uma lista em uma tupla:", tupla_convertida)

# Convertendo uma tupla em uma lista
lista_convertida = list(minha_tupla)
print("Convertendo uma tupla em uma lista:", lista_convertida)

# Removendo uma tupla
del minha_tupla
# print(minha_tupla)  # NameError: name 'minha_tupla' is not defined

# Criando uma tupla vazia
tupla_vazia = ()
print("\nTupla vazia:", tupla_vazia)

# Adicionando elementos a uma tupla (não é possível)
# tupla_vazia.append(1)  # AttributeError: 'tuple' object has no attribute 'append'

# Deletando uma tupla
del tupla_vazia
# print(tupla_vazia)  # NameError: name 'tupla_vazia' is not defined

# Usando tuplas como chaves em dicionários (devido à imutabilidade)
dicionario = {(1, 2): 'valor'}
print("\nDicionário com tupla como chave:", dicionario[(1, 2)])  # Saída: 'valor'

# Tuplas como valores de retorno de funções
def retorna_tupla():
    return 1, 2, 3

resultado = retorna_tupla()
print("\nTupla retornada pela função:", resultado)  # Saída: (1, 2, 3)

# Desempacotamento parcial
a, *resto = minha_tupla
print("\nDesempacotamento parcial:")
print("a:", a)
print("resto:", resto)  # Saída: [2, 3, 4, 5]

# Comparando tuplas (ordem dos elementos é considerada)
tupla1 = (1, 2, 3)
tupla2 = (1, 2, 4)
print("\nComparando tuplas:")
print("tupla1 == tupla2:", tupla1 == tupla2)  # Saída: False
print("tupla1 < tupla2:", tupla1 < tupla2)  # Saída: True

# Tuplas nomeadas (a partir do Python 3.6)
from collections import namedtuple

Ponto = namedtuple('Ponto', ['x', 'y'])
p = Ponto(10, y=20)
print("\nTuplas nomeadas:")
print("Ponto x:", p.x)
print("Ponto y:", p.y)

# Fim do programa
