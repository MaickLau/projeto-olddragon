from CriarPersonagem.Personagem import Personagem

class MenuCriarPersonagem():

    def mostrar_menu(self):

        print("----- Criação de Personagem / Distribuições -----\n")

        nome = input("Nome do Personagem: ")

        while True:

            print("\nEscolha o estilo de distribuição:")
            print("1. Estilo Clássico")
            print("2. Estilo Aventureiro")
            print("3. Estilo Heroico")

            try:
                opcao = int(input("Escolha: "))

                match(opcao):
                    case 1:
                        # adicionar bloco de código
                        break

                    case 2:
                        # adicionar bloco de código
                        break

                    case 3:
                        # adicionar bloco de código
                        break

                    case _:
                        print("Informe um valor válido!\n")

            except ValueError:
                print("Digite apenas números inteiros!\n")