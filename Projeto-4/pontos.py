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


def minimo(f):
    [a, b] = f
    if b < 0:
        return [-b/a, 0]
    else:
        return [0, b]

# ponto de máximo, quem chega primeiro ao limite: x ou y?


def maximo(n, t, f):
    [a, b] = f
    maxy = a*n*t+b
    maxx = (n*t-b)/a

    # retornar o valor inserido e o valor calculado
    if maxy < maxx:
        return [n*t, maxy]
    else:
        return [maxx, n*t]

# captura os pontos em determinado intervalo


def intervalo(P, min, max):
    a = []
    for i in range(n):
        for j in range(n):
            if i+1 >= min[0] and i+1 <= max[0] and j+1 >= min[1] and j+1 <= max[1]:
                try:
                    a[i].append(P[i][j])
                except:
                    a.append([])
                    a[i].append(P[i][j])
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
    print(f'p: {p[0]}')
    print(f'lista: {x0m, x0n, y0m, y0n}')
    pontos = []
    if (p[0] - t/2 <= x0n <= p[0] + t/2) and len(pontos) < 2 and [round(x0n, 5), round(a*x0n+b, 5)] not in pontos:
        print('1')
        pontos.append([round(x0n, 5), round(a*x0n+b, 5)])
    if (p[0] - t/2 <= x0m <= p[0] + t/2) and len(pontos) < 2 and [round(x0m, 5), round(a*x0m+b, 5)] not in pontos:
        print('2')
        pontos.append([round(x0m, 5), round(a*x0m+b, 5)])
    if (p[1] - t/2 <= y0m <= p[1] + t/2) and len(pontos) < 2 and [round((y0m-b)/a, 5), round(y0m, 5)] not in pontos:
        print('3')
        pontos.append([round((y0m-b)/a, 5), round(y0m, 5)])
    if (p[1] - t/2 <= y0n <= p[1] + t/2) and len(pontos) < 2 and [round((y0n-b)/a, 5), round(y0n, 5)] not in pontos:
        print('4')
        pontos.append([round((y0n-b)/a, 5), round(y0n, 5)])
    return pontos

# calcula quais pixels são atravessados por um determinado feixe f, dado a grade de possíveis p, a quantidade n e o tamanho t dos pixels
def estaNoPontoP(f, p, n, t):
    P = intervalo(p, minimo([1.57, -0.12]), maximo(n, t, [1.57, -0.12]))
    listaPossiveis = []

    for linha in P:
        maximos = maximoY(linha[0][0]-t/2, t, f)
        [p0, p1] = maximos
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
    
    print(pontosProximos)
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
    print(f'g: {pts}\n')

    # verifica qual área deve ser calculada
    qual = qualArea(f, g, p, t)

    # verifica os pontos de intersecção da outra reta
    ptsOutra = ver(g, t, p)
    print(f'qual: {qual}')
    # se o qual tiver len 2 e 

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


f = [1.57, -.12] # equação do feixe
g = [1.57, -2.12]
n = 16 # tamanho da tela n x n
t = 2 # tamanho do pixel
p = pontos(n, t) # pixels da tela

# print(porcentagem(f, g, t, [3, 3]))
# print(retasSobreMesmoPixel(f, g, [1, 1], t))

pontosDeF = estaNoPontoP(f, p, n, t)
pontosDeG = estaNoPontoP(g, p, n, t)
st = ""

for po in pontosDeF:
    if po not in pontosDeG:
        porc = porcentagem(f, g, t, po)
        st += f"\n\n Ponto: {po} \n Funcao: {f} \n Porcentagem: {porc}"
        # print(f'\n\n Ponto: {po} \n Função: {f} \n Porcentagem: {porc}')
    else:
        print(f'\n\n\n f: {f} / g: {g} / po: {po}')
        porc = retasSobreMesmoPixel(f, g, po, t)
        st += f'\n\n Ponto: {po} \n Funcoes: {f} e {g} \n Porcentagem: {porc}'
        # print(f'\n\n Ponto: {po} \n Funções: {f} e {g} \n Porcentagem: {porc}')

for po in pontosDeG:
    if po not in pontosDeF:
        porc = porcentagem(g, f, t, po)
        st += f"\n\n Ponto: {po} \n Funcao: {g} \n Porcentagem: {porc}"
        # print(f'\n\n Ponto: {po} \n Função: {g} \n Porcentagem: {porc}')

c = open('./a/a.txt', 'w')
c.write(st)
c.close()

print('foi!')


# isso passa as coordenadas para serem plotadas no gnu
def plotNoGnu():
    txt = "# X Y\n"
    for pa in pontosDeG:
        txt += f"{pa[0]} {pa[1]}\n"
    for pa in pontosDeF:
        txt += f"{pa[0]} {pa[1]}\n"
    c = open('./a/dados.txt', 'w')
    c.write(txt)
    c.close()

    w = open('./a/retangulos.txt', 'w')
    txt = ""
    iterador = 1
    for linha in p:
        for pix in linha:
            txt += f"set object {iterador} rect from {pix[0]-t/2},{pix[1]-t/2} to {pix[0]+t/2},{pix[1]+t/2}\n"
            iterador += 1
    txt += f"replot {f[0]}*x+{f[1]}\nreplot {g[0]}*x+{g[1]}"
    w.write(txt)
    w.close()
plotNoGnu()

