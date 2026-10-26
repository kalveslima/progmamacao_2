n = int(input('Número de crianças: '))

nomes = []
bons = 0
maus = 0

for _ in range(n):
    entrada = input('Entrada: ')
    sinal = entrada[0]
    nome = entrada[1:].strip()

    nomes.append(nome)

    if sinal == '+':
        bons += 1
    else:
        maus += 1

nomes.sort()

for nome in nomes:
    print(nome)

print(f"Criancas boazinhas: {bons}")
print(f"Criancas levadas: {maus}")
# ESSES EXERCICIOS SAO DO SEGUNDO TRABALHO DO LUCIO OS NOMES ESTAO INCORRETOS.... EX 1