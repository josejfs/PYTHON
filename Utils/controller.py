#! /bin/python3

import os
import sys
from DAO import *

class Inicializar:
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

class CategoriaController:
    @staticmethod
    def salvar_categoria(categoria_nome):
        if categoria_nome.strip() == "":
            print("Erro! O nome da categoria não pode ser vazio!")
        else:
            try:
                CategoriaDAO.salvar_categoria(categoria_nome)
                CategoriaController.listar_categoria()
            except ValueError as e:
                return str(e)
            except Exception as e:
                return f"Erro inesperado: {e}"
        
    @staticmethod
    def listar_categoria():
        try:
            categorias = CategoriaDAO.listar_categoria()
            
            # Encontra o tamanho máximo para cada coluna
            max_id = len("ID")  # Começa com o tamanho do cabeçalho
            max_categoria = len("Categoria")
            
            for categoria in categorias:
                max_id = max(max_id, len(str(categoria.id)))
                max_categoria = max(max_categoria, len(categoria.categoria))
            
            # Adiciona espaço extra para padding
            max_id += 2
            max_categoria += 2
            
            # Cria a linha divisória
            linha = f"+{'-' * max_id}+{'-' * max_categoria}+"
            
            # Imprime o cabeçalho
            print(linha)
            print(f"|{'ID':^{max_id}}|{'Categoria':^{max_categoria}}|")
            print(linha)
            
            # Imprime cada categoria
            for categoria in categorias:
                print(f"|{str(categoria.id):^{max_id}}|{categoria.categoria:^{max_categoria}}|")
            
            # Imprime a linha final
            print(linha)
                
        except ValueError as e:
            return str(e)
        except Exception as e:
            return f"Erro inesperado: {e}"
        
    @staticmethod
    def editar_categoria():
        pass

    @staticmethod
    def deletar_categoria():
        pass