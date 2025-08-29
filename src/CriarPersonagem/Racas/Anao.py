from Interfaces.Raca import Raca

class Anao(Raca):

    def __init__(self):
        super().__init__()
        self.nome = "Anão"
        self.movimento = 6
        self.infravisao = 18
        self.alinhamento = "ordem"

    def descricao(self):
        super().descricao()