# Livrarias
import math # Livraria com funções matemáticas

# O projeto é separado por funções, sedo main a função responsável por chamar as outras funções
# Variaveis globais que poderão ser acessadas de qualquer função
d = 10.81 * (10**7) # Distancia entre sol e Venus
D = 14.95 * (10**7) # Distancia entre Sol e Terra
k = 1 # Constante

def main():
    # Legenda do Menu
    print("Menu\n0 - Sair\n1 - Calcular o brilho digitando uma distancia em km pertencente ao intervalo [4.14 * 10^7 , 25.76 * 10^7] \n2 - Descobrir qual é a distância r quando brilho é máximo\n3 - Calcula p quando brilho é máximo\n4 - Descobrir qual o angulo VSE quando brilho for máximo\n")

    # Aqui sera usado um lupe infinito para que o usuário possa usar o código diversas vezes sem precisar execuar novamente
    while True: 
        menu = int(input("Digte uma opção: "))
        if menu == 1:
            # Tratamento de dados para que o usuário só possa digitar um valor no intervalo
            while True:
                # A distância será multiplicada por 10^7 para facilitar o usuário a digitar no intervalo desejado
                r = float(input("Digite uma distância em km (ela vai ser multiplicada por 10^7): "))
                print("O brilho sera: ", b(r))

                if(r >= 4.14 and r <= 25.76):
                        break
                print("Valores fora do intervalo, tente outro valor!")

        elif menu == 2:
            print("O brilho sera máximo na distancia r =", maxr()); 
        elif menu == 3:
            print("O briho será máximo quando p =", pmax())
        elif menu == 4:
            print("O brilho será máximo quando VSE =", maxtetha(),"Radianos")
        elif menu == 0:
            break
        else:
            print("Opção inválida! ")

# Funções

# função que encontra o brilho em função de r
def b(r):
    r = r * (10**7)
    B = k * (2*d*r + r**2 + d**2 - D**2) / (4 * d * r**3)

    return B

# função que encontra o brilho maximo em função de r
def maxr():
    B = -2*d + math.sqrt(d**2 + 3 * (D**2))

    return B

# função que p quando brilho for máximo
def pmax():
    
    r = maxr() # Pegando o valor máxido de r para usar na fórmula
    p = (r**2 + d**2 + 2*d*r - D**2) / (4 * d * r)
    
    return p

# função que encontra o brilho máximo em funnção de tetha
def maxtetha():
    r = maxr() # Pegando o valor máxido de r para usar na fórmula
    theta  = math.acos((d**2 + D**2 - r**2) / (2*d*D))
    print((theta * 180) / math.pi)
    return theta


# Chama a função Main depois de já ter lido todas as funções
main()

