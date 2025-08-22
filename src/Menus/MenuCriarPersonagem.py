import os
from CriarPersonagem.Distribuicao import Distribuicao

class MenuCriarPersonagem():

    def __init__(self):
        self.atributos = {"Força": 0, "Destreza": 0, "Constituição": 0, "Inteligência": 0, "Sabedoria": 0, "Carisma": 0}
        self.distribuicao = Distribuicao()

    def mostrar_menu(self):

        print("----- Criação de Personagem / Distribuições -----\n")

        while True:

            print("\nEscolha o estilo de distribuição:")
            print("1. Estilo Clássico")
            print("2. Estilo Aventureiro")
            print("3. Estilo Heroico")

            try:
                opcao = int(input("Escolha: "))

                match(opcao):
                    case 1:
                        self.atributos = self.distribuicao.classico()

                        for chave, valor in self.atributos.items():
                            print(f"{chave}: {valor}")
                        break

                    case 2: # melhorar bloco de código
                        valores = self.distribuicao.aventureiro()

                        for chave in self.atributos:
                            print("Escolha os valores para cada atributo: ")

                            while True:
                                for i in valores:
                                    print(i, end=' ')

                                valor = int(input(f"\n{chave}: "))

                                self.limpar_tela()

                                if valor in valores:
                                    self.atributos[chave] = valor
                                    valores.remove(valor)
                                    break
                                else:
                                    print("Esse valor não está disponível!\n")
                        break

                    case 3: # melhorar bloco de código
                        valores = self.distribuicao.heroico()

                        for chave in self.atributos:
                            print("Escolha os valores para cada atributo: ")

                            while True:
                                for i in valores:
                                    print(i, end=' ')

                                valor = int(input(f"\n{chave}: "))

                                self.limpar_tela()

                                if valor in valores:
                                    self.atributos[chave] = valor
                                    valores.remove(valor)
                                    break
                                else:
                                    print("Esse valor não está disponível!\n")
                        break

                    case _:
                        print("Informe um valor válido!\n")

            except ValueError:
                print("Digite apenas números inteiros!\n")

    def limpar_tela(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')