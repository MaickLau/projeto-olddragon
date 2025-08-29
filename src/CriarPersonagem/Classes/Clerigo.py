from Interfaces.ClassePersonagem import ClassePersonagem

class Clerigo(ClassePersonagem):
    def __init__(self):
        super().__init__()
        self.nome = "clérigo"
        self.pontos_vida = "+1d8"
        self.armas = "apenas impactantes"
        self.armaduras = "todas"
        self.itens_magicos = "todos desde que sejam ordeiros"
        self.habilidades = ["Magias Divinas", "Afastar Mortos-Vivos", "Cura Milagrosa"]

    def descricao(self):
        super().descricao()