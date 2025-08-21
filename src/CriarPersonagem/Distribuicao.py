from .RolarDados import RolarDados

class Distribuicao():

    def __init__(self):
        self.dado = RolarDados()
        self.atributos = {}

    def classico(self):
        self.atributos["Força"] = self.dado.rolar_d6()
        self.atributos["Destreza"] = self.dado.rolar_d6()
        self.atributos["Constituição"] = self.dado.rolar_d6()
        self.atributos["inteligencia"] = self.dado.rolar_d6()
        self.atributos["Sabedoria"] = self.dado.rolar_d6()
        self.atributos["Carisma"] = self.dado.rolar_d6()

    def aventureiro(self):
        valores = []

        for i in range(6):
            valores.append(self.dado.rolar_d6())
            # terminar

    def heroico(self):
        valores = []

        for i in range(7):
            valores.append(self.dado.rolar_d6())
            # terminar