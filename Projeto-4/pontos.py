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
	return [[x0, y0],[x1, y1]]

# verifica em quais pontos de determinado pixel a reta passou
def ver(f, t, p):
	[a, b] = f
	#1
	x0m = (p[1]+t/2-b)/a
	x0n = (p[1]-t/2-b)/a
	y0m = a*(p[0]+t/2)+b
	y0n = a*(p[0]-t/2)+b
	pontos = []
	if (p[0] - t/2 <= x0n <= p[0] + t/2):
		pontos.append([x0n, a*x0n+b])
	if (p[0] - t/2 <= x0m <= p[0] + t/2):
		pontos.append([x0m, a*x0m+b])
	if (p[1] - t/2 <= y0m <= p[1] + t/2):
		pontos.append([(y0m-b)/a, y0m])
	if (p[1] - t/2 <= y0n <= p[1] + t/2):
		pontos.append([(y0n-b)/a, y0n])


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
    print(f'valor: {numerador/denominador}')
    return numerador/denominador

# calcula a distância entre duas retas quaisquer
def distanciaEntreRetas(f, g):
    a = -f[0]
    b = 1
    cf = -f[1]
    cg = -g[1]
    return abs(cf - cg)/((a**2+b**2)**0.5)

# calcula a distância entre dois pontos quaisquer
def distanciaEntrePontos(p1, p2):
    y = (p1[1]-p2[1])**2
    x = (p1[0]-p2[0])**2
    return (x+y)**0.5

# determina vértices do pixel que estão mais próximos da outra reta que da reta dita
def verticesProximos(f, g, p, t):
    distanciaFG = distanciaEntreRetas(f, g)
    
    pontosProximos = []
    # distância superior esquerda
    if distanciaPontoReta([p[0]-t/2, p[1]+t/2], g) <= distanciaFG: pontosProximos.append([p[0]-t/2, p[1]+t/2])
    # distância superior direita
    if distanciaPontoReta([p[0]+t/2, p[1]+t/2], g) <= distanciaFG: pontosProximos.append([p[0]+t/2, p[1]+t/2])
    # distância inferior esquerda
    if distanciaPontoReta([p[0]-t/2, p[1]-t/2], g) <= distanciaFG: pontosProximos.append([p[0]-t/2, p[1]-t/2])
    # distância inferior direita
    if distanciaPontoReta([p[0]+t/2, p[1]-t/2], g) <= distanciaFG: pontosProximos.append([p[0]+t/2, p[1]-t/2])
    print(f"distâncias: {distanciaPontoReta([p[0]+t/2, p[1]-t/2], g)} / {distanciaFG}")
    print(f"pontos próximos {[p[0], p[1]]}")
    return pontosProximos

# verifica qual seção de área deve ser considerada
def qualArea(f, g, p, t):
    pontosProximos = verticesProximos(f, g, p, t)
    # se for 1 ponto apenas, significa que é situação de triângulo, e consequentemente a menor área
    if len(pontosProximos) == 1:
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

#calcula a porcentagem da menor área que um feixe ocupa quando atravessa um pixel sobre a área do próprio pixel
def porcentagem(f, g, t, p):

    # se quiser mudar para o valor ficar decimal, bota 1. Se quiser percentual, bota 100
    percentualValor = 1
    pts = ver(f, t, p)

    # verifica qual área deve ser calculada
    qual = qualArea(f, g, p, t)
    if qual == t*t:
        return percentualValor
    print(pts)
    # atravessa horizontalmente
    if (pts[0][0]).is_integer() and (pts[1][0]).is_integer():
        print('horizontal')
        if pts[0][1] == qual[0][1]:
            dif = abs(pts[0][1]-qual[0][1]) + abs(pts[1][1]-qual[1][1])
        else:
            dif = abs(pts[0][1]-qual[1][1]) + abs(pts[1][1]-qual[0][1])
        areaDeBase = t*dif/2
        return percentualValor*areaDeBase/(t*t)
        
    elif (pts[0][1]).is_integer() and (pts[1][1]).is_integer() :
        print('vertical')
        if pts[0][0] == qual[0][0]:
            dif = abs(pts[0][0]-qual[0][0]) + abs(pts[1][0]-qual[1][0])
        else:
            dif = abs(pts[0][0]-qual[1][0]) + abs(pts[1][0]-qual[0][0])
        areaDeBase = t*dif/2
        return percentualValor*areaDeBase/(t*t)
    else:
        print('triangulo')
        # nesse caso, calcularemos o triângulo
        l1 = [pts[0][0], pts[0][1], 1]
        l2 = [pts[1][0], pts[1][1], 1]
        print(f"qual: {qual}")

        # para saber se queremos ele ou o restante, vemos se há 1 ou 3 elementos na lista
        if len(qual) == 1: #se se quiser o triângulo
            print('quer triangulo')
            pontoReferencia = qual[0]
            l3 = [pontoReferencia[0], pontoReferencia[1], 1]
            areaDeBase = abs(m.determinanteLU([l1, l2, l3])/2)
            return percentualValor*areaDeBase/(t*t)

        elif len(qual) == 3: # se se quiser o restante            
            print('não quer triangulo')
            # faz-se necessário verificar qual está faltando
            # usei o fato de que se algum deles não tem a diagonal na lista, então fica prático
            if distanciaEntrePontos(qual[0], qual[1]) == t*(2**0.5):
                #então o que falta é o que faz diagonal com o qual[2]
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
            areaDeBase = abs(m.determinanteLU([l1, l2, l3])/2)
            return percentualValor*(t*t-areaDeBase)/(t*t)

# calcula a área do compreendida quando as duas retas passam sobre o mesmo pixel juntas
def retasSobreMesmoPixel(f, g, p, t):
    percentualValor = 1

    areaDeInterseccao = porcentagem(f, g, t, p) + porcentagem(g, f, t, p) - percentualValor

    return areaDeInterseccao


f = [1.57, -.12] # equação do feixe
g = [1.57, -2.12]
n = 4 # tamanho da tela n x n
t = 2 # tamanho do pixel
p = pontos(n, t) # pixels da tela

# print(porcentagem(f, g, t, [3, 3]))
print(retasSobreMesmoPixel(f, g, [3, 3], t))