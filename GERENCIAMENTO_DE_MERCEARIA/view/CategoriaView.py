#! /usr/bin/python3
#CategoriaView.py

from controller.CategoriaController import CategoriaController
from controller.InicializarController import InicializarController as Inicializar

class CategoriaView:
    @staticmethod
    def sub_menu(itens):
        print("=" * 20 + " Categorias " + "=" * 20)
        for i in itens:
            print(f"{i} - {itens[i]}")
        print("0 - Sair\n")

    @staticmethod
    def categoria():
        while True:
            lista_sub_menu = {
                "1": "Cadastrar Categoria", 
                "2": "Listar Categorias", 
                "3": "Limpar Tela"
            }
            CategoriaView.sub_menu(lista_sub_menu)
            opcao = input("Digite a opção desejada: ")
            print("=" * 52)

            if opcao == "1":
                Inicializar.limpar_tela()
                print("=" * 20 + " Categorias " + "=" * 20)
                cat1 = input("Digite o nome da categoria ou 'c' para cancelar: ")
                if cat1 == "c":
                    Inicializar.limpar_tela()
                    CategoriaView.categoria()
                else:
                    CategoriaController.salvar_categoria(cat1)

            elif opcao == "2":
                Inicializar.limpar_tela()
                CategoriaController.listar_categoria()

            elif opcao == "3":
                Inicializar.limpar_tela()

            elif opcao == "0":
                Inicializar.limpar_tela()
                break
            else:
                Inicializar.limpar_tela()
                print("Opção inválida!")