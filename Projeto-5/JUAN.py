X = [[0.36815084663504394], [0.14180925256236895], [0.2879616376364997], [0.20207826316608607]]

y = []

for elemento in X:
    y.append(elemento[0])

for k in range(1, len(y)+1):
    print(f"Posição {k}: Página {y.index(sorted(y)[-k])+1}")
