# importar as bibliotecas
import matplotlib as mpl
import numpy as np
from matplotlib import pyplot as plt

# os valores de D e d
D = 14.95 * 10**7 # é a distância da Terra ao Sol
d = 10.81 * 10**7 # é a distância de Vênus ao Sol

# parâmetro r vai receber 5000 valores entre D-d até D+d. Representa a distância da Terra a Vênus.
r = np.linspace((D-d), (D+d), 5000)

# as funções paramétricas
theta = np.arccos((D**2 + d**2 - r**2)/(2*d*D))
B = ((10**17)*(r**2 + d**2 + 2*d*r - D**2)/(4*d* r**3)) #multiplicamos por uma constante 10**17 apenas por conveniência dos valores de y no gráfico

# plotar no gráfico
plt.figure()
plt. plot(theta, B)
plt.xlabel('∠VST (rad)')
plt.ylabel('Brilho')
plt.show()
