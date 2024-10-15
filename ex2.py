with open('pares.txt', 'r') as pares_file:
    pares = [int(linha.strip()) for linha in pares_file.readlines()]

if pares == sorted(pares):
    pares.sort(reverse=True)
    ordem = "decrescente"
elif pares == sorted(pares, reverse=True):
    pares.sort()
    ordem = "crescente"
else:
    print("Erro: O arquivo não está totalmente ordenado.")
    exit()

with open('pares.txt', 'w') as pares_file:
    for numero in pares:
        pares_file.write(f"{numero}\n")

print(f"Arquivo 'pares.txt' alterado para ordem {ordem} com sucesso!")