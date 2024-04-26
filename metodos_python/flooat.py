# Definindo um número float
num = 3.14159

# Funções embutidas
print("Funções embutidas:")
print("float():", float())  # Retorna 0.0
print("abs():", abs(-5.5))  # Retorna o valor absoluto
print("round():", round(3.14159, 2))  # Arredonda o número para 2 casas decimais
print("max():", max([1.5, 2.5, 3.5]))  # Retorna o maior elemento da lista
print("min():", min([1.5, 2.5, 3.5]))  # Retorna o menor elemento da lista
print("sum():", sum([1.5, 2.5, 3.5]))  # Retorna a soma dos elementos da lista

# Métodos de objeto
print("\nMétodos de objeto:")
print("as_integer_ratio():", num.as_integer_ratio())  # Retorna a representação fracionária como um par de inteiros
print("is_integer():", num.is_integer())  # Retorna True se o número for um inteiro, caso contrário, False

# Funções adicionais
print("\nFunções adicionais:")
print("isfinite():", num.isfinite())  # Retorna True se o número for finito, caso contrário, False
print("isinf():", num.isinf())  # Retorna True se o número for infinito, caso contrário, False
print("isnan():", num.isnan())  # Retorna True se o número for NaN (Not a Number), caso contrário, False
print("hex():", float.hex(num))  # Retorna a representação hexadecimal do número
