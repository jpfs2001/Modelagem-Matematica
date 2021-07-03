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

def normaEuclidiana(V): 
    n = 0
    for v in V:
        n += v[0]**2
        
    n = n**0.5

    return n


def produtoEscalar(A, B):
    p = 0
    for i in range(len(A)):
        p += A[i][0]*B[i][0]
    return p

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

def diferencaMatrizes(m1, m2):
    # cria primeiramente uma matriz de diferença
    diferenca = []
    for i in range(0, len(m1)):
        # mesma coisa, só que criando uma linha
        linha = []
        for j in range(0, len(m1[i])):
            #calcula a diferença entre cada termo, já que há correspondência
            linha.append(m1[i][j] - m2[i][j])
        diferenca.append(linha)
    return diferenca

def chuteInicial(tamanho):
    chute = []
    for j in range(tamanho):
        linha = [1/tamanho]
        chute.append(linha)
    return chute

def c(M):
    c = -1

    for coluna in range(len(M[0])):
        min_ = M[0][coluna]
    
    for linha in range(len(M)):
        if min_ < M[linha][coluna]:
            min_ = M[linha][coluna]
        
    mod = 1 - 2*min_
    if mod < 0:
        mod = (-1)*mod
        
    if c < mod:
        c = mod

    return c

def calculoErro(xk, xk1):
    c_ = c(M)    
    return (c_/(1-c_))*normaEuclidiana(diferencaMatrizes(xk, xk1))


def autovetor(A, x0, margem):
    # definição do vetor X
    X = [x0]
    erro = 10**8
    listaErro = []
    while erro > margem:
        xi = produtoMatriz(A, X[-1])
        X.append(xi)
        erro = calculoErro(X[-1], X[-2])
        listaErro.append(erro)

    return [X, listaErro]

A = [
    [0, 0, 1, .5], 
    [1/3, 0, 0, 0], 
    [1/3, .5, 0, .5], 
    [1/3, .5, 0, 0]
]

y0 = chuteInicial(len(A))
m = 0.15
margem = 0.001

M = calculoM(m, A)

print(f'{"*"*40}\n O programa só calcula o dominante \n{"*"*40} \n M: ')

for mi in M:
    print(mi)

[eigenVet, listaErro] = autovetor(M, y0, margem)
eigenVet = eigenVet[-1] # este é o X mais preciso
ultimoErro = listaErro[-1] # este é o último erro
print(f'\n autovetor: {eigenVet} / erro: {ultimoErro}')