# Criando um dicionário
meu_dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

# Acessando valores do dicionário
print("Acessando valores:")
print("Nome:", meu_dicionario['nome'])  # Saída: João
print("Idade:", meu_dicionario['idade'])  # Saída: 30
print("Cidade:", meu_dicionario['cidade'])  # Saída: São Paulo

# Alterando valores do dicionário
meu_dicionario['idade'] = 31
print("\nAlterando valores:")
print("Nova idade:", meu_dicionario['idade'])  # Saída: 31

# Adicionando novos pares chave-valor
meu_dicionario['profissão'] = 'Engenheiro'
print("\nAdicionando novo par chave-valor:")
print("Profissão:", meu_dicionario['profissão'])  # Saída: Engenheiro

# Removendo um par chave-valor
del meu_dicionario['cidade']
print("\nRemovendo um par chave-valor:")
print("Dicionário após a remoção:", meu_dicionario)  # Saída: {'nome': 'João', 'idade': 31, 'profissão': 'Engenheiro'}

# Verificando se uma chave existe no dicionário
print("\nVerificando se uma chave existe:")
if 'cidade' in meu_dicionario:
    print("A chave 'cidade' existe no dicionário.")
else:
    print("A chave 'cidade' não existe no dicionário.")

# Iterando sobre as chaves do dicionário
print("\nIterando sobre as chaves:")
for chave in meu_dicionario.keys():
    print(chave)

# Iterando sobre os valores do dicionário
print("\nIterando sobre os valores:")
for valor in meu_dicionario.values():
    print(valor)

# Iterando sobre itens (pares chave-valor) do dicionário
print("\nIterando sobre itens:")
for chave, valor in meu_dicionario.items():
    print(chave, ":", valor)

# Compreensão de dicionário
print("\nCompreensão de dicionário:")
pares_chave_valor = {chave: valor for chave, valor in meu_dicionario.items() if chave != 'profissão'}
print("Dicionário resultante:", pares_chave_valor)

# Método get()
print("\nMétodo get():")
print("Idade:", meu_dicionario.get('idade'))  # Saída: 31
print("Altura:", meu_dicionario.get('altura', 'Altura não especificada'))  # Saída: Altura não especificada

# Método setdefault()
print("\nMétodo setdefault():")
print("Cidade:", meu_dicionario.setdefault('cidade', 'Rio de Janeiro'))  # Saída: Rio de Janeiro
print("Dicionário após setdefault:", meu_dicionario)  # Saída: {'nome': 'João', 'idade': 31, 'profissão': 'Engenheiro', 'cidade': 'Rio de Janeiro'}

# Método popitem()
print("\nMétodo popitem():")
chave, valor = meu_dicionario.popitem()
print("Item removido:", chave, ":", valor)
print("Dicionário após popitem:", meu_dicionario)

# Método pop()
print("\nMétodo pop():")
profissao = meu_dicionario.pop('profissão')
print("Profissão removida:", profissao)
print("Dicionário após pop:", meu_dicionario)

# Método clear()
print("\nMétodo clear():")
meu_dicionario.clear()
print("Dicionário após clear:", meu_dicionario)

# Usando OrderedDict
from collections import OrderedDict

print("\nUsando OrderedDict:")
dicionario_ord = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print("Dicionário original:", dicionario_ord)

# Usando defaultdict
from collections import defaultdict

print("\nUsando defaultdict:")
dicionario_def = defaultdict(int)
dicionario_def['a'] = 1
dicionario_def['b'] = 2
print("Dicionário defaultdict:", dicionario_def)
print("Valor padrão para chave 'c':", dicionario_def['c'])  # Retorna 0 (int padrão)

# Fatiamento de dicionários
print("\nFatiamento de dicionários:")
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
chaves = ['a', 'c', 'e']
sub_dicionario = {chave: dicionario[chave] for chave in chaves}
print("Sub dicionário:", sub_dicionario)

# Outros métodos úteis: update(), copy()
print("\nOutros métodos úteis:")
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d1.update(d2)
print("Dicionário após update:", d1)
copia_dicionario = d1.copy()
print("Cópia do dicionário:", copia_dicionario)

