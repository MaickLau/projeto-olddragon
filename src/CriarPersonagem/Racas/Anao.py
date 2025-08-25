from Interfaces.Raca import Raca

class Anao(Raca):

    def __init__(self):
        super().__init__()
        self.movimento = 6
        self.infravisao = 18
        self.alinhamento = "ordem"