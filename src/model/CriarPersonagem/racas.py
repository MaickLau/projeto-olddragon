from enum import Enum

class RacaPersonagem(Enum):

    ANAO = ("Anão", 6, 18, "ordem")
    ELFO = ("Elfo", 9, 18, "neutro")
    HALFLING = ("Halfling", 6, 0, "neutro")
    HUMANO = ("Humano", 9, 0, "qualquer")

    def __init__(self, nome, movimento, infravisao, alinhamento):
        self.nome = nome
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento