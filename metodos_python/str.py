# Métodos para Strings em Python

# capitalize(): Retorna uma cópia da string com o primeiro caractere em maiúsculo e o restante em minúsculo.
s = "hello world"
print("capitalize():", s.capitalize())  # Saída: "Hello world"

# upper(): Retorna uma cópia da string com todos os caracteres em maiúsculo.
print("upper():", s.upper())  # Saída: "HELLO WORLD"

# lower(): Retorna uma cópia da string com todos os caracteres em minúsculo.
print("lower():", s.lower())  # Saída: "hello world"

# title(): Retorna uma cópia da string com a primeira letra de cada palavra em maiúscula e as demais em minúscula.
print("title():", s.title())  # Saída: "Hello World"

# strip(): Retorna uma cópia da string com todos os espaços em branco removidos do início e do final da string.
s = "   hello world   "
print("strip():", s.strip())  # Saída: "hello world"

# replace(): Retorna uma cópia da string com todas as ocorrências de uma substring substituídas por outra.
s = "hello world"
print("replace():", s.replace("hello", "hi"))  # Saída: "hi world"

# split(): Retorna uma lista de substrings separadas por um delimitador.
print("split():", s.split())  # Saída: ['hello', 'world']

# join(): Retorna uma string concatenando os elementos de uma lista separados por um separador.
lista = ['hello', 'world']
print("join():", " ".join(lista))  # Saída: "hello world"

# find(): Retorna o índice da primeira ocorrência de uma substring na string (ou -1 se não encontrar).
print("find():", s.find("world"))  # Saída: 6

# rfind(): Retorna o índice da última ocorrência de uma substring na string (ou -1 se não encontrar).
print("rfind():", s.rfind("world"))  # Saída: 6

# index(): Retorna o índice da primeira ocorrência de uma substring na string (ou gera um ValueError se não encontrar).
print("index():", s.index("world"))  # Saída: 6

# rindex(): Retorna o índice da última ocorrência de uma substring na string (ou gera um ValueError se não encontrar).
print("rindex():", s.rindex("world"))  # Saída: 6

# count(): Retorna o número de ocorrências de uma substring na string.
print("count():", s.count("o"))  # Saída: 2

# startswith(): Verifica se a string começa com uma determinada substring.
print("startswith():", s.startswith("hello"))  # Saída: True

# endswith(): Verifica se a string termina com uma determinada substring.
print("endswith():", s.endswith("world"))  # Saída: True

# isalpha(): Retorna True se todos os caracteres da string forem letras.
print("isalpha():", s.isalpha())  # Saída: False

# isalnum(): Retorna True se todos os caracteres da string forem alfanuméricos (letras ou números).
s = "hello123"
print("isalnum():", s.isalnum())  # Saída: True

# isnumeric(): Retorna True se todos os caracteres da string forem dígitos.
s = "123"
print("isnumeric():", s.isnumeric())  # Saída: True

# isdigit(): Retorna True se todos os caracteres da string forem dígitos.
print("isdigit():", s.isdigit())  # Saída: True

# isdecimal(): Retorna True se todos os caracteres da string forem decimais.
print("isdecimal():", s.isdecimal())  # Saída: True

# isupper(): Retorna True se todos os caracteres da string forem maiúsculos.
s = "HELLO"
print("isupper():", s.isupper())  # Saída: True

# islower(): Retorna True se todos os caracteres da string forem minúsculos.
s = "hello"
print("islower():", s.islower())  # Saída: True

# isspace(): Retorna True se a string contiver apenas espaços em branco.
s = "   "
print("isspace():", s.isspace())  # Saída: True

# istitle(): Retorna True se a string estiver em formato de título (cada palavra começando com maiúscula).
s = "Hello World"
print("istitle():", s.istitle())  # Saída: True

# center(): Retorna uma cópia da string centralizada em um determinado número de caracteres.
s = "hello"
print("center():", s.center(10))  # Saída: "  hello   "

# ljust(): Retorna uma cópia da string justificada à esquerda em um campo de largura especificado.
print("ljust():", s.ljust(10))  # Saída: "hello     "

# rjust(): Retorna uma cópia da string justificada à direita em um campo de largura especificado.
print("rjust():", s.rjust(10))  # Saída: "     hello"

# zfill(): Preenche a string com zeros à esquerda até alcançar o comprimento especificado.
s = "42"
print("zfill():", s.zfill(5))  # Saída: "00042"

# expandtabs(): Expande os tabuladores em espaços.
s = "hello\tworld"
print("expandtabs():", s.expandtabs())  # Saída: "hello   world"

# encode(): Codifica a string usando o codec especificado.
s = "hello world"
print("encode():", s.encode(encoding="utf-8"))  # Saída: b'hello world'

# swapcase(): Retorna uma cópia da string com maiúsculas convertidas em minúsculas e vice-versa.
s = "Hello World"
print("swapcase():", s.swapcase())  # Saída: "hELLO wORLD"

# title(): Retorna uma cópia da string com a primeira letra de cada palavra em maiúscula e as demais em minúscula.
s = "hello world"
print("title():", s.title())  # Saída: "Hello World"

# partition(): Divide a string em três partes usando um separador e retorna uma tupla.
s = "hello.world"
print("partition():", s.partition("."))  # Saída: ('hello', '.', 'world')

# rpartition(): Divide a string em três partes usando um separador e retorna uma tupla, começando da direita.
s = "hello.world.world"
print("rpartition():", s.rpartition("."))  # Saída: ('hello.world', '.', 'world')

# lstrip(): Retorna uma cópia da string com todos os espaços em branco à esquerda removidos.
s = "   hello world   "
print("lstrip():", s.lstrip())  # Saída: "hello world"

# rstrip(): Retorna uma cópia da string com todos os espaços em branco à direita removidos.
s = "   hello world   "
print("rstrip():", s.rstrip())  # Saída: "   hello world"

# maketrans(): Retorna uma tabela de tradução a ser usada em conjunção com translate().
print("maketrans():", str.maketrans("aeiou", "12345"))

# translate(): Retorna uma cópia da string com os caracteres especificados traduzidos ou removidos.
s = "hello world"
translation_table = str.maketrans("aeiou", "12345")
print("translate():", s.translate(translation_table))  # Saída: "h2ll4 w4rld"

# format_map(): Substitui placeholders na string com valores do dicionário.
person = {'name': 'John', 'age': 30}
formatted_string = "{name} is {age} years old.".format_map(person)
print("format_map():", formatted_string)  # Saída: "John is 30 years old."


# Manipulação de strings

# Concatenação de strings
s1 = "hello"
s2 = "world"
concatenated = s1 + " " + s2
print("Concatenação:", concatenated)  # Saída: "hello world"

# Formatação de strings
name = "John"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print("Formatação:", formatted_string)  # Saída: "My name is John and I am 30 years old."

# Interpolação de strings (f-strings)
formatted_string = f"My name is {name} and I am {age} years old."
print("Interpolação:", formatted_string)  # Saída: "My name is John and I am 30 years old."

# Repetição de strings
repeated_string = "hello " * 3
print("Repetição:", repeated_string)  # Saída: "hello hello hello "

# Tamanho de uma string
print("Tamanho da string:", len(s1))  # Saída: 5

# Acesso aos caracteres de uma string
print("Primeiro caractere:", s1[0])  # Saída: 'h'
print("Último caractere:", s1[-1])  # Saída: 'o'

# Fatiamento de strings
substring = s1[1:4]
print("Fatiamento:", substring)  # Saída: 'ell'

# Fatiamento com passo
substring = s1[::2]
print("Fatiamento com passo:", substring)  # Saída: 'hlo'

# Fatiamento invertido
substring = s1[::-1]
print("Fatiamento invertido:", substring)  # Saída: 'olleh'

# Fatiamento com índices negativos
substring = s1[-3:-1]
print("Fatiamento com índices negativos:", substring)  # Saída: 'll'
