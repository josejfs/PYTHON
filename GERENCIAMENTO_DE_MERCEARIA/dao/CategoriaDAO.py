#! /bin/python3
#Categoria.py

import json
from model.CategoriaModel import CategoriaModel as Categoria

class CategoriaDAO:
    @classmethod
    def salvar_categoria(cls, categoria_nome):

        arquivo_json = "DB/categoria.json"

        # Tentar carregar categorias existentes ou iniciar uma lista vazia
        try:
            with open(arquivo_json, 'r') as file:
                categorias_existentes = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            categorias_existentes = []

        # Determinar o próximo ID
        if categorias_existentes:
            ultimo_id = max(categoria['id'] for categoria in categorias_existentes)
            novo_id = ultimo_id + 1
        else:
            novo_id = 1

        # Criar o dicionário da nova categoria
        categoria_dict = {"id": novo_id, "categoria": categoria_nome}
        categorias_existentes.append(categoria_dict)

        # Salvar as categorias atualizadas no arquivo
        with open(arquivo_json, 'w') as file:
            json.dump(categorias_existentes, file, indent=4)

        print(f"\nCategoria '{categoria_nome}' com ID {novo_id} Salva com sucesso!\n")

    @classmethod
    def listar_categoria(cls):

        arquivo_json = "DB/categoria.json"

        try:
            with open(arquivo_json, 'r') as file:
                categorias_existentes = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            categorias_existentes = []

        categorias = []
        for categoria in categorias_existentes:
            categoria_obj = Categoria(categoria['id'], categoria['categoria'])
            categorias.append(categoria_obj)

        return categorias
    
    @classmethod
    def editar_categoria(cls):
        pass

    @classmethod
    def deletar_categoria(cls):
        pass