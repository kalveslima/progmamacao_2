memo = {}

def quadribonacci(n):
    if n <= 4:
        return n - 1

    if n in memo:
        return memo[n]

    resultado = quadribonacci(n-1) + quadribonacci(n-2) + quadribonacci(n-3) + quadribonacci(n-4)
    memo[n] = resultado
    return resultado


n = int(input())
print(quadribonacci(n))