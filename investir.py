while True:
    n, q = map(int, input('N e Q: ').split())

    notas = []
    for _ in range(n):
        notas.append(int(input()))
    notas.sort(reverse=True)

    for _ in range(q):
        p = int(input())
        print(notas[p - 1])
        #exercicio 2 do segundo trabalho do lucio, os nomes estao incorretos