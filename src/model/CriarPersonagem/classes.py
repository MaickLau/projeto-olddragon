from enum import Enum

class ClassePersonagem(Enum):
    CLERIGO = ("Clérigo", "+1d8", "impactantes", "todas", "todos, ordeiros", ["Magias Divinas", "Afastar Mortos-Vivos", "Cura Milagrosa"])
    GUERREIRO = ("Guerreiro", "+1d10", "todas", "todas", "pergaminhos de proteção", ["Aparar", "Maestria em Arma"])
    LADRAO = ("Ladrão", "+1d6", "pequenas/médias", "leves", "pergaminhos de proteção", ["Ataque Furtivo", "Ouvir Ruídos", "Talentos de Ladrão"])
    MAGO = ("Mago", "+1d4", "pequenas", "nenhuma", "todos", ["Magias Arcanas", "Ler Magias", "Detectar Magias"])

    def __init__(self, nome, pontos_vida, armas, armaduras, itens_magicos, habilidades):
        self.nome = nome
        self.pontos_vida = pontos_vida
        self.armas = armas
        self.armaduras = armaduras
        self.itens_magicos = itens_magicos
        self.habilidades = habilidades