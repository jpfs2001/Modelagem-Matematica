from tomografia import Tomografia
import numpy as np
from pontos import Ferramentas, Metodos
from exibir import exibir

# inicializa a tomografia
tomografia = Tomografia()

### CONFIGURAÇÕES ###
percentualValor = 1

### VALORES DE ENTRADA ###
feixe = [1, 0] # equação do feixe
n = 3 # tamanho da tela n x n
t = 2 # tamanho do pixel
tamanhoFeixe = 2 # tamanho do feixe

### INSTANCIAMENTO ###
ferr = Ferramentas(t, n, percentualValor)
met = Metodos(tamanhoFeixe, n, t, ferr)

retas = [[0.000001, 1], [0.0000001, 3], [0.000001, 5], [1, -3], [1, 0], [1, 3], [100000, -500000], [100000, -300000], [100000, -100000], [-1, 9], [-1, 6], [-1, 3]]  

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
a = []

#### INÍCIO ####
ç = int(input("Escolha o método desejado para cálculo \n 1 - método do centro do pixel \n 2 - método da reta central \n 3 - método da área \n Digite a opção correspondente: "))    

# calcula os a
for r in retas:
    # conforme a opção, cálcula os dados com determinado método
    if ç == 1:
        dados = met.metodoCentro(r)
    elif ç == 2:
        dados = met.metodoRetaCentral(r)
    elif ç == 3:
        dados = met.metodoArea(r)

    # definição da matriz
    matrizTeste = []
    for l in range(n):
        lis = []
        for j in range(n):
            lis.append(0)
        matrizTeste.append(lis)

    # converte os dados para uma matriz propriamente dita
    for dado in dados[0]:
        j = int((dado[1][0]-t/2)/t)
        i = int((n*t-dado[1][1]-t/2)/t)
        matrizTeste[i][j] = dado[2]

    # conversão da matriz para o formato utilizado
    matrizConvertida = []
    for linha in matrizTeste:
        for coluna in linha:
            matrizConvertida.append([coluna])
    # adiciona na lista
    a.append(matrizConvertida)

met.escreverEquacoes(a, b)

# calcula os x
x = tomografia.densidade(a, b, True)
# os exibe
print(x)

# converte o resultado para uma matriz quadrada
matrizResultante = []
linha = []
for i in range(0, len(x)):
    linha.append(x[i].tolist()[0][0])
    if (i+1)%3==0:
        matrizResultante.append(linha)
        linha = []

# exibe a imagem formada pelos x calculados
exibir(matrizResultante)