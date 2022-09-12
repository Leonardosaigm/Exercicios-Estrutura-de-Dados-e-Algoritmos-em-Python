# def fatorial(n):
#     fat = 1
#     for n in range(1, n+1):
#         fat *= n
#     print(fat)
#
# fatorial(6)
# # Soma sem recursao
# def soma1(n):
#     soma = 0
#     for i in range(n + 1):
#         soma += 1
#     return soma
#
# # Soma com recursao
# def soma2(n):
#     if n == 0:
#         return 0
#     return n + soma2(n - 1)

def fatorial_recursao(n):
    if n == 1:
        return 1

    return n * fatorial_recursao(n-1)


print(fatorial_recursao(3))

