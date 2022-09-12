# Baseado no conteúdo aprendido até agora, crie uma pilha utilizando listas encadeadas. Algumas dicas:
# Use uma lista encadeada simples
# Crie uma nova classe chamada PilhaListaEncadeada com os seguintes métodos:
# empilhar
# desempilhar
# pilha_vazia
# ver_topo
# Os métodos acima devem ser executar as funções definidas anteriormente na lista encadeada

import numpy as np


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)


class PilhaListaencadeada:
    def __init__(self):
        self.primeiro = None

    def empilhar(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def desempilhar(self):
        self.pilha_vazia()
        temporario = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temporario

    def pilha_vazia(self):
        if self.primeiro == None:
            print('A pilha está vazia.')
            return None

    def ver_topo(self):
        self.pilha_vazia()
        if self.primeiro != None:
            topo = self.primeiro
            topo.mostra_no()


lista = PilhaListaencadeada()
lista.empilhar(1)
lista.empilhar(2)
lista.empilhar(3)
lista.desempilhar()
lista.ver_topo()






