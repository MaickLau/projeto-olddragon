class Personagem:

    def __init__(self, nome=None, raca=None, classe=None):
        self.atributos = {"Força": 0, "Destreza": 0, "Constituição": 0, "Inteligência": 0, "Sabedoria": 0, "Carisma": 0}
        self.nome = nome
        self.raca = raca
        self.classe = classe