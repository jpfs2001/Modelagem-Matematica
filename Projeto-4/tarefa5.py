from acharb import retornaB, retornaA
from tomografia import Tomografia
from exibir import exibir


t = Tomografia()

b = retornaB()
a = retornaA()

x = t.densidade(a, b, 1)

# converte o resultado para uma matriz quadrada
matrizResultante = []
linha = []
for i in range(0, len(x)):
    linha.append(x[i].tolist()[0][0])
    if (i+1)%80==0:
        matrizResultante.append(linha)
        linha = []

# exibe a imagem formada pelos x calculados
exibir(matrizResultante)