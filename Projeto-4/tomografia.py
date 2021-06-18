import numpy as np
from numpy.core.fromnumeric import transpose
from matrizes import Matrizes
l = Matrizes()

class Tomografia:    

    def densidade(self, a, b):

        # Cria uma variável x0, que será o ponto inicial.

        x0 = []

        for i in range(len(a[0])): 
            x0.append([0])
        
        # Execução da fórmula apresentada no artigo
        
        x = [] 

        for k in range(50): # Estrutura de repetição para aumentar a precisão dos resultados

            x.clear() # Limpa a lista para que somente o ultimo resultado seja salvo

            for i in range(len(a)): # Estrutura de repetição que resolve o sistema de n icógnitas e m equações usando projeção ortogonal
                
                # Conversão das listas para matrizes numpy
                
                x0 = np.asmatrix(x0)
                a[i] = np.matrix(a[i])          

                if(i == 0): # caso esteja na primeira repetição, o algorítmo usará o x0 no lugar do x[i-1]

                    aux = x0 + a[i] * ( (b[i]-(np.transpose(a[i]) * x0)) / (np.transpose(a[i]) * np.asmatrix(a[i]) ) )  
                    x.append(aux)

                else:

                    aux = x[i-1] + a[i] * ( (b[i]-(np.transpose(a[i]) * x[i-1])) / (np.transpose(a[i]) * np.asmatrix(a[i]) ) )  
                    x.append(aux)

                if(i == (len(a)-1)):
                    x0 = x[i]


        # Transformando em uma fração e retornando o resultado x onde k = 12 e p = 50
        tamanho = len(x)-1

        x = x[tamanho]
        
        max = np.matrix.max(x)
        
        for i in range(len(x)):
            x[i] = x[i]/max

        return x





