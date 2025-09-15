from .rolardados import rolar

class Distribuicao:

    # retorna um dicionário com valores aleatórios armazenados em cada chave
    def classico(self):
        atributos = {}
        atributos["Força"] = sum(rolar())
        atributos["Destreza"] = sum(rolar())
        atributos["Constituição"] = sum(rolar())
        atributos["Inteligencia"] = sum(rolar())
        atributos["Sabedoria"] = sum(rolar())
        atributos["Carisma"] = sum(rolar())

        return atributos

    # retorna uma lista com 6 valores, cada um representando a soma de um lançamento de 3 dados com 6 lados
    def aventureiro(self):
        soma = []

        for i in range(6):
            soma.append(sum(rolar()))

        return soma

    # retorna uma lista com 6 valores, cada um representando a soma de um lançamento de 4 dados com 6 lados, descartando o menor valor
    def heroico(self):
        soma = []

        for i in range(6):
            aux = rolar(6, 4)
            aux.remove(min(aux))
            soma.append(sum(aux))

        return soma