from utils.limpar_tela import limpar_tela
from Menus.MenuRacas import MenuRacas
from CriarPersonagem.Atributos.Distribuicao import Distribuicao
from CriarPersonagem.Personagem import Personagem

class MenuAtributos:

    def __init__(self, personagem : Personagem):
        self.distribuicao = Distribuicao()
        self.personagem = personagem

    def mostrar_menuAtributos(self):

        # garante entrada de um valor inteiro
        while True:
            try:
                print("----- Criação de Personagem / Distribuições -----\n")
                print("Escolha o estilo de distribuição:")
                print("1. Estilo Clássico")
                print("2. Estilo Aventureiro")
                print("3. Estilo Heroico")
                print("4. Voltar")
                opcao = int(input("Escolha: "))

                match(opcao):
                    case 1:
                        limpar_tela()
                        self.personagem.atributos = self.distribuicao.classico()
                        print("Valores gerados:\n")

                        for chave, valor in self.personagem.atributos.items():
                            print(f"{chave:<12} : {valor:}")

                        input("\nPressione ENTER para continuar...")
                        limpar_tela()

                        break

                    case 2:
                        limpar_tela()
                        self.distribuir_e_mostrar_atributos(self.distribuicao.aventureiro())
                        break

                    case 3:
                        limpar_tela()
                        self.distribuir_e_mostrar_atributos(self.distribuicao.heroico())
                        break

                    case 4:
                        limpar_tela()
                        return

                    case _:
                        limpar_tela()
                        print("Informe um valor válido!\n")

            except ValueError:
                limpar_tela()
                print("Digite apenas números inteiros!\n")

        m = MenuRacas(self.personagem)
        m.mostrar_menuRacas()

    def distribuir_e_mostrar_atributos(self, valores):
        for chave in self.personagem.atributos:

            # para garantir a entrada de um número inteiro
            while True:
                print("Escolha os valores para cada atributo: ", *valores)

                try:
                    valor = int(input(f"\n{chave}: "))

                    # se válido, atribui ao dicionário e remove da lista
                    if valor in valores:
                        self.personagem.atributos[chave] = valor
                        valores.remove(valor)
                        limpar_tela()
                        break
                    else:
                        limpar_tela()
                        print("Esse valor não está disponível!\n")

                except ValueError:
                    limpar_tela()
                    print("Apenas valores inteiros serão aceitos!\n")


        
        print("Valores atribuidos: \n")
        for chave, valor in self.personagem.atributos.items():
            print(f"{chave:<12} : {valor}")

        input("\nPressione ENTER para continuar...")
        limpar_tela()