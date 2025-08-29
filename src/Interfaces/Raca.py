from abc import ABC, abstractmethod

class Raca(ABC):

    def __init__(self):
        self.nome = None
        self.movimento = None
        self.infravisao = None
        self.alinhamento = None
        self.habilidade = []

    @abstractmethod
    def descricao(self):
        print(f"Um {self.nome} possui:\n")
        print(f"{'Movimento':<12}: {self.movimento}")
        print(f"{'Infravisão':<12}: {self.infravisao}")
        print(f"{'Alinhamento':<12}: {self.alinhamento}")