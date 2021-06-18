import numpy as np
from matrizes import Matrizes
m = Matrizes()

# pixels, dada uma quantidade e um intervalo
def pontos(n, t):
    P = [0]*n

    for i in range(0, n):
        P[i] = [0]*n
        for j in range(0, n):
            P[i][j] = [
                t*(2*(i+1)-1)//2,
                t*(2*(j+1)-1)//2
            ]
    return P

# ponto de mínimo
def minimo(f, n, t):
    [a, b] = f
    if a > 0:
        if b < 0:
            return [-b/a, 0]
        else:
            return [0, b]
    else:
        # verifica primeiro se o mínimo cartesiano está dentro do escopo
        if 0 <= -b/a <= n*t:
            # o mínimo será quando a reta atravessar y = 0, então x = -b/a
            return [-b/a, 0]
        elif 0 <= a*n*t+b <= n*t:
            return [n*t, a*n*t+b]

# ponto de máximo, quem chega primeiro ao limite: x ou y?
def maximo(n, t, f):
    [a, b] = f
    if a > 0:
        maxy = a*n*t+b
        maxx = (n*t-b)/a
        # retornar o valor inserido e o valor calculado
        if maxy < maxx:
            return [n*t, maxy]
        else:
            return [maxx, n*t]

    elif a < 0:
        # o máximo será quando a reta atravessar o eixo y e estiver dentro do limite de pixels ou quando seu y for igual ao limite
        # no primeiro caso, x = 0 e b = y
        if 0 <= b <= n*t:
            return [0, b]
        # no segundo caso, y = n*t e x = (n*t-b)/a
        elif 0 <= n*t/a - b/a <= n*t:
            return [(n*t-b)/a, n*t]



# captura os pontos em determinado intervalo
def intervalo(n, min, max):
    a = []
    for i in range(1, 2*n, 2):
        for j in range(1, 2*n, 2):
            if (min[0] <= i <= max[0] or min[0] >= i >= max[0]) and (min[1] <= j <= max[1] or min[1] >= j >= max[1]):
                try:
                    a[i].append([i, j])
                except:
                    a.append([])
                    a[-1].append([i, j])
    return a

# calcula os pontos de intersecção da reta com o pixel dado um valor inicial, o tamanho do pixel e a função
def maximoY(i, t, f):
	[a, b] = f
	if a*i+b < 0:
		y0 = 0
		x0 = -b/a
	else:
		y0 = a*i+b
		x0 = i
	if a*(i+t)+b < 0:
		y1 = 0
		x1 = -b/a
	else:
		y1 = a*(i+t)+b
		x1 = i+t
	return [[x0, y0], [x1, y1]]

# verifica em quais pontos de determinado pixel a reta passou
def ver(f, t, p):
    [a, b] = f
    x0m = (p[1]+t/2-b)/a
    x0n = (p[1]-t/2-b)/a
    y0m = a*(p[0]+t/2)+b
    y0n = a*(p[0]-t/2)+b
    pontos = []
    if (p[0] - t/2 <= x0n <= p[0] + t/2) and len(pontos) < 2 and [round(x0n, 5), round(a*x0n+b, 5)] not in pontos:
        # print('1')
        pontos.append([round(x0n, 5), round(a*x0n+b, 5)])
    if (p[0] - t/2 <= x0m <= p[0] + t/2) and len(pontos) < 2 and [round(x0m, 5), round(a*x0m+b, 5)] not in pontos:
        # print('2')
        pontos.append([round(x0m, 5), round(a*x0m+b, 5)])
    if (p[1] - t/2 <= y0m <= p[1] + t/2) and len(pontos) < 2 and [round((y0m-b)/a, 5), round(y0m, 5)] not in pontos:
        # print('3')
        pontos.append([round((y0m-b)/a, 5), round(y0m, 5)])
    if (p[1] - t/2 <= y0n <= p[1] + t/2) and len(pontos) < 2 and [round((y0n-b)/a, 5), round(y0n, 5)] not in pontos:
        # print('4')
        pontos.append([round((y0n-b)/a, 5), round(y0n, 5)])
    return pontos

# calcula quais pixels são atravessados por um determinado feixe f, dado a grade de possíveis p, a quantidade n e o tamanho t dos pixels
def estaNoPontoP(f, p, n, t):

    if f[0] > 0:
        P = intervalo(n, minimo(f, n, t), maximo(n, t, f))
    else:
        P = intervalo(n, maximo(n, t, f), minimo(f, n, t))
        
    listaPossiveis = []
    for linha in P:
        if f[0] > 0:
            [p0, p1] = maximoY(linha[0][0]-t/2, t, f)
        else:
            [p0, p1] = ver(f, t, linha[0])            

        for p in linha: 
            if p0[0]-t/2 <= p[0] <= p1[0]+t/2 and p0[1]-t/2 <= p[1] <= p1[1]+t/2 and p not in listaPossiveis: 
                listaPossiveis.append(p)
          
    return listaPossiveis

def lado(f, g):
    # se f estiver à esquerda, sua raiz deve ser menor que a raiz de g
    if -f[1]/f[0] < -g[1]/g[0]:
        return 0
    # se g estiver à esquerda, vale a mesma coisa
    elif -g[1]/g[0] < -f[1]/f[0]:
        return 1

# calcula distancia entre um ponto qualquer e uma reta
def distanciaPontoReta(ponto, f):
    a = -f[0]
    b = 1
    c = -f[1]
    numerador = abs(a*ponto[0]+b*ponto[1]+c)
    denominador = (a**2 + b**2)**0.5
    return round(numerador/denominador, 5)

# calcula a distância entre duas retas quaisquer
def distanciaEntreRetas(f, g):
    a = -f[0]
    b = 1
    cf = -f[1]
    cg = -g[1]
    return round(abs(cf - cg)/((a**2+b**2)**0.5), 5)

# calcula a distância entre dois pontos quaisquer
def distanciaEntrePontos(p1, p2):
    y = (p1[1]-p2[1])**2
    x = (p1[0]-p2[0])**2
    return round((x+y)**0.5, 5)

# determina vértices do pixel que estão mais próximos da outra reta que da reta dita
def verticesProximos(f, g, p, t):
    distanciaFG = distanciaEntreRetas(f, g)
    pontosProximos = []
    vertices = [[p[0]-t/2, p[1]+t/2], [p[0]+t/2, p[1]+t/2], [p[0]-t/2, p[1]-t/2], [p[0]+t/2, p[1]-t/2]]
    
    try:
        vertices.index([p[0], round(g[0]*p[0]+g[1], 5)])
    except:
        for vert in vertices:
            if distanciaPontoReta(vert, g) < distanciaFG or distanciaPontoReta(vert, g) < distanciaPontoReta(vert, f): 
                pontosProximos.append(vert)
    else:
        vertices.remove([p[0], f[0]*p[0]+f[1]])
        pontosProximos = vertices.copy()
    
    return pontosProximos

# verifica qual seção de área deve ser considerada
def qualArea(f, g, p, t):
    pontosProximos = verticesProximos(f, g, p, t)

    # se for true, f está à esquerda. Se for false, f está à direita
    posicao = -f[1]/f[0] < -g[1]/g[0]

    if len(pontosProximos) == 1:
        if (pontosProximos[0] == [p[0]-t/2, p[1]-t/2] and posicao) or (pontosProximos[0] == [p[0]-t/2, p[1]+t/2] and posicao) or (pontosProximos[0] == [p[0]+t/2, p[1]-t/2] and not posicao) or (pontosProximos[0] == [p[0]+t/2, p[1]+t/2] and not posicao):
            return 0
        else:
            # se for 1 ponto apenas, significa que é situação de triângulo, e consequentemente a menor área
            return pontosProximos
    
    # se forem 2 pontos, é necessário retornar quais são eles
    if len(pontosProximos) == 2:
        return pontosProximos

    # se forem 3 pontos, calcular a área do triângulo menor e a da forma maior com base nele, t*t - ele
    if len(pontosProximos) == 3:
        return pontosProximos

    # se forem 4 pontos, é o próprio pixel
    else: 
        return t*t

# calcula a porcentagem da menor área que um feixe ocupa quando atravessa um pixel sobre a área do próprio pixel
def porcentagem(f, g, t, p):

    # se quiser mudar para o valor ficar decimal, bota 1. Se quiser percentual, bota 100
    percentualValor = 1
    pts = ver(f, t, p)

    # verifica qual área deve ser calculada
    qual = qualArea(f, g, p, t)

    if qual == t*t:
        return percentualValor
    elif qual == 0:
        return 0
    
    # atravessa horizontalmente
    if len(pts) > 1 and len(qual) > 1 and ((pts[0][0] == p[0]-t/2 and pts[1][0] == p[0]+t/2) or (pts[1][0] == p[0]-t/2 and pts[0][0] == p[0]+t/2)):
        if pts[0][1] == qual[0][1]:
            dif = abs(pts[0][1]-qual[0][1]) + abs(pts[1][1]-qual[1][1])
        else:
            dif = abs(pts[0][1]-qual[1][1]) + abs(pts[1][1]-qual[0][1])
        areaDeBase = t*dif/2
        return percentualValor*areaDeBase/(t*t)

    # atravessa verticalmente    
    elif len(pts) > 1 and len(qual) > 1 and ((pts[0][1] == p[1]-t/2 and pts[1][1] == p[1] + t/2) or (pts[1][1] == p[1]-t/2 and pts[0][1] == p[1] + t/2)):
        if pts[0][0] == qual[0][0]:
            dif = abs(pts[0][0]-qual[0][0]) + abs(pts[1][0]-qual[1][0])
        else:
            dif = abs(pts[0][0]-qual[1][0]) + abs(pts[1][0]-qual[0][0])
        areaDeBase = t*dif/2
        return percentualValor*areaDeBase/(t*t)
    else:
        if len(pts) > 1:
            # nesse caso, calcularemos o triângulo
            l1 = [pts[0][0], pts[0][1], 1]
            l2 = [pts[1][0], pts[1][1], 1]
            
            # para saber se queremos ele ou o restante, vemos se há 1 ou 3 elementos na lista
            if len(qual) == 1: #se se quiser o triângulo
                pontoReferencia = qual[0]
                l3 = [pontoReferencia[0], pontoReferencia[1], 1]
                # areaDeBase = abs(m.determinanteLU([l1, l2, l3])/2)
                areaDeBase = abs(np.linalg.det([l1, l2, l3])/2)
                return percentualValor*areaDeBase/(t*t)

            elif len(qual) == 3: # se se quiser o restante        
                # faz-se necessário verificar qual está faltando
                # usei o fato de que se algum deles não tem a diagonal na lista, então fica prático
                if distanciaEntrePontos(qual[0], qual[1]) == t*(2**0.5):
                    # então o que falta é o que faz diagonal com o qual[2]
                    p1 = qual[2]
                elif distanciaEntrePontos(qual[0], qual[2]) == t*(2**0.5):
                    # então o que falta é o que faz diagonal com o qual[1]
                    p1 = qual[1]
                else:
                    # o que falta é o que faz diagonal com o qual[0]
                    p1 = qual[0]
                
                pontoFaltante = [0, 0]
                if p1[0] > p[0]: pontoFaltante[0] = p[0]-t/2
                else: pontoFaltante[0] = p[0]+t/2
                if p1[1] > p[1]: pontoFaltante[1] = p[1]-t/2
                else: pontoFaltante[1] = p[1]+t/2

                l3 = [pontoFaltante[0], pontoFaltante[1], 1]
                # areaDeBase = abs(m.determinanteLU([l1, l2, l3])/2)
                areaDeBase = abs(np.linalg.det([l1, l2, l3])/2)
                

                return percentualValor*(t*t-areaDeBase)/(t*t)
        else: 
            ptsG = ver(g, t, p)
            l1 = [ptsG[0][0], ptsG[0][1], 1]
            l2 = [ptsG[1][0], ptsG[1][1], 1]
            l3 = [pts[0][0], pts[0][1], 1]
            areaDeBase = abs(np.linalg.det([l1, l2, l3])/2)
            return percentualValor*areaDeBase/(t*t)

# calcula a área do compreendida quando as duas retas passam sobre o mesmo pixel juntas
def retasSobreMesmoPixel(f, g, p, t):
    percentualValor = 1

    areaDeInterseccao = porcentagem(f, g, t, p) + porcentagem(g, f, t, p) - percentualValor
    return areaDeInterseccao

# isso passa as coordenadas para um txt no formato do GNUplot
def plotNoGnu(dados, p, t, funcoes):
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

def simularParaFeixe(funcaoInicial, tamanhoFeixe, n, t, p, salvarGNU):

    # se for maior que t*sqrt(2), utilizar iterações
    # caso em que o tamanho do feixe não supera t*sqrt(2)
    [a, b] = funcaoInicial
    f = [a, b+(tamanhoFeixe/2)*(a*a+1)**0.5]
    g = [a, b-(tamanhoFeixe/2)*(a*a+1)**0.5]

    # captura os pixels os quais as retas passam
    pontosDeF = estaNoPontoP(f, p, n, t)
    pontosDeG = estaNoPontoP(g, p, n, t)

    # se quiser salvar no formato GNU
    if salvarGNU:
        plotNoGnu(pontosDeF + pontosDeG, p, t, [f, g])

    # onde os dados serão guardados
    dados = []

    # calcula para os pontos de F e F inter G
    for pix in pontosDeF:
        # se g não tiver atravessado ele
        if pix not in pontosDeG:
            # calcula a porcentagem da área
            porc = porcentagem(f, g, t, pix)
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
            porc = retasSobreMesmoPixel(f, g, pix, t)
            dados.append([
                [f, g], # função
                pix, # pixel calculado
                porc # porcentagem
            ])
    # calcula para os pontos de G
    for pix in pontosDeG:
        # calcula a porcentagem
        porc = porcentagem(g, f , t, pix)
        dados.append([
            [g], # função
            pix, # pixel calculado
            porc # porcentagem
        ])
    
    return dados

def armazenarEmTxt(dados, arquivo):
    txt = ""
    for dado in dados:
        txt += f"Funcao(oes): {dado[0]}\n"
        txt += f"Pixel: {dado[1]}\n"
        txt += f"Coeficiente: {dado[2]}\n\n"
    arq = open(arquivo, 'w')
    arq.write(txt)
    arq.close()

feixe = [.01, 5.12] # equação do feixe
n = 16 # tamanho da tela n x n
t = 2 # tamanho do pixel
p = pontos(n, t) # pixels da tela

tamanhoFeixe = 1.0744461230854325

armazenarEmTxt(simularParaFeixe(feixe, tamanhoFeixe, n, t, p, True), './a/a.txt')


print('foi!')


