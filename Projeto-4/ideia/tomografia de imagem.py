from PIL import Image
from numpy import asarray
import matplotlib.pyplot as plt



# bota a imagem aí
image = Image.open('./ideia/1234.png')

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
            for k in j:
                soma += k
            soma -= a
            soma /= 765
        m.append(soma)
    matriz.append(m)

def exibir(matriz):
    # plota usando a escala de cinza
    plt.imshow(matriz, aspect='auto', cmap="Greys")
    plt.axis('off')
    plt.show()

# exibe a matriz usando a função do exibir.py la
exibir(matriz)