#! /bin/python3
#DOA.py

import json
from model import Categoria

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
    
class ProdutoDAO:
    @classmethod
    def salvar_produto(cls, produto_nome, valor, categoria_id):

        arquivo_json = "DB/produto.json"

        # Tentar carregar produtos existentes ou iniciar uma lista vazia
        try:
            with open(arquivo_json, 'r') as file:
                produtos_existentes = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            produtos_existentes = []

        # Determinar o próximo ID
        if produtos_existentes:
            ultimo_id = max(produto['id'] for produto in produtos_existentes)
            novo_id = ultimo_id + 1
        else:
            novo_id = 1

        # Criar o dicionário do novo produto
        produto_dict = {"id": novo_id, "produto": produto_nome, "valor": valor, "categoria_id": categoria_id}
        produtos_existentes.append(produto_dict)

        # Salvar os produtos atualizados no arquivo
        with open(arquivo_json, 'w') as file:
            json.dump(produtos_existentes, file, indent=4)

        print(f"Produto '{produto_nome}' salvo com ID {novo_id} no arquivo {arquivo_json} com sucesso!")

    @classmethod
    def listar_produto(cls):

        arquivo_json = "DB/produto.json"

        try:
            with open(arquivo_json, 'r') as file:
                produtos_existentes = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            produtos_existentes = []

        return produtos_existentes
    
class FornecedorDAO:
    @classmethod
    def salvar_fornecedor(cls, fornecedor_nome, cnpj, endereco, telefone, email, produto_id, categoria_id):

        arquivo_json = "DB/fornecedor.json"

        # Tentar carregar fornecedores existentes ou iniciar uma lista vazia
        try:
            with open(arquivo_json, 'r') as file:
                fornecedores_existentes = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            fornecedores_existentes = []

        # Determinar o próximo ID
        if fornecedores_existentes:
            ultimo_id = max(fornecedor['id'] for fornecedor in fornecedores_existentes)
            novo_id = ultimo_id + 1
        else:
            novo_id = 1

        # Criar o dicionário do novo fornecedor
        fornecedor_dict = {"id": novo_id, "fornecedor": fornecedor_nome, "cnpj": cnpj, "endereco": endereco, "telefone": telefone, "email": email, "produto_id": produto_id, "categoria_id": categoria_id}
        fornecedores_existentes.append(fornecedor_dict)

        # Salvar os fornecedores atualizados no arquivo
        with open(arquivo_json, 'w') as file:
            json.dump(fornecedores_existentes, file, indent=4)

        print(f"Fornecedor '{fornecedor_nome}' salvo com ID {novo_id} no arquivo {arquivo_json} com sucesso!")

    @classmethod
    def listar_fornecedor(cls):

        arquivo_json = "DB/fornecedor.json"

        try:
            with open(arquivo_json, 'r') as file:
                fornecedores_existentes = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            fornecedores_existentes = []

        return fornecedores_existentes

class ClienteDAO:
    @classmethod
    def salvar_cliente(cls, cliente_nome, endereco, telefone):

        arquivo_json = "DB/cliente.json"

        # Tentar carregar clientes existentes ou iniciar uma lista vazia
        try:
            with open(arquivo_json, 'r') as file:
                clientes_existentes = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            clientes_existentes = []

        # Determinar o próximo ID
        if clientes_existentes:
            ultimo_id = max(cliente['id'] for cliente in clientes_existentes)
            novo_id = ultimo_id + 1
        else:
            novo_id = 1

        # Criar o dicionário do novo cliente
        cliente_dict = {"id": novo_id, "cliente": cliente_nome, "endereco": endereco, "telefone": telefone}
        clientes_existentes.append(cliente_dict)

        # Salvar os clientes atualizados no arquivo
        with open(arquivo_json, 'w') as file:
            json.dump(clientes_existentes, file, indent=4)

        print(f"Cliente '{cliente_nome}' salvo com ID {novo_id} no arquivo {arquivo_json} com sucesso!")
    
    @classmethod
    def listar_cliente(cls):

        arquivo_json = "DB/cliente.json"

        try:
            with open(arquivo_json, 'r') as file:
                clientes_existentes = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            clientes_existentes = []

        return clientes_existentes

class FuncionarioDAO(ClienteDAO):
    @classmethod
    def salvar_funcionario(cls, funcionario_nome, endereco, telefone):
            
            arquivo_json = "DB/funcionario.json"
    
            # Tentar carregar funcionarios existentes ou iniciar uma lista vazia
            try:
                with open(arquivo_json, 'r') as file:
                    funcionarios_existentes = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                funcionarios_existentes = []
    
            # Determinar o próximo ID
            if funcionarios_existentes:
                ultimo_id = max(funcionario['id'] for funcionario in funcionarios_existentes)
                novo_id = ultimo_id + 1
            else:
                novo_id = 1
    
            # Criar o dicionário do novo funcionario
            funcionario_dict = {"id": novo_id, "funcionario": funcionario_nome, "endereco": endereco, "telefone": telefone}
            funcionarios_existentes.append(funcionario_dict)
    
            # Salvar os funcionarios atualizados no arquivo
            with open(arquivo_json, 'w') as file:
                json.dump(funcionarios_existentes, file, indent=4)
    
            print(f"Funcionario '{funcionario_nome}' salvo com ID {novo_id} no arquivo {arquivo_json} com sucesso!")
        
    @classmethod
    def listar_funcionario(cls):
        
            arquivo_json = "DB/funcionario.json"
        
            try:
                with open(arquivo_json, 'r') as file:
                    funcionarios_existentes = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                funcionarios_existentes = []
        
            return funcionarios_existentes
    
class VendaDAO:
    @classmethod
    def salvar_venda(cls, produto_id, cliente_id, funcionario_id, quantidade, valor_total, data_venda):
            
            arquivo_json = "DB/venda.json"
    
            # Tentar carregar vendas existentes ou iniciar uma lista vazia
            try:
                with open(arquivo_json, 'r') as file:
                    vendas_existentes = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                vendas_existentes = []
    
            # Determinar o próximo ID
            if vendas_existentes:
                ultimo_id = max(venda['id'] for venda in vendas_existentes)
                novo_id = ultimo_id + 1
            else:
                novo_id = 1
    
            # Criar o dicionário da nova venda
            venda_dict = {"id": novo_id, "produto_id": produto_id, "cliente_id": cliente_id, "funcionario_id": funcionario_id, "quantidade": quantidade, "valor_total": valor_total, "data_venda": data_venda}
            vendas_existentes.append(venda_dict)
    
            # Salvar as vendas atualizadas no arquivo
            with open(arquivo_json, 'w') as file:
                json.dump(vendas_existentes, file, indent=4)
    
            print(f"Venda do produto ID {produto_id} para o cliente ID {cliente_id} pelo funcionário ID {funcionario_id} salva com ID {novo_id} no arquivo {arquivo_json} com sucesso!")
        
    @classmethod
    def listar_venda(cls):
            
                arquivo_json = "DB/venda.json"
            
                try:
                    with open(arquivo_json, 'r') as file:
                        vendas_existentes = json.load(file)
                except (FileNotFoundError, json.JSONDecodeError):
                    vendas_existentes = []
            
                return vendas_existentes
