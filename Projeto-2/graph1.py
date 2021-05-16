# importar as bibliotecas
import matplotlib as mpl
import numpy as np
from matplotlib import pyplot as plt

# os valores de D e d
D = 14.95 * 10**7 # é a distância da Terra ao Sol
d = 10.81 * 10**7 # é a distância de Vênus ao Sol

# parâmetro r vai receber 1000 valores entre D-d até D+d. Representa a distância da Terra a Vênus.
r = np.linspace((D-d), (D+d), 1000)

# as funções paramétricas
theta = np.arccos((D**2 + d**2 - r**2)/(2*d*D))
B = ((r**2 + d**2 + 2*d*r - D**2)/(4*d* r**3))

# plotar no gráfico
plt.figure()
plt. plot(theta, B)
plt.show()
