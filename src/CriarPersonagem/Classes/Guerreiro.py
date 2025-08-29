from Interfaces.ClassePersonagem import ClassePersonagem

class Guerreiro(ClassePersonagem):
    def __init__(self):
        super().__init__()
        self.nome = "guerreiro"
        self.pontos_vida = "+1d10"
        self.armas = "todas"
        self.armaduras = "todas"
        self.itens_magicos = "pergaminhos de proteção"
        self.habilidades = ["Aparar", "Maestria em Arma"]

    def descricao(self):
        super().descricao()