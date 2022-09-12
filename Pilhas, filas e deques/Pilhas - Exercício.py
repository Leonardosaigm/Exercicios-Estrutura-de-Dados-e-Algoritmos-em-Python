# Exercício de Pilhas: Crie uma expressão onde a cada caracter "(" "[" "{" ele adicione a uma pilha e caso a
# expressão contenha os caracteres ')', ']', '}' ele deve desempilhar, caso ele finalize a pilha sem "nada"
# a expressão será válida.


import numpy as np


class Pilha:

    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __pilha_cheia(self):
        if self.__topo == self.__capacidade - 1:
            return True
        else:
            return False

    def __pilha_vazia(self):
        if self.__topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print('A pilha está cheia')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor

    def desempilhar(self):
        if self.__pilha_vazia():
            print('A pilha está vazia')
        else:
            self.__topo -= 1

    def ver_topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1


expressao = str(input('Digite uma expressão com "(" "[" "{": '))
tamanho_pilha = Pilha(len(expressao))
parametros_abre = ['(', '{', '[']
parametros_fecha = [')', ']', '}']
problema = False
for c in range(len(expressao)):
    if expressao[c] in parametros_abre:
        tamanho_pilha.empilhar(c)
    if expressao[c] in parametros_fecha:
        if tamanho_pilha.ver_topo() != -1:
            tamanho_pilha.desempilhar()
        else:
            print('Sua expressão não é válida!')
            problema = True
            break
if not problema:
    if tamanho_pilha.ver_topo() >= 1:
        print('Sua expressão não é válida')
    elif tamanho_pilha.ver_topo() == -1:
        print('Sua expressão é valida!')

