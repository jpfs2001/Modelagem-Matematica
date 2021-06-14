import numpy as np
from numpy.core.fromnumeric import transpose
from tomografia import Tomografia

t = Tomografia()

at = np.array([
    [1, 1],
    [1, -2],
    [3, -1]
])

a = np.array([
    [[1], [1]],
    [[1], [-2]],
    [[3], [-1]]
])

x0 = np.array([[1], [3]])

b = np.array([
    2,
    -2,
    3
])



x = t.densidade(a, at, b, x0)

for i in range(len(x)):
    print(f"x {i+1}: {x[i]}")