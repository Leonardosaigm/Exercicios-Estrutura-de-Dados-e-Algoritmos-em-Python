# def potencia_padrao(n, e):
#     pot = n
#     for c in range(1, e):
#         pot = pot * n
#     print(pot)


def potencia_recursiva(n, e):
    if n < 0 or e < 0:
        return -1
    if e == 0:
        return 1
    return n * potencia_recursiva(n, e-1)


print(potencia_recursiva(2, 5))
