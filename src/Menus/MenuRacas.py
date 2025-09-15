from utils.limpar_tela import limpar_tela
from Menus.MenuClasses import MenuClasses
from CriarPersonagem.Personagem import Personagem
from CriarPersonagem.Racas.Humano import Humano
from CriarPersonagem.Racas.Elfo import Elfo
from CriarPersonagem.Racas.Anao import Anao
from CriarPersonagem.Racas.Halfling import Halfling

class MenuRacas:

    def __init__(self, personagem : Personagem):
        self.personagem = personagem
        self.racas = {"humano": Humano, "elfo": Elfo, "anão": Anao, "halfling": Halfling}

    def mostrar_menuRacas(self):

        while True:
            try:
                print("----- Criação de Personagem / Raças -----\n")
                print("Escolha a raça do personagem:")
                print("1. Humano")
                print("2. Elfo")
                print("3. Anão")
                print("4. Halfling")
                print("5. Voltar")
                opcao = int(input("\nEscolha: "))

                limpar_tela()

                match(opcao):
                    case 1:
                        limpar_tela()
                        self.definir_raca("humano")
                        break

                    case 2:
                        limpar_tela()
                        self.definir_raca("elfo")
                        break

                    case 3:
                        limpar_tela()
                        self.definir_raca("anão")
                        break

                    case 4:
                        limpar_tela()
                        self.definir_raca("halfling")
                        break

                    case 5:
                        limpar_tela()
                        return
                    
                    case _:
                        limpar_tela()
                        print("Informe um valor válido!\n")

            except ValueError:
                limpar_tela()
                print("Digite apenas números inteiros!\n")

        m = MenuClasses(self.personagem)
        m.mostrar_menuClasses()

    def definir_raca(self, raca_nome):
        self.personagem.raca = self.racas[raca_nome]()
        limpar_tela()
        self.personagem.raca.descricao()

        input("\nPressione ENTER para continuar...")
        limpar_tela()
