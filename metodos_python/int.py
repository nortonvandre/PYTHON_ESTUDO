# Definindo um número inteiro
num = 42

# Funções embutidas
print("Funções embutidas:")
print("int():", int())  # Retorna 0
print("bin():", bin(num))  # Retorna a representação binária do número
print("oct():", oct(num))  # Retorna a representação octal do número
print("hex():", hex(num))  # Retorna a representação hexadecimal do número
print("abs():", abs(-5))  # Retorna o valor absoluto
print("pow():", pow(2, 3))  # Retorna a potência (2 elevado a 3)
print("sum():", sum([1, 2, 3]))  # Retorna a soma dos elementos da lista
print("round():", round(3.14159, 2))  # Arredonda o número para 2 casas decimais
print("max():", max([1, 2, 3]))  # Retorna o maior elemento da lista
print("min():", min([1, 2, 3]))  # Retorna o menor elemento da lista

# Métodos de objeto
print("\nMétodos de objeto:")
print("bit_length():", num.bit_length())  # Retorna o número de bits necessário para representar o número
print("to_bytes():", num.to_bytes(2, byteorder='big'))  # Retorna a representação do número como uma sequência de bytes
print("from_bytes():", int.from_bytes(b'\x00*', byteorder='big'))  # Converte uma sequência de bytes em um número
print("__add__():", num.__add__(5))  # Retorna a soma do número com outro
print("__sub__():", num.__sub__(5))  # Retorna a diferença do número com outro
print("__mul__():", num.__mul__(2))  # Retorna o produto do número por outro
print("__floordiv__():", num.__floordiv__(5))  # Retorna a divisão inteira do número por outro
print("__mod__():", num.__mod__(5))  # Retorna o resto da divisão do número por outro
print("__pow__():", num.__pow__(3))  # Retorna o número elevado a uma potência
print("__abs__():", (-5).__abs__())  # Retorna o valor absoluto do número

# Funções adicionais
print("\nFunções adicionais:")
print("divmod():", divmod(10, 3))  # Retorna o par de quociente e resto da divisão
print("isinstance():", isinstance(num, int))  # Verifica se o objeto é uma instância de uma classe
print("issubclass():", issubclass(int, object))  # Verifica se a classe é uma subclasse de outra
print("reversed():", list(reversed([1, 2, 3])))  # Retorna uma lista reversa
print("round():", round(3.14159, 2))  # Arredonda o número para 2 casas decimais
print("format():", format(123, '04d'))  # Formata o número como uma string com 4 dígitos, preenchendo com zeros à esquerda se necessário
