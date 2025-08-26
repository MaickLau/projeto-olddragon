from CriarPersonagem.Atributos.RolarDados import RolarDados

class Distribuicao:

    def __init__(self):
        self.dado = RolarDados()

    # retorna um dicionário com valores aleatórios armazenados em cada chave
    def classico(self):
        atributos = {}
        atributos["Força"] = self.dado.rolar_3d6()
        atributos["Destreza"] = self.dado.rolar_3d6()
        atributos["Constituição"] = self.dado.rolar_3d6()
        atributos["inteligencia"] = self.dado.rolar_3d6()
        atributos["Sabedoria"] = self.dado.rolar_3d6()
        atributos["Carisma"] = self.dado.rolar_3d6()

        return atributos

    # retorna uma lista com 6 valores, cada um representando a soma de um lançamento de 3 dados com 6 lados
    def aventureiro(self):
        soma = []

        for i in range(6):
            soma.append(self.dado.rolar_3d6())

        return soma

    # retorna uma lista com 6 valores, cada um representando a soma de um lançamento de 4 dados com 6 lados, descartando o menor valor
    def heroico(self):
        soma = []

        for i in range(6):
            soma.append(self.dado.rolar_4d6_descarta_menor())

        return soma