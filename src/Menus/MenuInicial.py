from .MenuAtributos import MenuAtributos

class MenuInicial():

    def mostrar_menuInicial(self):
        m = MenuAtributos()
        m.limpar_tela()

        while True:
            print("----- Início -----\n")
            print("1. Criar Personagem")
            print("0. Sair")
            
            try:
                opcao = int(input("\nEscolha: "))

                match(opcao):
                    case 1:
                        m.mostrar_menu()
                    
                    case 0:
                        m.limpar_tela()
                        print("Encerrando...\n")
                        break

                    case _:
                        m.limpar_tela()
                        print("Informe um valor válido!\n")

            except ValueError:
                m.limpar_tela()
                print("Digite apenas números inteiros!\n")