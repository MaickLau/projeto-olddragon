from abc import ABC

class Raca(ABC):

    def __init__(self):
        self.movimento = None
        self.infravisao = None
        self.alinhamento = None
        self.habilidade = []