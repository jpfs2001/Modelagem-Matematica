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
    print("Menu\n0 - Sair\n1 - Calcular o brilho em função da distância r entre a Terra e Vênus. \n2 - Descobrir qual é a distância r quando o brilho é máximo e abrir o gráfico do brilho em função de r.\n3 - Calcular o brilho em função do ângulo θ entre Terra, Sol e Vênus. \n4 - Descobrir qual o ângulo θ quando brilho for máximo e abrir o gráfico do brilho em função de θ. \n5 - Calcular p quando brilho é máximo. \n")

    # Aqui sera usado um lupe infinito para que o usuário possa usar o código diversas vezes sem precisar execuar novamente
    while True: 
        menu = int(input("Digte uma opção: "))
        if menu == 1:
            # Tratamento de dados para que o usuário só possa digitar um valor no intervalo
            while True:
                # A distância será multiplicada por 10^6 para facilitar o usuário a digitar no intervalo desejado
                r = float(input("Digite uma distância em milhões de km (entre 41.4 e 257.6): "))
                r = r * (10**6)
                if(r >= (D-d) and r <= (D+d)):
                        break
                print("Valores fora do intervalo, tente outro valor!")
            
            print("O brilho será: ", (b(r) / maxb()) * 100, "% do bilho máximo.")

        elif menu == 2:
            print("O brilho será máximo na distância r =", maxr()/ 10**6, "milhões de km.")
            graph1() 
        elif menu == 3:
            theta = float(input("Digite o valor de θ em graus: "))
            print("O brilho será: ", (btheta(theta) / maxb()) * 100, "% do brilho máximo.")
        elif menu == 4:
            print("O brilho será máximo quando θ =", maxtheta(),"º.")
            graph2()
        elif menu == 5:
            print("O briho será máximo quando p =", pmax())
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
    theta  = 180/math.pi * math.acos((d**2 + D**2 - r**2) / (2*d*D))
    return theta

# Função que retorna o gráfico θ x Brilho
def graph2():
    # parâmetro r vai receber 5000 valores entre D-d até D+d. Representa a distância da Terra a Vênus.
    r = np.linspace((D-d), (D+d), 5000)

    # as funções paramétricas
    theta = 180/math.pi * np.arccos((D**2 + d**2 - r**2)/(2*d*D))
    B = ((10**17)*(r**2 + d**2 + 2*d*r - D**2)/(4*d* r**3)) #multiplicamos por uma constante 10**17 apenas por conveniência dos valores de y no gráfico

    # plotar no gráfico
    plt.figure()
    plt.plot(theta, B)
    plt.axis([0, 180, 0, 7])
    plt.title("Gráfico θ x B")
    plt.xlabel('Ângulo θ Terra-Sol-Vênus')
    plt.ylabel('Brilho')
    plt.text(88, 6.4, "*Considerar θ o menor ângulo TSV")
    plt.show()

# Função que retorna o gráfico r x Brilho
def graph1():
    r = np.linspace((D-d), (D+d), 5000)
    B = ((10**17)*(r**2 + d**2 + 2*d*r - D**2)/(4*d* r**3))
    plt.figure()
    plt. plot(r / 10**6, B)
    plt.axis([(D-d)/ 10**6, (D+d)/ 10**6, 0, 7])
    plt.title("Gráfico r x B")
    plt.xlabel('Distância r da Terra a Vênus (em milhões de km)')
    plt.ylabel('Brilho')
    plt.show()


# Retorna o brilho em função do ângulo theta
def btheta(theta):
    if theta % 180 == 0:
        return 0
    else:
        theta = (theta * math.pi) / 180
        r = math.sqrt(D**2 + d**2 - 2 * D * d * math.cos(theta)) # converte o ang theta em uma distancia r por lei dos cossenos
        return b(r)

# Função de brilho máximo para auxiliar em contas
def maxb():
    r = maxr() # r recebe valor que maximiza o brilho
    return b(r)

# Chama a função Main depois de já ter lido todas as funções
main()

