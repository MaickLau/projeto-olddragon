from .RolarDados import RolarDados

class Distribuicao():

    def __init__(self):
        self.dado = RolarDados()

    def classico(self):
        atributos = {}
        atributos["Força"] = self.dado.rolar_3d6()
        atributos["Destreza"] = self.dado.rolar_3d6()
        atributos["Constituição"] = self.dado.rolar_3d6()
        atributos["inteligencia"] = self.dado.rolar_3d6()
        atributos["Sabedoria"] = self.dado.rolar_3d6()
        atributos["Carisma"] = self.dado.rolar_3d6()

        return atributos

    def aventureiro(self):
        soma = []

        for i in range(6):
            soma.append(self.dado.rolar_3d6())

        return soma

    def heroico(self):
        soma = []

        for i in range(6):
            soma.append(self.dado.rolar_4d6_descarta_menor())

        return soma