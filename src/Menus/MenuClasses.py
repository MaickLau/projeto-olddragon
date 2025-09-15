from utils.limpar_tela import limpar_tela
from CriarPersonagem.Personagem import Personagem
from CriarPersonagem.Classes.Guerreiro import Guerreiro
from CriarPersonagem.Classes.Clerigo import Clerigo
from CriarPersonagem.Classes.Ladrao import Ladrao
from CriarPersonagem.Classes.Mago import Mago

class MenuClasses:
    def __init__(self, personagem : Personagem):
        self.personagem = personagem
        self.classes = {"guerreiro": Guerreiro, "clérigo": Clerigo, "ladrão": Ladrao, "mago": Mago}

    def mostrar_menuClasses(self):
        while True:
            try:
                print("----- Criação de Personagem / Classes -----\n")
                print("Escolha a classe do personagem:")
                print("1. Guerreiro")
                print("2. Clérigo")
                print("3. Ladrão")
                print("4. Mago")
                print("5. Voltar")
                opcao = int(input("Escolha: "))

                match(opcao):
                    case 1:
                        limpar_tela()
                        self.definir_classe("guerreiro")
                        break

                    case 2:
                        limpar_tela()
                        self.definir_classe("clérigo")
                        break

                    case 3:
                        limpar_tela()
                        self.definir_classe("ladrão")
                        break

                    case 4:
                        limpar_tela()
                        self.definir_classe("mago")
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

    def definir_classe(self, classe_nome):
        self.personagem.classe = self.classes[classe_nome]()
        limpar_tela()
        self.personagem.classe.descricao()

        input("\nPressiona ENTER para continuar...")
        limpar_tela()