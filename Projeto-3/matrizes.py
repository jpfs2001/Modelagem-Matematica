class Matrizes:        
    def gerarIdentidade(self, tamanho):
        # resumindo, pega uma matriz vazia
        identidade = [0]*tamanho
        for i in range(0, tamanho):
            # gera uma linha com o tamanho desejado
            identidade[i] = [0]*tamanho
            # estabelece os elementos diagonais como 1
            identidade[i][i] = 1
        return identidade

    def diferencaMatrizes(self, m1, m2):
        # cria primeiramente uma matriz de diferença
        diferenca = [0]*len(m1) 
        for i in range(0, len(m1)):
            # mesma coisa, só que criando uma linha
            diferenca[i] = [0]*len(m1)
            for j in range(0, len(m1)):
                #calcula a diferença entre cada termo, já que há correspondência
                diferenca[i][j] = m1[i][j] - m2[i][j]
        return diferenca
    
    def cofator(self, matriz, ponto):
        # matriz cofator
        M = []
        for i in range(0, len(matriz)):
            l = []
            for j in range(0, len(matriz)):
            # pega todos os elementos que não têm linha i e coluna j
                if i != ponto[0] and j != ponto[1]:
                    l.append(matriz[i][j])
            # no caso em que é a_{ixj}, a linha fica vazia, então a gente ignora ela
            if len(l) != 0: M.append(l)
        return (-1)**(sum(ponto))*self.determinanteLU(M)

    def transposta(self, matriz):
        # matriz vazia
        m = [0]*len(matriz)
        # a transposta é basicamente trocar quem está na coluna por quem está na linha e vice-versa
        for i in range(0, len(matriz)):
            # cria linha
            m[i] = [0]*len(matriz)
            # troca
            for j in range(0, len(matriz)):
                m[i][j] = matriz[j][i]
        return m

    def adjunta(self, matriz):
        # a adjunta é uma transposta de matriz de cofatores...
        M = []
        for i in range(0, len(matriz)):
            l = []
            # calcula os cofatores e suas determinantes
            for j in range(0, len(matriz)):
                l.append(self.cofator(matriz, [i, j]))
            M.append(l)
        return self.transposta(M)

    def inversa(self, matriz):
        # a inversa de A pode ser dada por A^{-1} = adj(A)/det(A), por isso ela não existe se det(A) = 0
        return self.multiplicacaoNumeroReal(self.adjunta(matriz), 1/self.determinanteLU(matriz))

    def determinanteLaplace(self, matriz):
        # a determinante usando o método de Laplace utiliza os cofatores
        # se for uma matriz 2x2, a determinante é esse produto básico
        if len(matriz) == 2:
            return matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]

        # se for uma matriz maior que 2x2, aí tem um produto entre certos elementos pela determinante de seus cofatores
        det = 0
        for i in range(0, len(matriz)):
            det += self.cofator(matriz, [i, 0])
        return det

    def multiplicacao(self, m1, m2):
        # a multiplicação de matrizes é dada por, sendo A_{ixn}*B_{nxj} = C_{ixj}
        # o termo c_{ixk} = sum_{j=1}^n a_{ixj}*b{jxk}
        matriz = [0]*len(m2)
        for i in range(0, len(m1)):
            total = 0
            for j in range(0, len(m1[i])):
                total += m1[i][j]*m2[j]    
            matriz[i] = total
        return matriz

    def multiplicacaoNumeroReal(self, m, numero):
        # multiplicar uma matriz por um número real é multiplicar cada elemento dessa matriz por aquele número...
        for i in range(0, len(m)):
            for j in range(0, len(m)):
                m[i][j] *= numero
        return m

    def decomposicao(self, matriz):
        tamanho = len(matriz)
        L = self.gerarIdentidade(tamanho)

        U = matriz.copy()
        for coluna in range(0, len(matriz)-1):
            for linha in range(coluna+1, len(matriz)):
                L[linha][coluna] = U[linha][coluna]/U[coluna][coluna]
                for c in range(coluna, len(matriz)):
                    U[linha][c] -= L[linha][coluna]*U[coluna][c]
        return [L, U]

    def determinanteLU(self, matriz):
        U = self.decomposicao(matriz)[1]
        det = 1
        for i in range(0, len(U)):
            det *= U[i][i]
        return det