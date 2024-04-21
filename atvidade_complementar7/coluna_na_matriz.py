coluna = int(input())
tipoDeOperacao = input().upper()

M = []
for i in range(12):
    linha = list(map(float, input().split()))
    M.append(linha)

if coluna < 0 or coluna > 11:
    print("Número de coluna inválido. Deve estar entre 0 e 11.")
else:
    soma = sum(M[linha][coluna] for linha in range(12))

    if tipoDeOperacao == "M":
        resultado = soma / 12
    else:
        resultado = soma

    print(f'{resultado:.1f}')

