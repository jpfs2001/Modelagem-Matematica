# Código que objetiva generalizar a obtenção da matriz de ligação A ao olharmos seu grafo.

# 2º Parte: cria-se uma matriz A nxn. Inicialmente todas suas entradas são iguais a zero, ao final dessa parte suas entradas são zero se o elemento da linha não recebe links do elemento da coluna e 1 se recebe.
def gerarAVazio(n):
    A = []
    for x in range(n):
        AUX = []
        for y in range(n):
            AUX.append(0)
        A.append(AUX)
    return A

def insercaoDoUsuario():
    # 1º Parte: pergunta-se a quantidade de páginas a serem analisadas (se chamando essa quantidade de n, A é uma matriz nxn).
    while True:
        n = input("Quantas são as páginas? Digite um numeral inteiro positivo: ")
        try:
            n = float(n)
        except:
            print("Você não digitou um numeral. Tente novamente.")
            continue
        if n % 1 == 0 and n > 0:
            n = int(n)
            break
        else:
            print("Você não digitou um inteiro positivo. Tenta novamente.")
            continue    

    A = gerarAVazio(n)

    print("Numere as páginas de 1 a n.\nResponda no formato 1, 2, ..., n-1, n.")

    for linha in range(len(A)):

        while True:
            aux = 0
            r = input("Quais páginas tem links para a página {}?\n".format(linha + 1))
            try:
                R = r.split(",")
            except:
                print("Formato incompatível. Tente novamente.")
                continue
            
            try:
                for i in R:
                    i = float(i)
                    if i > n or i <= 0:
                        aux = -1
                        print("Você citou páginas fora do alcance. Tente novamente.")
                    if i % 1 != 0:
                        aux = -1
                        print("Você digitou páginas como números não inteiros. Tente novamente.")
            except:
                print("Você utilizou caracteres inválidos. Tente novamente.")
                continue
                
            if aux == -1:
                continue
                
            break

            
        for item in R:
            coluna = int(float(item)) - 1
            if coluna == linha:
                A[linha][coluna] = 0
            else:
                A[linha][coluna] = 1


    # 3º Parte: por fim, os elementos de uma coluna são divididos pela quantidade de elementos não núlos dela.

    for coluna in range(len(A[0])):
        contador = 0
        for linha in range(len(A)):
            if A[linha][coluna] != 0:
                contador += 1
        if contador != 0:
            for linha_aux in range(len(A)):
                A[linha_aux][coluna] = A[linha_aux][coluna]/contador
        
    print(f"\n{'-'*50}\n\nA matriz de ligação A é dada por:\nA = {A}\n")

    return A