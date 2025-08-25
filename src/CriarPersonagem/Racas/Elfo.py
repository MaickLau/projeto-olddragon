from Interfaces.Raca import Raca

class Elfo(Raca):

    def __init__(self):
        super().__init__()
        self.movimento = 9
        self.infravisao = 18
        self.alinhamento = "neutralidade"