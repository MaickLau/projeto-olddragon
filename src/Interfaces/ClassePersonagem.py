from abc import ABC, abstractmethod

class ClassePersonagem(ABC):
    def __init__(self):

        self.nome = None
        self.pontos_vida = None
        self.armas = None
        self.armaduras = None
        self.itens_magicos = None
        self.habilidades = []

    @abstractmethod
    def descricao(self):
        print(f"Equipamentos que um {self.nome} pode usar: \n")
        print(f"{'Armas':<14}: {self.armas}")
        print(f"{'Armadura':<14}: {self.armaduras}")
        print(f"{'Itens Mágicos':<14}: {self.itens_magicos}")

        print("\nHabilidades:\n")
        for i in self.habilidades:
            print(f"-{i}")

        print(f"\nGanha {self.pontos_vida} por nível")