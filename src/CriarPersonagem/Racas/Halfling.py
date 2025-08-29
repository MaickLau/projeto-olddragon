from Interfaces.Raca import Raca

class Halfling(Raca):

    def __init__(self):
        super().__init__()
        self.nome = "halfling"
        self.movimento = 6
        self.infravisao = 0
        self.alinhamento = "neutro"

    def descricao(self):
        super().descricao()