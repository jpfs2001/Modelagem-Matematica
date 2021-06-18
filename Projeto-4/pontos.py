import numpy as np
from matrizes import Matrizes
m = Matrizes()

class Ferramentas:
    def __init__(self, t, n, percentualValor):
        # se quiser mudar para o valor ficar decimal, bota 1. Se quiser percentual, bota 100
        self.percentualValor = percentualValor
        self.t = t
        self.n = n
    # pixels, dada uma quantidade e um intervalo
    def pontos(self):
        P = [0]*self.n

        for i in range(0, self.n):
            P[i] = [0]*self.n
            for j in range(0, self.n):
                P[i][j] = [
                    self.t*(2*(i+1)-1)//2,
                    self.t*(2*(j+1)-1)//2
                ]
        return P
    # ponto de mínimo
    def minimo(self, f):
        [a, b] = f
        if a > 0:
            if b < 0:
                return [-b/a, 0]
            else:
                return [0, b]
        else:
            # verifica primeiro se o mínimo cartesiano está dentro do escopo
            if 0 <= -b/a <= self.n*self.t:
                # o mínimo será quando a reta atravessar y = 0, então x = -b/a
                return [-b/a, 0]
            elif 0 <= a*self.n*self.t+b <= self.n*self.t:
                return [self.n*self.t, a*self.n*self.t+b]
    # ponto de máximo, quem chega primeiro ao limite: x ou y?
    def maximo(self, f):
        [a, b] = f
        if a > 0:
            maxy = a*self.n*self.t+b
            maxx = (self.n*self.t-b)/a
            # retornar o valor inserido e o valor calculado
            if maxy < maxx:
                return [self.n*self.t, maxy]
            else:
                return [maxx, self.n*self.t]

        elif a < 0:
            # o máximo será quando a reta atravessar o eixo y e estiver dentro do limite de pixels ou quando seu y for igual ao limite
            # no primeiro caso, x = 0 e b = y
            if 0 <= b <= self.n*self.t:
                return [0, b]
            # no segundo caso, y = n*t e x = (n*t-b)/a
            elif 0 <= self.n*self.t/a - b/a <= self.n*self.t:
                return [(self.n*self.t-b)/a, self.n*self.t]
    # captura os pontos em determinado intervalo
    def intervalo(self, min, max):
        a = []
        for i in range(1, 2*self.n, 2):
            for j in range(1, 2*self.n, 2):
                if (min[0] <= i-t/2 <= max[0] or min[0] >= i-t/2 >= max[0] or min[0] <= i+t/2 <= max[0] or min[0] >= i+t/2 >= max[0]) and (min[1] <= j-t/2 <= max[1] or min[1] >= j-t/2 >= max[1] or min[1] <= j+t/2 <= max[1] or min[1] >= j+t/2 >= max[1]):
                    try:
                        a[i].append([i, j])
                    except:
                        a.append([])
                        a[-1].append([i, j])
        return a
    # calcula os pontos de intersecção da reta com o pixel dado um valor inicial, o tamanho do pixel e a função
    def maximoY(self, i, f):
        [a, b] = f
        if a*i+b < 0:
            y0 = 0
            x0 = -b/a
        else:
            y0 = a*i+b
            x0 = i
        if a*(i+self.t)+b < 0:
            y1 = 0
            x1 = -b/a
        else:
            y1 = a*(i+self.t)+b
            x1 = i+self.t
        return [[x0, y0], [x1, y1]]
    # verifica em quais pontos de determinado pixel p de lado t a reta f passou
    def ver(self, f, p):
        [a, b] = f
        x0m = (p[1]+self.t/2-b)/a
        x0n = (p[1]-self.t/2-b)/a
        y0m = a*(p[0]+self.t/2)+b
        y0n = a*(p[0]-self.t/2)+b
        pontos = []
        if (p[0] - self.t/2 <= x0n <= p[0] + self.t/2) and len(pontos) < 2 and [round(x0n, 5), round(a*x0n+b, 5)] not in pontos:
            # print('1')
            pontos.append([round(x0n, 5), round(a*x0n+b, 5)])
        if (p[0] - self.t/2 <= x0m <= p[0] + self.t/2) and len(pontos) < 2 and [round(x0m, 5), round(a*x0m+b, 5)] not in pontos:
            # print('2')
            pontos.append([round(x0m, 5), round(a*x0m+b, 5)])
        if (p[1] - self.t/2 <= y0m <= p[1] + self.t/2) and len(pontos) < 2 and [round((y0m-b)/a, 5), round(y0m, 5)] not in pontos:
            # print('3')
            pontos.append([round((y0m-b)/a, 5), round(y0m, 5)])
        if (p[1] - self.t/2 <= y0n <= p[1] + self.t/2) and len(pontos) < 2 and [round((y0n-b)/a, 5), round(y0n, 5)] not in pontos:
            # print('4')
            pontos.append([round((y0n-b)/a, 5), round(y0n, 5)])

        return pontos
    # calcula quais pixels são atravessados por um determinado feixe f, dado a grade de possíveis p, a quantidade n e o tamanho t dos pixels
    def estaNoPontoP(self, f):
        # verifica se a reta é crescente ou decrescente
        if f[0] > 0:
            P = self.intervalo(self.minimo(f), self.maximo(f))
        else:
            P = self.intervalo(self.maximo(f), self.minimo(f))
        
        # lista onde serão armazenados os pixels atravessados
        listaPossiveis = []
        for linha in P:
            # variável que determina se deve-se verificar a condição do ponto ou não
            # a necessidade dela surge quando se tem coeficiente angular negativo, já que alguns pontos que estão no intervalo não são atravessados, embora outros da mesma linha sejam
            k = False
            # se o coeficiente angular for positivo, chama a função maximoY
            if f[0] > 0:
                [p0, p1] = self.maximoY(linha[0][0]-self.t/2, f)
                k = True
                
            for p in linha: 
                # se for negativo, chama a função ver
                if f[0] < 0:
                    try: self.ver(f, p)[1]
                    # se por algum motivo o ponto não tiver
                    except: pass
                    else: 
                        [p0, p1] = self.ver(f, p)           
                        k = True
                # verifica se o ponto é atravessado
                if k and p0[0]-self.t/2 <= p[0] <= p1[0]+self.t/2 and p0[1]-self.t/2 <= p[1] <= p1[1]+self.t/2 and p not in listaPossiveis: 
                    listaPossiveis.append(p)
            
        return listaPossiveis
    # calcula distancia entre um ponto qualquer e uma reta
    def distanciaPontoReta(self, ponto, f):
        # abs(ax+by+c)/sqrt(a^2+b^2)
        a = -f[0]
        b = 1
        c = -f[1]
        numerador = abs(a*ponto[0]+b*ponto[1]+c)
        denominador = (a**2 + b**2)**0.5
        return round(numerador/denominador, 5)
    # calcula a distância entre duas retas quaisquer
    def distanciaEntreRetas(self, f, g):
        # abs(c'-c)/sqrt(a^2+b^2)
        a = -f[0]
        b = 1
        cf = -f[1]
        cg = -g[1]
        return round(abs(cf - cg)/((a**2+b**2)**0.5), 5)
    # calcula a distância entre dois pontos quaisquer
    def distanciaEntrePontos(self, p1, p2):
        # sqrt((xb-xa)^2+(yb-ya)^2)

        y = (p1[1]-p2[1])**2
        x = (p1[0]-p2[0])**2
        return round((x+y)**0.5, 5)
    # determina vértices do pixel que estão mais próximos da outra reta que da reta dita
    def verticesProximos(self, f, g, p):
        # calcula a distância entre as retas
        distanciaFG = self.distanciaEntreRetas(f, g)
        # array onde serão armazenados os pontos próximos da segunda função
        pontosProximos = []
        # vértices do pixel
        vertices = [[p[0]-self.t/2, p[1]+self.t/2], [p[0]+self.t/2, p[1]+self.t/2], [p[0]-self.t/2, p[1]-self.t/2], [p[0]+self.t/2, p[1]-self.t/2]]
        
        # se houver algum vértice que seja atravessado pela segunda função
        try:
            vertices.index([p[0], round(g[0]*p[0]+g[1], 5)])
        except:
            # se não houver, verifica para cada vértice
            for vert in vertices:
                # se a distância entre a segunda função e o vértice for menor que a distância entre as retas ou a distância entre a segunda função e o vértice for menor que a distância entre o vértice e a primeira
                if self.distanciaPontoReta(vert, g) < distanciaFG or self.distanciaPontoReta(vert, g) < self.distanciaPontoReta(vert, f): 
                    pontosProximos.append(vert)
        else:
            # se houver, os outros são adicionados
            vertices.remove([p[0], f[0]*p[0]+f[1]])
            pontosProximos = vertices.copy()
        
        return pontosProximos
    # verifica qual seção de área deve ser considerada
    # é uma função mais "organizativa" que qualquer coisa, não tem muita serventia prática
    def qualArea(self, f, g, p):
        # calcula os pontos próximos
        pontosProximos = self.verticesProximos(f, g, p)

        # se for true, f está à esquerda. Se for false, f está à direita
        posicao = -f[1]/f[0] < -g[1]/g[0]

        # se tiver comprimento 1, podem ser dois casos:
        if len(pontosProximos) == 1:
            # caso em que não se passa pelo pixel
            if (pontosProximos[0] == [p[0]-self.t/2, p[1]-self.t/2] and posicao) or (pontosProximos[0] == [p[0]-self.t/2, p[1]+self.t/2] and posicao) or (pontosProximos[0] == [p[0]+self.t/2, p[1]-self.t/2] and not posicao) or (pontosProximos[0] == [p[0]+self.t/2, p[1]+self.t/2] and not posicao):
                return 0
            else:
                # situação de triângulo, e consequentemente a menor área
                return pontosProximos
        
        # se forem 2 pontos, é necessário retornar quais são eles, pois será um trapézio
        if len(pontosProximos) == 2:
            return pontosProximos

        # se forem 3 pontos, calcular a área do triângulo menor e a da forma maior com base nele, t*t - ele
        if len(pontosProximos) == 3:
            return pontosProximos

        # se forem 4 pontos, é o próprio pixel
        else: 
            return self.t*self.t
    # calcula a porcentagem da menor área que um feixe ocupa quando atravessa um pixel sobre a área do próprio pixel
    def porcentagem(self, f, g, p):
        # area de comparação
        areaDeComparacao = self.distanciaEntreRetas(f, g)*self.t

        pts = self.ver(f, p)

        # verifica qual área deve ser calculada
        qual = self.qualArea(f, g, p)

        # se for algum dos valores extremos excepcionais
        if qual == self.t**0.5:
            return self.percentualValor
        elif qual == 0:
            return 0
        
        # atravessa horizontalmente
        if len(pts) > 1 and len(qual) > 1 and ((pts[0][0] == p[0]-self.t/2 and pts[1][0] == p[0]+self.t/2) or (pts[1][0] == p[0]-self.t/2 and pts[0][0] == p[0]+self.t/2)):
            if pts[0][1] == qual[0][1]:
                dif = abs(pts[0][1]-qual[0][1]) + abs(pts[1][1]-qual[1][1])
            else:
                dif = abs(pts[0][1]-qual[1][1]) + abs(pts[1][1]-qual[0][1])
            areaDeBase = self.t*dif/2
            return self.percentualValor*areaDeBase/areaDeComparacao
        # atravessa verticalmente    
        elif len(pts) > 1 and len(qual) > 1 and ((pts[0][1] == p[1]-self.t/2 and pts[1][1] == p[1] + self.t/2) or (pts[1][1] == p[1]-self.t/2 and pts[0][1] == p[1] + self.t/2)):
            if pts[0][0] == qual[0][0]:
                dif = abs(pts[0][0]-qual[0][0]) + abs(pts[1][0]-qual[1][0])
            else:
                dif = abs(pts[0][0]-qual[1][0]) + abs(pts[1][0]-qual[0][0])
            areaDeBase = self.t*dif/2
            return self.percentualValor*areaDeBase/areaDeComparacao
        else:
            if len(pts) > 1:
                # nesse caso, calcularemos o triângulo
                l1 = [pts[0][0], pts[0][1], 1]
                l2 = [pts[1][0], pts[1][1], 1]
                
                # para saber se queremos ele ou o restante, vemos se há 1 ou 3 elementos na lista
                if len(qual) == 1: #se se quiser o triângulo
                    pontoReferencia = qual[0]
                    l3 = [pontoReferencia[0], pontoReferencia[1], 1]

                    areaDeBase = abs(np.linalg.det([l1, l2, l3])/2)

                    return self.percentualValor*areaDeBase/areaDeComparacao

                elif len(qual) == 3: # se se quiser o restante        
                    # faz-se necessário verificar qual está faltando
                    # usei o fato de que se algum deles não tem a diagonal na lista, então fica prático
                    if self.distanciaEntrePontos(qual[0], qual[1]) == self.t*(2**0.5):
                        # então o que falta é o que faz diagonal com o qual[2]
                        p1 = qual[2]
                    elif self.distanciaEntrePontos(qual[0], qual[2]) == self.t*(2**0.5):
                        # então o que falta é o que faz diagonal com o qual[1]
                        p1 = qual[1]
                    else:
                        # o que falta é o que faz diagonal com o qual[0]
                        p1 = qual[0]
                    
                    pontoFaltante = [0, 0]
                    if p1[0] > p[0]: pontoFaltante[0] = p[0]-self.t/2
                    else: pontoFaltante[0] = p[0]+t/2
                    if p1[1] > p[1]: pontoFaltante[1] = p[1]-self.t/2
                    else: pontoFaltante[1] = p[1]+t/2

                    l3 = [pontoFaltante[0], pontoFaltante[1], 1]
                    areaDeBase = abs(np.linalg.det([l1, l2, l3])/2)
                    
                    return self.percentualValor*((self.t**0.5)-areaDeBase)/areaDeComparacao
            else: 
                # no caso de se haver somente um ponto, é calculado o triângulo formado para a outra função
                ptsG = self.ver(g, p)
                l1 = [ptsG[0][0], ptsG[0][1], 1]
                l2 = [ptsG[1][0], ptsG[1][1], 1]
                l3 = [pts[0][0], pts[0][1], 1]
                areaDeBase = abs(np.linalg.det([l1, l2, l3])/2)
                return self.percentualValor*areaDeBase/areaDeComparacao
    # calcula a área do compreendida quando as duas retas passam sobre o mesmo pixel juntas
    def retasSobreMesmoPixel(self, f, g, p):
        # calcula os valores separadamente e remove o total, de modo que o restante é a intersecção entre ambos
        areaDeInterseccao = self.porcentagem(f, g, p) + self.porcentagem(g, f, p) - self.percentualValor
        return areaDeInterseccao

class Salvar:
    def armazenarEmTxt(self, dados, arquivo):
        txt = ""
        for dado in dados:
            txt += f"Funcao(oes): {dado[0]}\n"
            txt += f"Pixel: {dado[1]}\n"
            txt += f"Coeficiente: {dado[2]}\n\n"
        arq = open(arquivo, 'w')
        arq.write(txt)
        arq.close()
    # isso passa as coordenadas para um txt no formato do GNUplot
    # não é essencial, só serve para visualizar algumas coisas
    def plotNoGnu(self, dados, p, t, funcoes):
        # plota os pontos atravessados
        txt = "# X Y\n"
        for pa in dados:
            txt += f"{pa[0]} {pa[1]}\n"
        aDados = open('./a/dados.txt', 'w')
        aDados.write(txt)
        aDados.close()

        # plota os pixels na tela
        arqRetangulos = open('./a/retangulos.txt', 'w')
        txt = ""
        iterador = 1
        for linha in p:
            for pix in linha:
                txt += f"set object {iterador} rect from {pix[0]-t/2},{pix[1]-t/2} to {pix[0]+t/2},{pix[1]+t/2}\n"
                iterador += 1
        
        # plota as funções
        for i in range(len(funcoes)):
            funcao = funcoes[i]
            re = ""
            if i >= 1:
                re = "re"
            txt += f"{re}plot {funcao[0]}*x+{funcao[1]}\n"

        # plota os dados.txt
        txt += f'replot "dados.txt"'

        # salva
        arqRetangulos.write(txt)
        arqRetangulos.close()

class Metodos:
    def __init__(self, tamanhoFeixe,  n, t, ferr):
        self.Ferr = ferr # ferramentas instanciadas
        self.tamanhoFeixe = tamanhoFeixe
        self.n = n
        self.t = t
          
    # método do centro, onde o centro do pixel está contido no intervalo entre f e g
    def metodoCentro(self, funcaoInicial):
        [a, b] = funcaoInicial
        f = [a, b+(self.tamanhoFeixe/2)*(a*a+1)**0.5]
        g = [a, b-(self.tamanhoFeixe/2)*(a*a+1)**0.5]

        pontosDeF = self.Ferr.estaNoPontoP(f)
        pontosDeG = self.Ferr.estaNoPontoP(g)
        dados = []

        for p in pontosDeF+pontosDeG:
            # verifica quem passou nesse ponto
            if p in pontosDeF and pontosDeG: funcoesConsideradas = [f, g]
            elif p in pontosDeF: funcoesConsideradas = [f]
            else: funcoesConsideradas = [g]

            # ordena os pontos para saber quem está no meio, tanto em x quanto em y
            listY = [f[0]*p[0]+f[1], p[1], g[0]*p[0]+g[1]] # axp+bf, yp, axp+bg
            listY.sort()
            listX = [p[1]-f[1], p[0]*f[0], p[1]-g[1]] # yp-bf, xp*a, yp-bg
            listX.sort()
            # se o ponto central do pixel não estiver entre F e G, a = 0
            if listX[1]!=p[0] and listY[1]!=p[1]: valor = 0
            # se estiver, a = 1
            else: valor = 1

            # se o ponto não estiver na lista já adicionado anteriormente
            if [funcoesConsideradas, p, valor] not in dados:
                dados.append([funcoesConsideradas, p, valor])

        return [dados, [pontosDeF+pontosDeG, [f, g]]]
        
    # método onde a reta central atravessa um determinado pixel e a = (comprimento da reta que atravessou o pixel)/(t)
    def metodoRetaCentral(self, funcaoInicial):
        pontosFuncao = self.Ferr.estaNoPontoP(funcaoInicial)
        dados = []
        for p in pontosFuncao:
            pts = self.Ferr.ver(funcaoInicial, p)
            # se atravessar o vértice de um pixel
            if len(pts) == 1:
                dist = 0
            else:
                dist = self.Ferr.distanciaEntrePontos(pts[0], pts[1])
        
            dados.append([
                [funcaoInicial], # função que atravessou o pixel
                p, # pixel atravessado
                dist/self.t
            ])

        return [dados, [pontosFuncao, [funcaoInicial]]]

    # método da área, onde o pixel atravessado por alguma parte do feixe tem a = (área atravessada)/(área atravessada por um feixe horizontal)
    # para não ter o trabalho de simular, já que o pixel é necessariamente um quadrado (pelo menos nesse caso), considerei essa área como t*tamanhoFeixe, já que é um retângulo de lados t e tamanhoFeixe
    def metodoArea(self, funcaoInicial):

        # se for maior que t*sqrt(2), utilizar iterações
        # caso em que o tamanho do feixe não supera t*sqrt(2)
        [a, b] = funcaoInicial
        f = [a, b+(self.tamanhoFeixe/2)*(a*a+1)**0.5]
        g = [a, b-(self.tamanhoFeixe/2)*(a*a+1)**0.5]
        # captura os pixels os quais as retas passam
        pontosDeF = self.Ferr.estaNoPontoP(f)
        pontosDeG = self.Ferr.estaNoPontoP(g)

        # onde os dados serão guardados
        dados = []

        # calcula para os pontos de F e F inter G
        for pix in pontosDeF:
            # se g não tiver atravessado ele
            if pix not in pontosDeG:
                # calcula a porcentagem da área
                porc = self.Ferr.porcentagem(f, g, pix)
                # adiciona a lista de dados
                dados.append([
                    [f], # função
                    pix, # pixel calculado
                    porc # porcentagem
                ])
            # se g tiver atravessado
            else:
                # elimina de G para agilizar na hora de calcular somente os pixels de G
                pontosDeG.remove(pix)
                # calcula a porcentagem
                porc = self.Ferr.retasSobreMesmoPixel(f, g, pix)
                dados.append([
                    [f, g], # função
                    pix, # pixel calculado
                    porc # porcentagem
                ])
        # calcula para os pontos de G
        for pix in pontosDeG:
            # calcula a porcentagem
            porc = self.Ferr.porcentagem(g, f, pix)
            dados.append([
                [g], # função
                pix, # pixel calculado
                porc # porcentagem
            ])

        informacoesGNU = [pontosDeF+pontosDeG, [f, g]]
        
        return [dados, informacoesGNU]
 




########################### ENTRADA ##################################

### CONFIGURAÇÕES ###
percentualValor = 1

### VALORES DE ENTRADA ###
feixe = [-1.57, 26.12] # equação do feixe
n = 16 # tamanho da tela n x n
t = 2 # tamanho do pixel
tamanhoFeixe = 1.0744461230854325 # tamanho do feixe

### INSTANCIAMENTO ###
ferr = Ferramentas(t, n, 1)
met = Metodos(tamanhoFeixe, n, t, ferr)
salvar = Salvar()

### CHAMAMENTO ###
d = met.metodoCentro(feixe)
salvar.armazenarEmTxt(d[0], './a/a.txt')
salvar.plotNoGnu(d[1][0], ferr.pontos(), t, d[1][1])

# d = met.simularParaFeixe(feixe)
# salvar.armazenarEmTxt(d[0], './a/a.txt')
# p = ferr.pontos() # pixels da tela
# salvar.plotNoGnu(d[1][0], p, t, d[1][1])

################### ALGUMAS SIMULAÇÕES DE TESTE #######################
# simulações
# dados1 = simularParaFeixe(feixe, tamanhoFeixe, n, t)
# dados2 = simularParaFeixe([-1.57, 15.75], tamanhoFeixe, n, t)
# dados3 = simularParaFeixe([-1.57, 26.75], tamanhoFeixe, n, t)

# dados das simulações
# dados1Simulacao = dados1[0]
# dados2Simulacao = dados2[0]
# dados3Simulacao = dados3[0]
# informações para o GNUplot
# gnu1 = dados1[1]
# gnu2 = dados2[1]
# gnu3 = dados3[1]
# armazena em txt
# armazenarEmTxt(dados1Simulacao+dados2Simulacao+dados3Simulacao, './a/a.txt')
# armazena nos txt para o GNU
# plotNoGnu(gnu1[0]+gnu2[0]+gnu3[0], p, t, gnu1[1]+gnu2[1]+gnu3[1])

print('foi!')