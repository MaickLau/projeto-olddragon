from Interfaces.ClassePersonagem import ClassePersonagem

class Ladrao(ClassePersonagem):
    def __init__(self):
        super().__init__()
        self.nome = "ladrão"
        self.pontos_vida = "+1d6"
        self.armas = "apenas pequenas ou médias. Armas grandes geram ataques difíceis"
        self.armaduras = "apenas as leves"
        self.itens_magicos = "pergaminhos de proteção"
        self.habilidades = ["Ataque Furtivo", "Ouvir Ruídos", "Talentos de Ladrão"]

    def descricao(self):
        super().descricao()