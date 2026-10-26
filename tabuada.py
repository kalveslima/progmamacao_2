n = int(input())

for _ in range(n):
    palavras = input().split()
    palavras.sort(key=len)
    print(' '.join(palavras))
    #exercicio 3 do segundo trabalho do lucio, os nomes estao incorretos