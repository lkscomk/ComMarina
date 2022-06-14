class Cao:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
    def latir(self):
        return str(self.nome) + " latiu"
    def morder(self):
        return self.nome, "mordeu"

