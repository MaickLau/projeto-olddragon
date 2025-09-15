from utils.limpar_tela import limpar_tela
from Menus.MenuAtributos import MenuAtributos
from CriarPersonagem.Personagem import Personagem

class MenuInicial:

    def mostrar_menuInicial(self):
        limpar_tela()

        while True:
            print("----- Início -----\n")
            print("1. Criar Personagem")
            print("0. Sair")
            
            try:
                opcao = int(input("\nEscolha: "))

                match(opcao):
                    case 1:
                        limpar_tela()
                        nome = input("Digite o nome do personagem: ")
                        personagem = Personagem(nome)
                        m = MenuAtributos(personagem)
                        limpar_tela()
                        m.mostrar_menuAtributos()
                    
                    case 0:
                        limpar_tela()
                        print("Encerrando...\n")
                        break

                    case _:
                        limpar_tela()
                        print("Informe um valor válido!\n")

            except ValueError:
                limpar_tela()
                print("Digite apenas números inteiros!\n")