class MenuCriarPersonagem():

    def mostrar_menu(self):

        print("----- Criação de Personagem / Distribuições -----\n")

        nome = input("Nome do Personagem: ")

        # personagens = []
        # p = Personagem(nome)
        # personagens.append(p)

        while True:

            print("\nEscolha o estilo de distribuição:")
            print("1. Estilo Clássico")
            print("2. Estilo Aventureiro")
            print("3. Estilo Heroico")

            try:
                opcao = int(input("Escolha: "))

                match(opcao):
                    case 1:
                        # p.classico()
                        # p.exibirStatus()
                        print("Clássico")
                        break

                    case 2:
                        # p.aventureiro()
                        print("Aventureiro")
                        break

                    case 3:
                        # p.heroico()
                        print("Heroico")
                        break

                    case _:
                        print("Informe um valor válido!\n")

            except ValueError:
                print("Digite apenas números inteiros!\n")