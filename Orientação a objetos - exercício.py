class aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def dados(self):
        print('Nome:', self.nome)
        print('Nota 1:', self.nota1)
        print('Nota 2:', self.nota2)
        print('Média:', self.media())

    def resultado(self):
        if self.media() >= 6:
            return 'Aprovado!'
        else:
            return 'Reprovado'


joao = aluno('João', 8, 9)
print(joao.media())
joao.dados()
print(joao.resultado())