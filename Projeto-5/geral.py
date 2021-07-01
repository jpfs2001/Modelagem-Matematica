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
            x0 = produtoMatriz(A, y[-1])
            # y.append(produtoNumeroReal(x0, 1/normaEuclidiana(x0)))
            y.append(x0)
            print(abs(abs(produtoEscalar(y[-1], y[-2]))-1))

        erro = abs(abs(produtoEscalar(y[-1], y[-2]))-1)
    else:
        erro = 10
        y = [y0]
        while erro > margem:
            x0 = produtoMatriz(A, y[-1])
            y.append(x0)
            print(erro)
            erro = abs(produtoEscalar(y[-1], y[-2])-1)

    return [y, erro]

def produtoEscalar(A, B):
    p = 0
    for i in range(len(A)):
        p += A[i][0]*B[i][0]
    return p

def autovalor(A, y):
    return produtoEscalar(y, produtoMatriz(A, y))

def somaMatrizes(m1, m2):
    # cria primeiramente uma matriz de soma
    soma = [0]*len(m1) 
    for i in range(len(m1)):
        # mesma coisa, só que criando uma linha
        soma[i] = [0]*len(m1)
        for j in range(len(m1)):
            #calcula a soma entre cada termo, já que há correspondência
            soma[i][j] = m1[i][j] + m2[i][j]
    return soma

def calculoM(m, A):
    S = []
    for i in range(len(A)):
        linha = []
        for j in range(len(A[i])):
            linha.append(1/len(A))
        S.append(linha)
    
    m1 = produtoNumeroReal(A, 1-m) # (1-m)A
    m2 = produtoNumeroReal(S, m) # mS
    M = somaMatrizes(m1, m2)
    return M

def chuteInicial(tamanho):
    chute = []
    for j in range(tamanho):
        linha = [1/tamanho]
        chute.append(linha)
    return chute
    
### Tarefas ###
# [X] Encontrar o A
# [X] A partir do A, calcular M = (1-m)A+ mS, onde S(n x n) = [[1/n, ...], ..., [1/n, ...]]
# [X] A partir do M, achar o x, dado que x(k) = Mx(k-1)

A = [
    [0, 0, 1, .5], 
    [1/3, 0, 0, 0], 
    [1/3, .5, 0, .5], 
    [1/3, .5, 0, 0]
]

y0 = chuteInicial(len(A))
k = 40
m = 0.15

M = calculoM(m, A)

print(f'{"*"*40}\n O programa só calcula o dominante \n{"*"*40} \n M: ')

for mi in M:
    print(mi)

[eigenVet, erro] = autovetor(M, y0, k)
eigenVet = eigenVet[-1]
# eigenVal = autovalor(A, eigenVet)
# print(f'\n autovetor: {eigenVet} \n autovalor: {eigenVal}')
print(f'\n autovetor: {eigenVet}')