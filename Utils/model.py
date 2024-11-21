#! /bin/python3
#model.py

from datetime import datetime as data

class Categoria:
    def __init__(self, id, categoria):
        self.id = id
        self.categoria = categoria

class Produto:
    def __init__(self, id, produto, valor, categoria_id):
        self.id = id
        self.produto = produto
        self.valor = valor
        self.categoria_id = categoria_id

class Fornecedor:
    def __init__(self, id, fornecedor, cnjp, endereco, telefone, email, produto_id, categoria_id):
        self.id = id
        self.fornecedor = fornecedor
        self.cnjp = cnjp
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.produto_id = produto_id
        self.categoria_id = categoria_id

class Cliente:
    def __init__(self, id, cliente, endereco, telefone):
        self.id = id
        self.cliente = cliente
        self.endereco = endereco
        self.telefone = telefone

class Funcionario:
    def __init__(self, id, funcionario, endereco, telefone):
        super().__init__(id, funcionario, endereco, telefone)

class Venda:
    def __init__(self, id, produto_id, cliente_id, funcionario_id, quantidade, valor_total, data_venda):
        self.id = id
        self.produto_id = produto_id
        self.cliente_id = cliente_id
        self.funcionario_id = funcionario_id
        self.quantidade = quantidade
        self.valor_total = valor_total
        self.data_venda = data.now