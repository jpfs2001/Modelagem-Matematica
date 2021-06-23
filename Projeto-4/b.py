def calcularB(A, X):
    b = []
    for linha in A:
        soma = 0
        for i in range(len(linha)):
            soma += linha[i][0]*X[i]
        b.append(soma)
    return b