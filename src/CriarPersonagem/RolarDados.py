import random

class RolarDados():

    def rolar_d6(self):
        return random.randint(1, 6)

    def rolar_3d6(self):
        valores = []

        for i in range(3):
            valores.append(self.rolar_d6())

        return sum(valores)

    def rolar_4d6_descarta_menor(self):
        valores = []

        for i in range(4):
            valores.append(self.rolar_d6())

        valores.remove(min(valores))
        return sum(valores)