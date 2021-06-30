def produtoMatriz(A, B):
    linA, colA = len(A), len(A[0])
    linB, colB = len(B), len(B[0])

    produto = []
    for linha in range(linA):
        produto.append([])
        for coluna in range(colB):
            produto[linha].append(0)
            for k in range(colA):
                produto[linha][coluna] += A[linha][k] * B[k][coluna]

    return produto

def produtoNumeroReal(A, x):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] *= x
    return A

def potenciaMatriz(A, n):
    prod = A
    for i in range(1, n):
        prod = produtoMatriz(A, prod)
    return prod

def normaEuclidiana(V): 
    n = 0
    for v in V:
        n += v[0]**2
    n = n**0.5

    return n

def beta(A, x0, k):
    return 1/normaEuclidiana(produtoMatriz(potenciaMatriz(A, k), x0))

def autovetor(A, y0, k, margem=0):
    if margem == 0:
        y = [y0]
        for i in range(k):
            x0 = produtoMatriz(A, y[i])
            y.append(produtoNumeroReal(x0, 1/normaEuclidiana(x0)))

        erro = abs(abs(produtoEscalar(y[-1], y[-2]))-1)
    else:
        erro = 10
        y = [y0]
        while erro > margem:
            x0 = produtoMatriz(A, y[-1])
            y.append(produtoNumeroReal(x0, 1/normaEuclidiana(x0)))

            erro = abs(abs(produtoEscalar(y[-1], y[-2]))-1)

    return [y, erro]

def produtoEscalar(A, B):
    p = 0
    for i in range(len(A)):
        p += A[i][0]*B[i][0]
    return p

def autovalor(A, y):
    return produtoEscalar(y, produtoMatriz(A, y))

A = [[1, 2], [3, 2]]
y0 = [[1], [0]]
k = 10

[eigenVet, erro] = autovetor(A, y0, k, 0.0001)
eigenVet = eigenVet[-1]
eigenVal = autovalor(A, eigenVet)
print(f'{"*"*40}\n O programa só calcula o dominante \n{"*"*40}\n autovetor: {eigenVet} \n erro: {erro} \n autovalor: {eigenVal}')