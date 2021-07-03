# a classe abaixo define alguns métodos utilizados para matrizes
class Matrizes:
    # produto entre duas matrizes
    def produtoMatriz(self, A, B):
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

    # produto de um número real por uma matriz
    def produtoNumeroReal(self, A, x):
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i][j] *= x
        return A

    # soma entre duas matrizes
    def somaMatrizes(self, m1, m2):
        # cria primeiramente uma matriz de soma
        soma = [0]*len(m1) 
        for i in range(len(m1)):
            # mesma coisa, só que criando uma linha
            soma[i] = [0]*len(m1)
            for j in range(len(m1)):
                #calcula a soma entre cada termo, já que há correspondência
                soma[i][j] = m1[i][j] + m2[i][j]
        return soma

    # diferença entre duas matrizes
    def diferencaMatrizes(self, m1, m2):
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

    # matriz M utilizada, dado que M = (1-m)A + mS
    # esta é a matriz perturbada de A
    def calculoM(self, m, A):
        S = []
        for i in range(len(A)):
            linha = []
            for j in range(len(A[i])):
                linha.append(1/len(A))
            S.append(linha)
        
        m1 = self.produtoNumeroReal(A, 1-m) # (1-m)A
        m2 = self.produtoNumeroReal(S, m) # mS
        M = self.somaMatrizes(m1, m2)
        return M

# a classe abaixo contém os principais métodos para vetores
class Vetores:
    # cálculo da norma euclidiana de um vetor
    def normaEuclidiana(self, V): 
        n = 0
        for v in V:
            n += v[0]**2
        n = n**0.5
        return n
    
    # cálculo do produto escalar A \cdot B
    def produtoEscalar(self, A, B):
        p = 0
        for i in range(len(A)):
            p += A[i][0]*B[i][0]
        return p

class Google:
    def __init__(self, A, m):
        # instanciamento das classes utilizadas
        self.Mat = Matrizes()
        self.Vet = Vetores()

        # definição de A e m no ambiente da classe
        self.A = A
        self.m = m
   
    # cálculo geral exigido
    def X(self, margem):
        # chute inicial
        self.x0 = self.chuteInicial()
        # matriz perturbada
        self.M = self.Mat.calculoM(self.m, self.A)
        
        # constante de erro
        self.c_ = self.c() 

        [ autovetor_iteracoes, listaErro ] = self.autovetorDominante(margem)

        return [ autovetor_iteracoes, listaErro, self.c_ ]

    # constante de erro que pode ser calculada imediatamente após o cálculo da matriz perturbada
    def c(self):
        c = -1

        for coluna in range(len(self.M[0])):
            min_ = self.M[0][coluna]
        
        for linha in range(len(self.M)):
            if min_ < self.M[linha][coluna]:
                min_ = self.M[linha][coluna]
            
        mod = 1 - 2*min_
        if mod < 0:
            mod = (-1)*mod
            
        if c < mod:
            c = mod

        return c
    
    # cálculo do erro
    def calculoErro(self, xk, xk1):
        return (self.c_/(1-self.c_))*self.Vet.normaEuclidiana(self.Mat.diferencaMatrizes(xk, xk1))

    # gera a matriz coluna de elementos 1/n
    def chuteInicial(self):
        tamanho = len(self.A)
        chute = []
        for j in range(tamanho):
            linha = [1/tamanho]
            chute.append(linha)
        return chute

    # cálculo do autovetor dominante com base na margem de erro oferecida
    def autovetorDominante(self, margem):
        # definição do vetor X
        autovetor_iteracoes = [self.x0]
        # erro absurdo inicial
        erro = 10**8
        # lista onde serão armazenados os erros
        listaErro = []
        # calcula até o erro ficar menor que a margem oferecida
        while erro > margem:
            # calcula o X e o adiciona na lista de X
            xi = self.Mat.produtoMatriz(self.M, autovetor_iteracoes[-1])
            autovetor_iteracoes.append(xi)
            # calcula o erro e o adiciona na lista de erros
            erro = self.calculoErro(autovetor_iteracoes[-1], autovetor_iteracoes[-2])
            listaErro.append(erro)
        
        return [autovetor_iteracoes, listaErro]