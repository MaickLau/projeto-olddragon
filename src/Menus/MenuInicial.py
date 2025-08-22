from .MenuCriarPersonagem import MenuCriarPersonagem

class MenuInicial():

    def mostrar_menuInicial(self):

        while True:
            print("----- Início -----\n")
            print("1. Criar Personagem")
            print("0. Sair")
            
            try:
                opcao = int(input("\nEscolha: "))

                match(opcao):
                    case 1:
                        m = MenuCriarPersonagem()
                        m.mostrar_menu()
                    
                    case 0:
                        print("Encerrando...\n")
                        break

                    case _:
                        print("Informe um valor válido!\n")

            except ValueError:
                print("Digite apenas números inteiros!\n")