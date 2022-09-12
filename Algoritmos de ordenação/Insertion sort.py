import numpy as np


def insertion_sort(vetor):
    n = len(vetor)

    for i in range(1, n):
        marcado = vetor[i]

        j = i - 1
        while j >= 0 and marcado < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = marcado

    return vetor


insertion_sort(np.array([15, 34, 8, 3]))

insertion_sort(np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))