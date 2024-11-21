#!/usr/bin/python3
#MenuView.py

from view.CategoriaView import CategoriaView
from controller.InicializarController import InicializarController as Inicializar


class MenuView:
    Inicializar()
    Inicializar.limpar_tela()
    
    @staticmethod
    def menu():
        while True:
            opcoes = {
                "1": "Categoria",
                "2": "Produto",
                "3": "Fornecedor",
                "4": "Cliente",
                "5": "Funcionário",
                "6": "Venda",
            }
            print("=" * 20 + " Categorias " + "=" * 20)
            for opcao in opcoes:
                print(f"{opcao} - {opcoes[opcao]}")
            print("0 - Sair\n")
            opcao = input("\nDigite a opção desejada: ")

            if opcao == "1":
                Inicializar.limpar_tela()
                CategoriaView.categoria()
            elif opcao == "2":
                pass
            elif opcao == "3":
                pass
            elif opcao == "4":
                pass
            elif opcao == "5":
                pass
            elif opcao == "6":
                pass
            elif opcao == "0":
                Inicializar.limpar_tela()
                print("Saindo do sistema...")
                exit()
            else:
                Inicializar.limpar_tela()
                print("Opção inválida!")