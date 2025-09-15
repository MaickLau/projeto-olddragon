import random

def rolar(lados=6, quantidade=3):
    valores = []
    for i in range(quantidade):
        valores.append(random.randint(1, lados))

    return valores