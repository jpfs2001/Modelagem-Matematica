from matrizes import Matrizes

m = Matrizes()

matriz = [
    [.1, .6, .6], 
    [.3, .2, 0], 
    [.3, .1, .1] 
]

d = [0, 18, 0]

a = []

# 1.a 
for i in range(len(matriz)): #Matriz que percorre as linhas da matriz e multiplica o elemento da coluna agricultura por 100
    a.append(100 * matriz[i][1])    

print("\nMatriz consumo para 100 unidades de agricultura: \n") 
for a in a:
    print(f"[ {a} ]")

# 1.b
# Diferença entre I e C
Dif = m.diferencaMatrizes(m.gerarIdentidade(len(matriz)), matriz)
# matriz de Leontief
L = m.inversa(Dif)

print("\nMatriz Leontief: \n")
for L in L:
    print(L)

# 1.c
x = m.multiplicacao(matriz, d)
print("\nMatriz com nível de produção: \n")
for x in x:
    print(f"[ {round(x, 10)} ]")




