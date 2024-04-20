# Lista de strings contendo nomes e números
string_junta = ["norton vandre de jesuz 02716641965", "joao 0841235467"]

# Lista para armazenar os dados separados
dados = []

# Loop para iterar sobre cada string na lista string_junta
for palavra in string_junta:
    # Inicializa as variáveis nome e número como strings vazias
    numero = ''
    nome = ''
    
    # Loop para iterar sobre cada caractere da string atual
    for string_separada in palavra:
        # Verifica se o caractere é um número
        if string_separada.isnumeric():
            # Se for número, adiciona ao final da string numero
            numero += string_separada
        else:
            # Se não for número, adiciona ao final da string nome
            nome += string_separada
    
    # Adiciona uma tupla contendo o nome e o número à lista dados
    dados.append((nome, numero))

# Imprime a lista de dados
print(dados)
