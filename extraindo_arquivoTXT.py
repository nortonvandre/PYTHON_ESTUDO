with open("arquivo.txt", "r") as arquivo:
    # Lê todas as linhas do arquivo e armazena em uma lista
    conteudo = arquivo.readlines()
lista = []
for linha in conteudo:
    # Remove a quebra de linha no final de cada linha
    linha = linha.strip()
    
    
    nome = linha.split("Nome ")[1].split(" CPF ")[0]
    numero = linha.split(" CPF ")[1]
    lista.append([nome,numero])
    
    
for nome,cpf in lista:
    print(nome,cpf)
