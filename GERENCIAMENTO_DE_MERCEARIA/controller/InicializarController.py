#! /bin/python3
#Inicializar.py

import os
import sys

class InicializarController:
    def __init__(self):
        if sys.platform == "nt":
            os.system("cls")
            self.criar_DB()
        elif sys.platform == "linux":
            os.system("clear")
            self.criar_DB()

    def criar_DB(self):
        if not os.path.exists("DB"):
            print("=" * 20 + " Categorias " + "=" * 20)
            print(f"Olá! estou verificando que esse é seu primeiro acesso ao sistema, \npor favor, aguarde enquanto eu configuro o banco de dados...")
            os.makedirs("DB")
            print("Banco de dados configurado com sucesso!")
            input("Pressione ENTER para continuar...")
        else:
            return None
        
    @staticmethod    
    def limpar_tela():
        if sys.platform == "nt":
            os.system("cls")
        elif sys.platform == "linux":
            os.system("clear")