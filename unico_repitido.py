
lista = [1, 2, 1, 2, 3, 4, 4, 5, 5]
unicos = set()
repetidos = []

for num in lista:
    if num in unicos:
        repetidos.append(num)
    else:
        unicos.add(num)

# Encontrar o número que aparece uma única vez
for num in lista:
    if num not in repetidos:
        numero_unico = num
        break

print(unicos)
print(repetidos)

print(f"O número que aparece uma única vez é: {numero_unico}")


    
