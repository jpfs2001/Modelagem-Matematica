# Livrarias
import math # Livraria com funções matemáticas

# O projeto é separado por funções, sedo main a função responsável por chamar as outras funções
# Variaveis globais que poderão ser acessadas de qualquer função
d = 10.81 * (10**7) # Distancia entre sol e Venus
D = 14.95 * (10**7) # Distancia entre Sol e Terra
k = 1 # Constante

def main():
    # Legenda do Menu
    print("Menu\n0 - Sair\n1 - Calcular o brilho digitando uma distancia pertencente ao intervalo [",D-d,",",D+d,"] \n2 - Descobrir qual é a distância r quando brilho é máximo\n3 - Calcular o brilho digitando o angulo VSE\n4 - Descobrir qual o angulo VSE quando brilho for máximo")

    # Aqui sera usado um lupe infinito para que o usuário possa usar o código diversas vezes sem precisar execuar novamente
    while True: 
        menu = int(input("Digte uma opção: "))
        
        if menu == 1:
            # A distância será multiplicada por 10^7 para facilitar o usuário a digitar no intervalo desejado
            r = float(input("Digite uma distância * 10^7 : "))
            print("O brilho sera: ", b(r))
        elif menu == 2:
            print("O brilho sera máximo na distancia r =", maxr()); 
        elif menu == 3:
            teta = float(input("Digite o valor do angulo VSE EM GRAUS: "))
            print("O brilho sera: ", R(teta))
        elif menu == 4:
            print("O brilho será máximo quando VSE =", maxteta(),"Radianos")
        elif menu == 0:
            break
        else:
            print("Opção inválida! ")

# Funções

# função que encontra o brilho em função de r
def b(r):
    r = r * (10**7)
    l = k * (2*d*r + r**2 + d**2 - D**2) / r**3 

    return l

# função que encontra o brilho maximo em função de r
def maxr():
    l = -2*d + math.sqrt(d**2 + 3 * (D**2))

    return l

# função que encontra o brilho em função de teta
def R(teta):
    return 1

# função que encontra o brilho máximo em funnção de teta
def maxteta():
    return 1

main()

