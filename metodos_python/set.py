# Criando conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Operações com conjuntos: união, interseção, diferença, diferença simétrica
print("Operações com conjuntos:")
# União de conjuntos
uniao = conjunto1.union(conjunto2)
print("\nUnião de conjuntos:", uniao)  # Saída: {1, 2, 3, 4, 5, 6, 7, 8}

# Interseção de conjuntos
intersecao = conjunto1.intersection(conjunto2)
print("Interseção de conjuntos:", intersecao)  # Saída: {4, 5}

# Diferença entre conjuntos
diferenca = conjunto1.difference(conjunto2)
print("Diferença entre conjunto1 e conjunto2:", diferenca)  # Saída: {1, 2, 3}

# Diferença simétrica entre conjuntos
diferenca_simetrica = conjunto1.symmetric_difference(conjunto2)
print("Diferença simétrica entre conjuntos:", diferenca_simetrica)  # Saída: {1, 2, 3, 6, 7, 8}

# Métodos de Adição e Remoção
print("\nMétodos de Adição e Remoção:")
# Adicionar elemento ao conjunto
conjunto1.add(6)
print("Conjunto1 após adição:", conjunto1)  # Saída: {1, 2, 3, 4, 5, 6}

# Remover elemento do conjunto
conjunto1.remove(6)
print("Conjunto1 após remoção:", conjunto1)  # Saída: {1, 2, 3, 4, 5}

# Discard: Remover elemento do conjunto sem gerar erro se não existir
conjunto1.discard(7)
print("Conjunto1 após discard:", conjunto1)  # Saída: {1, 2, 3, 4, 5}

# Pop: Remove e retorna um elemento aleatório do conjunto
elemento_removido = conjunto1.pop()
print("Elemento removido por pop:", elemento_removido)
print("Conjunto1 após pop:", conjunto1)  # Conjunto com um elemento a menos

# Métodos de Atualização
print("\nMétodos de Atualização:")
conjunto1.update([6, 7, 8])
print("Conjunto1 após update:", conjunto1)  # Adiciona elementos do iterável ao conjunto

conjunto1.intersection_update(conjunto2)
print("Conjunto1 após intersection_update:", conjunto1)  # Mantém apenas elementos presentes em ambos os conjuntos

conjunto1.difference_update(conjunto2)
print("Conjunto1 após difference_update:", conjunto1)  # Mantém apenas elementos presentes no conjunto1 e não no conjunto2

conjunto1.symmetric_difference_update(conjunto2)
print("Conjunto1 após symmetric_difference_update:", conjunto1)  # Atualiza para conter elementos presentes em um dos conjuntos, mas não em ambos

# Operações de Pertencimento e Comparação
print("\nOperações de Pertencimento e Comparação:")
# Issubset: Retorna True se todos os elementos do conjunto estiverem presentes no iterável
print("conjunto1 é subconjunto de conjunto2:", conjunto1.issubset(conjunto2))

# Issuperset: Retorna True se todos os elementos do iterável estiverem presentes no conjunto
print("conjunto1 é superconjunto de conjunto2:", conjunto1.issuperset(conjunto2))

# Isdisjoint: Retorna True se o conjunto não tiver elementos em comum com o iterável
print("conjunto1 e conjunto2 têm elementos em comum:", conjunto1.isdisjoint(conjunto2))

# Operações de Cópia e Limpeza
print("\nOperações de Cópia e Limpeza:")
# Copy: Retorna uma cópia rasa do conjunto
copia_conjunto = conjunto1.copy()
print("Cópia do conjunto1:", copia_conjunto)

# Clear: Remove todos os elementos do conjunto
conjunto1.clear()
print("Conjunto1 após clear:", conjunto1)

# Fim do programa
