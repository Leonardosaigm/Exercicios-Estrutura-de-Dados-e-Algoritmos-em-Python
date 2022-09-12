# #Baseado no conteúdo aprendido até agora, crie uma fila utilizando listas encadeadas. Algumas dicas:
# Use uma lista encadeada com extremidades duplas para controlar o início e o final da fila
# Crie uma nova classe chamada FilaListaEncadeada com os seguintes métodos:
# enfileirar
# desenfileirar
# fila_vazia
# ver_inicio
# Os métodos acima devem ser executar as funções definidas anteriormente na lista encadeada com extremidades duplas
class No:

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)


class ListaEncadeadaExtremidadeDupla:

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def lista_vazia(self):
        return self.primeiro == None

    def insere_inicio(self, valor):
        novo = No(valor)
        if self.lista_vazia():
            self.ultimo = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self, valor):
        novo = No(valor)
        if self.lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo

    def excluir_inicio(self):
        if self.lista_vazia():
            print('A lista está vazia')
            return

        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo
        return temp

    def mostrar(self):
        if self.lista_vazia():
            print('A lista está vazia')
            return
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo


class FilaListaEncadeada:
    def __init__(self):
        self.fila = ListaEncadeadaExtremidadeDupla()

    def enfileirar(self, valor):
        self.fila.insere_final(valor)

    def desenfileirar(self):
        return self.fila.excluir_inicio()

    def fila_vazia(self):
        return self.fila.lista_vazia()

    def ver_inicio(self):
        if self.fila_vazia():
            return -1
        return self.fila.primeiro.mostra_no()


fila = FilaListaEncadeada()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
fila.desenfileirar()
fila.desenfileirar()
fila.ver_inicio()
