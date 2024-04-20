# Método 1: Loop for para inverter a string
palavra1 = "exemplo"
palavra_contrario1 = ''

# Percorre cada caractere da palavra original
for p in palavra1:
    # Adiciona o caractere atual (p) no início da palavra_contrario1.
    # A expressão "(p + palavra_contrario1)" concatena o caractere atual (p)
    # com a palavra_contrario1, colocando-o no início da palavra invertida.
    palavra_contrario1 = (p + palavra_contrario1)

# Imprime a palavra invertida
print(f"Usando loop for: {palavra_contrario1}")

# Método 2: Usando slice para inverter a string
palavra2 = "python"
palavra_contrario2 = palavra2[::-1]

# Imprime a palavra invertida
print(f"Usando slice: {palavra_contrario2}")

# Método 3: Usando a função reversed e join para inverter a string
palavra3 = "programação"
palavra_contrario3 = ''.join(reversed(palavra3))

# Imprime a palavra invertida
print(f"Usando reversed e join: {palavra_contrario3}")
