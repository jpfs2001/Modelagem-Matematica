#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1º Parte: cálculo de M.

A = [[1,2,3],[4,5,6],[7,8,9]]   # "A" arbitrário para testar o programa.


mS = []   # m = 0.15

for linha in A:
  AUX_1 = []
  for elem in linha:
    s = 0.15*(1/len(A[0]))
    AUX_1.append(s)
  mS.append(AUX_1)


A_ = []   # Onde A_ = (1 − m)A, (1 - m) = 0.85.

for linha in A:
  AUX_2 = []
  for elem in linha:
    a_ = 0.85*elem
    AUX_2.append(a_)
  A_.append(AUX_2)
  

M = []   # Onde M = A_ + mS.

for linha in range(len(A)):
  AUX_3 = []
  
  for coluna in range(len(A[0])):
    
    AUX_3.append( A_[linha][coluna] + mS[linha][coluna] )
    
  M.append(AUX_3)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 2º Parte: cálculo de c.

c = -1

for coluna in range(len(M[0])):
  min_ = M[0][coluna]
  
  for linha in range(len(M)):
    if min_ > M[linha][coluna]:
      min_ = M[linha][coluna]
      
  mod = 1 - 2*min_
  if mod < 0:
    mod = (-1)*mod
    
  if c < mod:
    c = mod
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
