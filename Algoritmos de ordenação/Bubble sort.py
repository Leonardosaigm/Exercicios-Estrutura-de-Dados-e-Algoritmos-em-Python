import numpy as np


def bubble_sort(vetor):
    n = len(vetor)

    for i in range(n):
        for j in range(0, n - i - 1):
            if vetor[j] > vetor[j + 1]:
                temp = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp
    return vetor


bubble_sort(np.array([15, 34, 8, 3]))

bubble_sort(np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
