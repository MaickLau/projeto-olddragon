from Interfaces.Raca import Raca

class Elfo(Raca):

    def __init__(self):
        super().__init__()
        self.nome = "Elfo"
        self.movimento = 9
        self.infravisao = 18
        self.alinhamento = "neutro"

    def descricao(self):
        super().descricao()