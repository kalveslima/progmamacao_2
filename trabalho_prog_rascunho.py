import sys
sys.setrecursionlimit(10000)

memo = {}

def pascal(l, c):
    if c == 1 or c == l:
        return 1

    if (l, c) in memo:
        return memo[(l, c)]

    resultado = pascal(l - 1, c) + pascal(l - 1, c - 1)
    memo[(l, c)] = resultado
    return resultado


l, c = map(int, input().split())
print(pascal(l, c))
#exercicio 4 do segundo trabalho do lucio, os nomes estao incorretos