#! /bin/python3

from DAO import *

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
            for categoria in categorias:
                print(f'ID: {categoria.id}, Categoria: {categoria.categoria}')
        except ValueError as e:
            return str(e)
        except Exception as e:
            return f"Erro inesperado: {e}"


def main():
    print("=" * 20 + " Categorias " + "=" * 20)
    cat1 = input("Digite o nome da categoria: ")
    CategoriaController.salvar_categoria(cat1)
    #CategoriaController.listar_categoria()
    print("="*52)

'''
    ProdutoDAO.salvar_produto("Arroz", 5.0, 1)
    ProdutoDAO.salvar_produto("Feijão", 6.0, 1)
    ProdutoDAO.salvar_produto("Macarrão", 3.0, 1)
    ProdutoDAO.salvar_produto("Refrigerante", 4.0, 2)
    ProdutoDAO.salvar_produto("Suco", 3.0, 2)
    ProdutoDAO.salvar_produto("Detergente", 2.0, 3)
    ProdutoDAO.salvar_produto("Sabão em pó", 8.0, 3)

    produtos = ProdutoDAO.listar_produto()
    for produto in produtos:
        print(f'ID: {produto["id"]}, Produto: {produto["produto"]}, Valor: R$ {produto["valor"]}, Categoria ID: {produto["categoria_id"]}')

    FornecedorDAO.salvar_fornecedor("Mercado A", "123456789", "Rua A, 123", "12345678", "test@teste.com", 1, 1)
    FornecedorDAO.salvar_fornecedor("Mercado B", "987654321", "Rua B, 456", "87654321", "test@teste.com", 2, 2)

    fornecedores = FornecedorDAO.listar_fornecedor()
    for fornecedor in fornecedores:
        print(f'ID: {fornecedor["id"]}, Fornecedor: {fornecedor["fornecedor"]}, CNPJ: {fornecedor["cnpj"]}, Endereço: {fornecedor["endereco"]}, Telefone: {fornecedor["telefone"]}, Email: {fornecedor["email"]}, Produto ID: {fornecedor["produto_id"]}, Categoria ID: {fornecedor["categoria_id"]}')

    ClienteDAO.salvar_cliente("João", "Rua C, 789", "98765432")
    ClienteDAO.salvar_cliente("Maria", "Rua D, 012", "12345678")

    clientes = ClienteDAO.listar_cliente()
    for cliente in clientes:
        print(f'ID: {cliente["id"]}, Cliente: {cliente["cliente"]}, Endereço: {cliente["endereco"]}, Telefone: {cliente["telefone"]}')

    FuncionarioDAO.salvar_funcionario("José", "Rua E, 345", "87654321")
    FuncionarioDAO.salvar_funcionario("Ana", "Rua F, 678", "23456789")

    funcionarios = FuncionarioDAO.listar_funcionario()
    for funcionario in funcionarios:
        print(f'ID: {funcionario["id"]}, Funcionário: {funcionario["funcionario"]}, Endereço: {funcionario["endereco"]}, Telefone: {funcionario["telefone"]}')

    VendaDAO.salvar_venda(1, 1, 1, 2, 10.0, "2021-09-01")
    VendaDAO.salvar_venda(2, 2, 2, 3, 12.0, "2021-09-02")

    vendas = VendaDAO.listar_venda()
    for venda in vendas:
        print(f'ID: {venda["id"]}, Produto ID: {venda["produto_id"]}, Cliente ID: {venda["cliente_id"]}, Funcionário ID: {venda["funcionario_id"]}, Quantidade: {venda["quantidade"]}, Valor Total: R$ {venda["valor_total"]}, Data da Venda: {venda["data_venda"]}')
'''
if __name__ == "__main__":
    main()