from Interfaces.Raca import Raca

class Halfling(Raca):

    def __init__(self):
        super().__init__()
        self.movimento = 6
        self.infravisao = 0
        self.alinhamento = "neutralidade"