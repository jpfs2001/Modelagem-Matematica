# -*- coding: utf-8 -*-
"""matriz - questão 3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z9L_pPRyaJ2Jq3R4oB3LToffXcItkWp6
"""

A = [
    [0, .5, .5, 0, 0, 0, 0, 0],
    [0, 0, .5, .5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, .5],
    [.5, 0, .5, 0, 0, 0, 0, 0]
]

A_t = np.transpose(A)

print(A_t)

import numpy as np

X = [
    [[x1], [x2], [x3], [x4], [x5], [x6], [x7], [x8]]
]

X_T = np.transpose(X)