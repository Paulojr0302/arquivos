with open('pares.txt', 'r') as pares_file:
    pares = [int(linha.strip()) for linha in pares_file.readlines()]

with open('impares.txt', 'r') as impares_file:
    impares = [int(linha.strip()) for linha in impares_file.readlines()]

todos_numeros = sorted(pares + impares)

with open('paresimpares.txt', 'w') as result_file:
    for numero in todos_numeros:
        result_file.write(f"{numero}\n")

print("arquivo criado")