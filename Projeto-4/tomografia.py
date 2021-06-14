import numpy as np
from numpy.core.fromnumeric import transpose
from matrizes import Matrizes
l = Matrizes()

class Tomografia:    

    def densidade(self, a, at, b, x0):

         #Ponto "aleatório" usado como ponto inicial
        x = [] 
        
        for k in range(50): # Estrutura de repetição para aumentar a precisão dos resultados

            x.clear() #Limpa a lista para que somente o ultimo resultado seja salvo

            for i in range(len(a)): # Estrutura de repetição que resolve o sistema de n icógnitas usando projeção ortogonal
                
                if(i == 0): # caso esteja na primeira repetição, o algorítmo usará o x0 no lugar do x[i-1]

                    aux = np.matmul(a[i], ( (b[i] - np.matmul(at[i], x0)) / (np.matmul(at[i], a[i]))) )
                    
                    aux = l.inverterLinha(aux)
                    
                    x.append(np.sum([x0, aux], axis=0))

                else:

                    aux = np.matmul(a[i], ( (b[i] - np.matmul(at[i], x[i-1])) / (np.matmul(at[i], a[i]))) )
                    
                    aux = l.inverterLinha(aux)

                    x.append(np.sum([x[i-1], aux], axis=0))

                if(i == (len(a)-1)):
                    x0 = x[i]

        return x    




