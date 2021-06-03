from ler import lerPlanilha
from matrizes import Matrizes

l = Matrizes()

### tarefa 3 ####
# capturar dados
tamanhoMatriz = 12 # 12 x 12
comeca = [3, 6] # H6 
diretorio = "projeto-3/matriz.xls" # modelagem-matematica/projeto-3/matriz.xls
matriz = lerPlanilha(diretorio, comeca, tamanhoMatriz, 14)

# Diferença entre I e C
Dif = l.diferencaMatrizes(l.gerarIdentidade(len(matriz)), matriz)
# matriz de Leontief
L = l.inversa(Dif)
print("A matriz de Leontief é:")
for a in L: 
    print(a)

#comparando o obtido com a tabela lá
LeontiefTabela = lerPlanilha(diretorio, [3, 6], 12, 15)
DiferencaMedia = 0
for i in range(0, len(LeontiefTabela)):
    Diferencas = []
    for j in range(0, len(LeontiefTabela)):
        dif = 100-min([LeontiefTabela[i][j], L[i][j]])*100/max([LeontiefTabela[i][j], L[i][j]])
        if dif < 10**(-10): Diferencas.append(0) #se a diferença for menor que 10^-10, ele fala que é zero. É aceitável, vai...
        else: Diferencas.append(dif)
    DiferencaMedia += sum(Diferencas)/len(Diferencas)

print(f"\n\nA diferença média entre o calculado e o da planilha é de {DiferencaMedia}%")
### Para calcular o x, basta multiplicar a matriz de Leontief pela matriz demanda... ###