from pontos import Ferramentas, Metodos, Salvar
from PIL import Image
from numpy import asarray

def imagemParaArray(imagem):

    # bota a imagem aí
    image = Image.open(imagem)

    # converte para array
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
                for k in range(j):
                    soma += k
                soma -= a
                soma /= 765
            # m.append(soma)
            matriz.append(soma)

    return matriz

# não recomendo que se rode esse programa para um n muito grande
# considerar n = 512 fará o computador travar depois de alguns minutos
# considerar n até 128 pode demorar mas roda
X = imagemParaArray('C:/Users/jpfre/Desktop/Modelagem-Matematica/Projeto-4/ideia/gato50.jpg')

# para calcular determinado feixe... primeiro vamos estabelecer os valores de configuração e essas coisas
### CONFIGURAÇÕES ###
percentualValor = 1

### VALORES DE ENTRADA ###
feixe = [1, 0] # equação do feixe
n = 50 # tamanho da tela n x n
t = 2 # tamanho do pixel
tamanhoFeixe = 2 # tamanho do feixe
ferr = Ferramentas(t, n, percentualValor)
met = Metodos(tamanhoFeixe, n, t, ferr)

# acho justo estabelecer que a quantidade Q de retas por direção seja igual a n, mas deixemos em aberto
Q = n

# Tendo calculado as retas, basta se decidir sobre qual método usar:
# 1 - Centro
# 2 - Reta Central
# 3 - Área
metodo = 1

retas = ferr.retasConformeDirecao(Q, [tamanhoFeixe, 0.00001, 100000])

# os elementos de A estarão em A[0]
A = []
for linha in retas:
    d = met.aConformeRetas(metodo, linha)
    for el in d[0]:
        A.append(el)
    

from b import calcularB
# calcula o b
b = calcularB(A, X)

for i in range(len(b)):
    if 0 <= i <= 2:
        print(f'Horizontal: {b[i]}')
    elif 3 <= i <= 5:
        print(f'Diagonal crescente: {b[i]}')
    elif 6 <= i <= 8:
        print(f'Vertical: {b[i]}')
    else:
        print(f'Diagonal decrescente: {b[i]}')

# se quiser calcular as equações...
# equacoes = met.escreverEquacoes(A, b)

def retornaB():
    global b
    return b

def retornaA():
    global A
    return A

txt = ""
# for eq in equacoes:
#     txt += f"{eq}\n"
for bi in b:
    txt += f"{bi}\n"
f = open('b.txt', 'w')
f.write(txt)
f.close()

print(f"\n{'*'*30}\n Anotado em b.txt")

