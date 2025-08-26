import random

class RolarDados:

    # simula o lançamendo de 1 dado de 6 lados
    def rolar_d6(self):
        return random.randint(1, 6)

    # simula o lançamento de 3 dados de 6 lados e retorna a soma
    def rolar_3d6(self):
        valores = []

        for i in range(3):
            valores.append(self.rolar_d6())

        return sum(valores)

    # simula o lançamento de 4 dados de 6 lados, elimina o menor valor, e retorna a soma
    def rolar_4d6_descarta_menor(self):
        valores = []

        for i in range(4):
            valores.append(self.rolar_d6())

        valores.remove(min(valores))
        return sum(valores)