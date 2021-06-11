import numpy as np
from numpy.core.fromnumeric import transpose

def main():

    global x0
    
    for k in range(50):

        x = []

        for i in range(len(a)):
            

            if(i == 0):
                aux = np.matmul(at[i], ((b[i] - np.matmul(transpose(a[i]), x0)) / (np.matmul(np.transpose(a[i]), a[i]))))
                aux = inverter(aux)
                x.append(np.sum([x0, aux], axis=0))
            else:
                aux = np.matmul(at[i], ((b[i] - np.matmul(transpose(a[i]), x[i-1])) / (np.matmul(np.transpose(a[i]), a[i]))))
                aux = inverter(aux)
                x.append(np.sum([x[i-1], aux], axis=0))

            if(i == (len(a)-1)):
                x0 = x[i]
                print (x0, x[i])

    return x



def inverter(x):
    aux = []
    for i in x:
        aux.append([i]) 
    return(aux)

x0 = x00 = np.array([[1], [3]])
x0t = np.array([1, 3])

a = np.array([
    [1, 1],
    [1, -2],
    [3, -1]
])



at = np.array([
    [[1], [1]],
    [[1], [-2]],
    [[3], [-1]]
])



b = np.array([
    2,
    -2,
    3
])

k = np.array([1, 1])


# print(main())
print(main())