from Interfaces.Raca import Raca

class Humano(Raca):

    def __init__(self):
        super().__init__()
        self.nome = "humano"
        self.movimento = 9
        self.infravisao = 0
        self.alinhamento = "qualquer"

    def descricao(self):
        super().descricao()