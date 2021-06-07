from matrizes import Matrizes

m = Matrizes()

matriz = [
    [.1588, .0064, .0025, .0304, .0014, .0083, .1594],
    [.0057, .2645, .0436, .0099, .0083, .0201, .3413],
    [.0264, .1506, .3557, .0139, .0142, .0070, .0236],
    [.3299, .0565, .0495, .3636, .0204, .0483, .0649],
    [.0089, .0081, .0333, .0295, .3412, .0237, .0020],
    [.1190, .0901, .0996, .1260, .1722, .2368, .3369],
    [.0063, .0126, .0196, .0098, .0064, .0132, .0012]
    ]

d1958 = [74000, 56000, 10500, 25000, 17500, 196000, 5000]

d1964 = [99640, 75548, 14444, 33501, 23527, 263985, 65260]

# 1.b
# Diferença entre I e C
Dif = m.diferencaMatrizes(m.gerarIdentidade(len(matriz)), matriz)
# matriz de Leontief
Leontief = m.inversa(Dif)


x1958 =  m.multiplicacao(Leontief, d1958)
print("\nMatriz com nível de produção em 1958: \n")
for x in x1958:
    print(f"[ {round(x, 10)} ]")


x1964 = m.multiplicacao(Leontief, d1964)
print("\nMatriz com nível de produção em 1964: \n")
for x in x1964:
    print(f"[ {round(x, 10)} ]")