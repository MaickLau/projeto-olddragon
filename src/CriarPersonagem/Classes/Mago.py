from Interfaces.ClassePersonagem import ClassePersonagem

class Mago(ClassePersonagem):
    def __init__(self):
        self.nome = "mago"
        self.pontos_vida = "+1d4"
        self.armas = "apenas pequenas"
        self.armaduras = "nenhuma"
        self.itens_magicos = "todos"
        self.habilidades = ["Magias Arcanas", "Ler Magias", "Detectar Magias"]

    def descricao(self):
        super().descricao()