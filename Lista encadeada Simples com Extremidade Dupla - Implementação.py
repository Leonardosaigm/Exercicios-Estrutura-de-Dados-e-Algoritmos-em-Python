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

    def __lista_vazia(self):
        return self.primeiro == None

    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo

    def excluir_inicio(self):
        if self.__lista_vazia():
            print('A lista está vazia')
            return

        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo
        return temp

    def mostrar(self):
        if self.__lista_vazia():
            print('A lista está vazia')
            return
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

# Insere no início e mostrar
# lista = ListaEncadeadaExtremidadeDupla()
#
# lista.insere_inicio(1)
# lista.primeiro, lista.ultimo
# lista.mostrar()
# lista.primeiro, lista.ultimo


# Insere no final
#
# lista = ListaEncadeadaExtremidadeDupla()
# lista.insere_final(1)
# lista.primeiro, lista.ultimo
# lista.insere_final(2)
# lista.insere_final(3)
# lista.mostrar()
# lista.insere_inicio(0)
# lista.insere_final(4)
# lista.mostrar()

# Excluir do início
#
# lista = ListaEncadeadaExtremidadeDupla()
# lista.insere_inicio(1)
# lista.insere_final(3)
# lista.mostrar()
# lista.excluir_inicio()
# lista.mostrar()
# lista.excluir_inicio()
# lista.excluir_inicio()
# lista.mostrar()
