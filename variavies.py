# Funções e Métodos Relacionados a Variáveis em Python

# 1. type(): Retorna o tipo de dados de uma variável.
x = 5
print(type(x))  # Saída: <class 'int'>

# 2. id(): Retorna o identificador único de um objeto em memória.
x = 5
print(id(x))  # Saída: endereço de memória onde o valor 5 está armazenado

# 3. dir(): Retorna uma lista de todos os atributos e métodos disponíveis para um objeto.
x = "Olá"
print(dir(x))  # Lista todos os métodos disponíveis para strings

# 4. len(): Retorna o comprimento de um objeto, como uma sequência (string, lista, etc.).
lista = [1, 2, 3, 4, 5]
print(len(lista))  # Saída: 5

# 5. del: Remove uma variável ou item de uma sequência.
x = 5
del x  # Remove a variável x

# 6. setattr() e getattr(): Permitem definir e obter atributos de um objeto dinamicamente.
class Pessoa:
    nome = "Alice"

p = Pessoa()
setattr(p, 'idade', 30)  # Define o atributo 'idade'
print(getattr(p, 'idade'))  # Obtém o valor do atributo 'idade'
