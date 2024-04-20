# Lista original de números
lista = [1, 4, 2, 7, 3]
"""
Este programa permite ao usuário visualizar uma lista de números e escolher dois números 
para trocar suas posições. O usuário pode continuar trocando números quantas vezes 
desejar ou pode sair do programa quando estiver satisfeito.

Lógica de funcionamento:
1. Exibir a lista atual de números.
2. Solicitar dois números do usuário para trocar.
3. Verificar se os números estão na lista.
4. Trocar os números nas posições correspondentes usando os índices.
5. Perguntar ao usuário se deseja continuar trocando números.
6. Repetir o processo até que o usuário decida sair do programa.
"""

# Loop principal para exibir a lista e solicitar entrada do usuário
while True:
    # Exibe cada número da lista
    for num in lista:
        print(f"numero: {num}")
    
    # Loop interno para obter números para troca
    while True:
        # Solicita o primeiro número para troca
        num1 = int(input("Digite o número que deseja trocar: "))
        
        # Solicita o segundo número para troca
        num2 = int(input(f"Digite o número pelo qual você deseja trocar o número {num1}: "))
        
        # Verifica se o primeiro número está na lista
        if num1 not in lista:
            print("Número não está na lista!")
            continue
        
        # Verifica se o segundo número está na lista
        elif num2 not in lista:
            print("Número não está na lista!")
            continue
        
        # Se ambos os números estão na lista, sai do loop interno
        else:
            break
    
    # Encontra os índices dos números na lista usando a função index()
    id1 = lista.index(num1)
    id2 = lista.index(num2)
    
    # Troca os números usando uma variável temporária
    temp = lista[id1]
    lista[id1] = lista[id2]
    lista[id2] = temp
    
    # Pergunta ao usuário se deseja continuar
    continuar = input("Deseja continuar? (s/n): ").upper().strip()[0]
    
    # Se o usuário não deseja continuar, sai do loop principal
    if continuar != 'S':
        break
