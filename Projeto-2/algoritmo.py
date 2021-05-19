# importar as bibliotecas
import math # Funções matemáticas
import matplotlib as mpl # Biblioteca que permite a impressão de gráficos
import numpy as np # Biblioteca que ajuda a trabalhar com grandes vetores
from matplotlib import pyplot as plt 

# O projeto é separado por funções, sedo main a função responsável por chamar as outras funções
# Variaveis globais que poderão ser acessadas de qualquer função
d = 10.81 * (10**7) # Distancia entre sol e Venus
D = 14.95 * (10**7) # Distancia entre Sol e Terra
k = 1 # Constante

def main():
    # Legenda do Menu
    print("Menu\n0 - Sair\n1 - Calcular o brilho em função de uma distancia em km pertencente ao intervalo [4.14 * 10^7 , 25.76 * 10^7] que o usuário digita \n2 - Descobrir qual é a distância r quando brilho é máximo e retorna um gráfico do brilho em função da distância r\n3 - Calcula p quando brilho é máximo\n4 - Calcula o brilho em função de um θ que o usuário digita\n5 - Descobrir qual o angulo θ quando brilho for máximo e retorna um gráfico do brilho em função do ângulo θ\n")

    # Aqui sera usado um lupe infinito para que o usuário possa usar o código diversas vezes sem precisar execuar novamente
    while True: 
        menu = int(input("Digte uma opção: "))
        if menu == 1:
            # Tratamento de dados para que o usuário só possa digitar um valor no intervalo
            while True:
                # A distância será multiplicada por 10^7 para facilitar o usuário a digitar no intervalo desejado
                r = float(input("Digite uma distância em km (ela vai ser multiplicada por 10^7): "))
                r = r * (10**7)
                if(r >= (D-d) and r <= (D+d)):
                        break
                print("Valores fora do intervalo, tente outro valor!")
            
            print("O brilho sera: ", (b(r) / maxb()) * 100, "% do bilho máximo")

        elif menu == 2:
            print("O brilho sera máximo na distancia r =", maxr()); 
        elif menu == 3:
            print("O briho será máximo quando p =", pmax())
        elif menu == 4:
            theta = float(input("Digite o valor de θ em graus: "))
            print("O brilho será: ", (btheta(theta) / maxb()) * 100, "% do brilho máximo")
        elif menu == 5:
            print("O brilho será máximo quando θ =", maxtheta(),"Radianos")
            graph2()
        elif menu == 0:
            break
        else:
            print("Opção inválida! ")

# Funções

# função que encontra o brilho em função de r
def b(r):
    B = k * (2*d*r + r**2 + d**2 - D**2) / (4 * d * r**3)

    return B

# função que encontra o r quando o brilho é máximo
def maxr():
    r = -2*d + math.sqrt(d**2 + 3 * (D**2))

    return r

# função que p quando brilho for máximo
def pmax():
    
    r = maxr() # Pegando o valor máxido de r para usar na fórmula
    p = (r**2 + d**2 + 2*d*r - D**2) / (4 * d * r)
    
    return p

# função que encontra o theta quando brilho é máximo
def maxtheta():
    r = maxr() # Pegando o valor máxido de r para usar na fórmula
    theta  = math.acos((d**2 + D**2 - r**2) / (2*d*D))
    return theta

def graph2():
    # parâmetro r vai receber 5000 valores entre D-d até D+d. Representa a distância da Terra a Vênus.
    r = np.linspace((D-d), (D+d), 5000)

    # as funções paramétricas
    theta = np.arccos((D**2 + d**2 - r**2)/(2*d*D))
    B = ((10**17)*(r**2 + d**2 + 2*d*r - D**2)/(4*d* r**3)) #multiplicamos por uma constante 10**17 apenas por conveniência dos valores de y no gráfico

    # plotar no gráfico
    plt.figure()
    plt.plot(theta, B)
    plt.xlabel('θ (rad)')
    plt.ylabel('Brilho')
    plt.show()

# Retorna o brilho em função do ângulo theta
def btheta(theta):
    theta = (theta * math.pi) / 180
    r = math.sqrt(D**2 + d**2 - 2 * D * d * math.cos(theta)) # converte o ang theta em uma distancia r por lei dos cossenos
    return b(r)

# Função de brilho máximo para auxiliar em contas
def maxb():
    r = maxr() # r recebe valor que maximiza o brilho
    return b(r)

# Chama a função Main depois de já ter lido todas as funções
main()

