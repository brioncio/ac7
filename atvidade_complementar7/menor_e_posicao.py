N = int(input())
X = list(map(int, input().split()))

menorValor = min(X)
posicao = X.index(menorValor)

print(f"Menor valor: {menorValor}")
print(f"Posicao: {posicao}")
