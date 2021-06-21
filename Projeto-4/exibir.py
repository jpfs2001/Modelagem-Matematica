import numpy as np
import matplotlib.pyplot as plt

def matrizAleatoria(tamanho):
    matriz = []
    for i in range(tamanho):
        l = []  
        for j in range(tamanho):
            l.append(1-np.random.uniform())
        matriz.append(l)
    return matriz

def exibir(matriz):
    # plota usando a escala de cinza
    plt.imshow(matriz, aspect='auto', cmap="Greys")
    plt.axis('off')
    plt.show()

# exemplo de matriz aleatória de tamanho 100x100
# matriz = matrizAleatoria(100)
# exibir(matriz)