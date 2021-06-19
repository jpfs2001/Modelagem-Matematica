from tomografia import Tomografia
import numpy as np
from pontos import Ferramentas, Metodos

tomografia = Tomografia()
# ### CONFIGURAÇÕES ###
percentualValor = 1

# ### VALORES DE ENTRADA ###
feixe = [1, 0] # equação do feixe
n = 3 # tamanho da tela n x n
t = 2 # tamanho do pixel
tamanhoFeixe = 2 # tamanho do feixe

# ### INSTANCIAMENTO ###
ferr = Ferramentas(t, n, percentualValor)
met = Metodos(tamanhoFeixe, n, t, ferr)
retas = [[0.000001, 1], [0.0000001, 3], [0.000001, 5], [1, -3], [1, 0], [1, 3], [1000, -5000], [1000, -3000], [1000, -1000], [-1, 9], [-1, 6], [-1, 3]]
a = []

for r in retas:
    dados = met.metodoCentro(r)

    matrizTeste = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for dado in dados[0]:
        j = int((dado[1][0]-t/2)/t)
        i = int((n*t-dado[1][1]-t/2)/t)
        matrizTeste[i][j] = dado[2]

    matrizConvertida = []
    for linha in matrizTeste:
        for coluna in linha:
            matrizConvertida.append([coluna])

    a.append(matrizConvertida)
    
# a = np.array([
#     [[0], [0], [0], [0], [0], [0], [1], [1], [1]],
#     [[0], [0], [0], [1], [1], [1], [0], [0], [0]],
#     [[1], [1], [1], [0], [0], [0], [0], [0], [0]],
#     [[0], [0], [0], [0], [0], [1], [0], [1], [1]],
#     [[0], [0], [1], [0], [1], [0], [1], [0], [0]],
#     [[1], [1], [0], [1], [0], [0], [0], [0], [0]],
#     [[0], [0], [1], [0], [0], [1], [0], [0], [1]],
#     [[0], [1], [0], [0], [1], [0], [0], [1], [0]],
#     [[1], [0], [0], [1], [0], [0], [1], [0], [0]],
#     [[0], [1], [1], [0], [0], [1], [0], [0], [0]],
#     [[1], [0], [0], [0], [1], [0], [0], [0], [1]],
#     [[0], [0], [0], [1], [0], [0], [1], [1], [0]]
# ])



# for i in range(len(a)):
#     a[i] = np.asmatrix(a[i])
# for i in a:
#     print('a: ', i)

# print(a)
# i = (x-t/2)/t
# j = (nt-y-t/2)/t

b = np.array([
    13,
    15,
    8,
    14.79,
    14.31,
    3.81,
    18,
    12,
    6,
    10.51,
    16.13,
    7.04
])

x = tomografia.densidade(a, b)
print(x)