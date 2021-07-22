# Este arquivo contém quase todas as funções utilizadas no projeto

from PIL import Image
from numpy import asarray
import matplotlib.pyplot as plt
import os
from comparacao import comparar
from time import process_time as pt

class Imagem:
    # a partir de uma imagem, encontra uma matriz única e normalizada
    def matrizDeImagemNormalizada(self, link):
        # bota a imagem aí
        image = Image.open(link)
        #converte para array
        data = asarray(image)

        matriz = []
        for i in data:
            m = []
            for j in i:
                try: 
                    a = j[3]
                except:
                    a = 1
                soma = 0
                if a != 0:
                    for k in j:
                        soma += k
                    soma -= a
                    soma /= 765
                m.append(soma)
            matriz.append(m)
        return matriz

    # a partir de uma imagem, encontra três matrizes separadas com R, G e B
    def matrizesRGBImagem(self, link):
        # bota a imagem aí
        image = Image.open(link)
        #converte para array
        data = asarray(image)
        # matrizes separadas
        R, G, B = [], [], []
        
        for i in data:
            R.append([])
            G.append([])
            B.append([])
            for j in i:
                R[-1].append(j[0]/255)
                G[-1].append(j[1]/255)
                B[-1].append(j[2]/255)

        return [R, G, B]

class Matrizes:
    # produto entre duas matrizes, com a possibilidade de arredondar
    def produtoMatriz(self, A, B, arredondar = 3):
        linA, colA = len(A), len(A[0])
        linB, colB = len(B), len(B[0])

        produto = []
        for linha in range(linA):
            produto.append([])
            for coluna in range(colB):
                produto[linha].append(0)
                for k in range(colA):
                    produto[linha][coluna] += A[linha][k] * B[k][coluna]
                if arredondar > 0:
                    produto[linha][coluna] = round(produto[linha][coluna], arredondar)

        return produto

    # verifica se duas matrizes são iguais
    def verificaMatrizes(self, m1, m2):
        for i in range(len(m1)):
            for j in range(len(m1)):
                if m1[i][j] != m2[i][j]: return False
        return True

    # mod 1 de todos os elementos de uma matriz
    def mod1Matriz(self, A):
        lista = []
        for i in A:
            linha = []
            for j in i:
                linha.append(j % 1)
            lista.append(linha)
        return lista

    def transposta(self, m):
        matriz = m
        for i in range(len(m)):
            for j in range(len(m)):
                matriz[j][i] = m[i][j]

        return matriz

class AlgoritmoGeral:
    def __init__(self):
        self.Matrizes = Matrizes()
        self.Arquivos = Arquivos()

    # itera uma matriz até que se chegue em seu período ou retorna Falso e sua lista de iterações se ultrapassar o limite passado
    def iterarMatriz(self, C, matriz, limIt, salvar = False, limItEncerra = False):

        matrizBase = matriz
        listaIteracoes = [matrizBase]
        contador = 0
        inicio = pt()
        while contador < limIt:
            contador += 1
            lista = []
            for i in range(len(matriz)):
                l = []
                for j in range(len(matriz)):
                    l.append(0)
                lista.append(l)
            for i in range(len(matriz)):
                for j in range(len(matriz)):
                    gama = self.funcaoGama(i/len(matriz), j/len(matriz), C)
                    x = round(gama[0][0]*len(matriz))
                    y = round(gama[1][0]*len(matriz))
                    lista[i][j] = matriz[x][y]
            matriz = lista
            listaIteracoes.append(lista)
            if salvar: Desenho().exibir(matriz, f'matrizSalva{contador}_{C[0][0]}_{C[0][1]}_{C[1][0]}_{C[1][1]}', [101, 101])
            if self.Matrizes.verificaMatrizes(matrizBase, matriz) and not limItEncerra:
                return [contador, listaIteracoes]
        if not limItEncerra: return [False, listaIteracoes]
        else: 
            print(f'gama: {pt() - inicio} s')
            return[contador, listaIteracoes]


    # função Gama como definida no enunciado
    def funcaoGama(self, x, y, C):
        prod = self.Matrizes.produtoMatriz(C, [[x], [y]])
        return self.Matrizes.mod1Matriz(prod)

    # itera para cada cor usando arquivos
    def matrizesArquivosRGB(self, C, limIt, nomeArquivo, salvar = False, limiteEncerra = False):
        # lista
        lista = []
        # iterações
        for qual in range(1, 4):
            matriz = self.Arquivos.matrizDeArquivo(f'{nomeArquivo}{qual}')
            m = self.iterarMatriz(C, matriz, limIt, salvar, limiteEncerra)
            if not m[0]: 
                return [False, qual, qual]
            lista.append(m)
        return lista

class Arquivos:
    # transforma os arquivos txt em matriz
    def matrizDeArquivo(self, nome):
        w = open(f'./{nome}.txt', 'r')
        txt = w.read()
        m1 = txt.split('\n')
        matriz = []
        for m in m1:
            # linha = m.split('  ')
            linha = m.split(' ')
            listc = []
            for l in linha:  
                if l != "": listc.append(float(l))
            matriz.append(listc)
        matriz.pop(-1)
        # print(len(matriz))
        w.close()
        return matriz

class Desenho:
    # desenha colorizado 
    def desenharColorizado(self, R, G, B, nome="mistura", tamanho = [101, 101]):

        [WIDTH, HEIGHT] = tamanho
        FILENAME = (f"./resultado/{nome}.png", "PNG")

        pillow_obj = Image.new("RGB", (WIDTH, HEIGHT))
        pixel_set = pillow_obj.load()
        for row in range(WIDTH):
            for col in range(HEIGHT):
                r, g, b = round(R[row][col]*255), round(G[row][col]*255), round(B[row][col]*255)
                # seta a cor do pixel em RGB
                pixel_set[row, col] = (r, g, b)

        pillow_obj.save(*FILENAME)
    # salva imagem preta e branca
    def exibir(self, matriz, nome, tamanho = [101, 101]):
        [WIDTH, HEIGHT] = tamanho
        FILENAME = (f"./figs/{nome}.png", "PNG")

        pillow_obj = Image.new("RGB", (WIDTH, HEIGHT))
        pixel_set = pillow_obj.load()
        for row in range(WIDTH):
            for col in range(HEIGHT):
                r, g, b = round(matriz[row][col]*255), round(matriz[row][col]*255), round(matriz[row][col]*255)
                # seta a cor do pixel em RGB
                pixel_set[row, col] = (r, g, b)

        pillow_obj.save(*FILENAME)
        
        # if (comparar('base', f'{nome}') + comparar('base2', f'{nome}') + comparar('base3', f'{nome}') + comparar('base4', f'{nome}') + comparar('base5', f'{nome}')+comparar('base6', f'{nome}')+comparar('base7', f'{nome}'))/7 < 20.51:
        #     os.remove(f'./figs/{nome}.png')

class funcoesProntas:
    # faz a tarefa lá do Calvin
    def arnoldTarefa(self, salvarIteracoes = True):
        C = [[1, 1], [1, 2]]
        limIt = 60
        [R, G, B] = AlgoritmoGeral().matrizesArquivosRGB(C, limIt, './tarefa/arnold', salvarIteracoes)
        qualIteracao = 6
        if R: Desenho().desenharColorizado(R[1][qualIteracao], G[1][qualIteracao], B[1][qualIteracao])
            
    # tarefa que envolve o outro grupo
    def tarefa_OutroGrupo(self, nome, it, chave, salvarIteracoes = True):
        C = chave
        R = Arquivos().matrizDeArquivo(f'{nome}1')
        G = Arquivos().matrizDeArquivo(f'{nome}2')
        B = Arquivos().matrizDeArquivo(f'{nome}3')
        R1 = AlgoritmoGeral().iterarMatriz(C, R, it, salvarIteracoes, True)
        G1 = AlgoritmoGeral().iterarMatriz(C, G, it, salvarIteracoes, True)
        B1 = AlgoritmoGeral().iterarMatriz(C, B, it, salvarIteracoes, True)
        it = 45
        Desenho().desenharColorizado(R1[1][it], G1[1][it], B1[1][it])

    # armazenar em arquivo txt no formato que os arquivos arnold têm
    def salvarEmTxt(self, matriz, nome):
        # matriz que conterá todas as linhas juntas
        txt = ""
        for linha in matriz:
            for coluna in linha:
                txt += f"{coluna}  "
            txt += '\n'
        # agora, resta salvar
        f = open(f'./resultado/texto_{nome}.txt', 'w')
        f.write(txt)
        f.close()

    # dada uma imagem, gera suas três matrizes R, G e B, na forma de imagem...
    def gerarMatrizesDeImagemPropria(C, imagem, qualIteracao, salvarCadaIteracao = False, salvarTxt = False):
        [R, G, B] = Imagem().matrizesRGBImagem(imagem)
        Desenho().desenharColorizado(R, G, B)

        R1 = AlgoritmoGeral().iterarMatriz(C, R, qualIteracao, salvarCadaIteracao, True)
        G1 = AlgoritmoGeral().iterarMatriz(C, G, qualIteracao, salvarCadaIteracao, True)
        B1 = AlgoritmoGeral().iterarMatriz(C, B, qualIteracao, salvarCadaIteracao, True)

        if salvarTxt:
            funcoesProntas().salvarEmTxt(R1[1][-1], 'r')
            funcoesProntas().salvarEmTxt(G1[1][-1], 'g')
            funcoesProntas().salvarEmTxt(B1[1][-1], 'b')


        Desenho().desenharColorizado(R1[1][-1], G1[1][-1], B1[1][-1])