import os
from CriarPersonagem.Distribuicao import Distribuicao

class MenuAtributos():

    def __init__(self):
        self.atributos = {"Força": 0, "Destreza": 0, "Constituição": 0, "Inteligência": 0, "Sabedoria": 0, "Carisma": 0}
        self.distribuicao = Distribuicao()

    def mostrar_menu(self):
        self.limpar_tela()
        print("----- Criação de Personagem / Distribuições -----\n")

        while True:

            # garante entrada de uma valor inteiro
            while True:
                try:
                    print("Escolha o estilo de distribuição:")
                    print("1. Estilo Clássico")
                    print("2. Estilo Aventureiro")
                    print("3. Estilo Heroico")
                    opcao = int(input("Escolha: "))

                    self.limpar_tela()
                    break

                except ValueError:
                    self.limpar_tela()
                    print("Apenas números inteiros serão aceitos!\n")

            match(opcao):
                case 1:
                    self.atributos = self.distribuicao.classico()
                    print("Valores gerados:\n")

                    for chave, valor in self.atributos.items():
                        print(f"{chave}: {valor}")

                    input("\nPressione ENTER para continuar...")
                    self.limpar_tela()

                    break

                case 2:
                    self.distribuir_e_mostrar_atributos(self.distribuicao.aventureiro())
                    break

                case 3:
                    self.distribuir_e_mostrar_atributos(self.distribuicao.heroico())
                    break

                case _:
                    self.limpar_tela()
                    print("Informe um valor válido!\n")

    def limpar_tela(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

    def distribuir_e_mostrar_atributos(self, valores):
        for chave in self.atributos:

            # para garantir que valor existe na lista antes de continuar
            while True:

                # para garantir a entrada de um número inteiro
                while True:
                    print("Escolha os valores para cada atributo: ", end=' ')
                    for i in valores:
                        print(i, end=' ')

                    try:
                        valor = int(input(f"\n{chave}: "))
                        break
                    except ValueError:
                        self.limpar_tela()
                        print("Apenas valores inteiros serão aceitos!\n")

                # se válido, atribui ao dicionário e remove da lista
                if valor in valores:
                    self.atributos[chave] = valor
                    valores.remove(valor)
                    self.limpar_tela()
                    break
                else:
                    self.limpar_tela()
                    print("Esse valor não está disponível!\n")
        
        print("Valores atribuidos: \n")
        for chave, valor in self.atributos.items():
            print(f"{chave}: {valor}")

        input("\nPressione ENTER para continuar...")
        self.limpar_tela()