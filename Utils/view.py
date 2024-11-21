#! /usr/bin/python3

from controller import *

def main():
    Inicializar()
    Inicializar.limpar_tela()

    def sub_menu(itens):
        print("=" * 20 + " Categorias " + "=" * 20)
        for i in itens:
            print(f"{i} - {itens[i]}")
        print("0 - Sair\n")

    def categoria():
        while True:
            lista_sub_menu = {
                "1": "Cadastrar Categoria", 
                "2": "Listar Categorias", 
                "3": "Limpar Tela"
            }
            sub_menu(lista_sub_menu)
            opcao = input("Digite a opção desejada: ")
            print("=" * 52)

            if opcao == "1":
                Inicializar.limpar_tela()
                print("=" * 20 + " Categorias " + "=" * 20)
                cat1 = input("Digite o nome da categoria ou 'c' para cancelar: ")
                if cat1 == "c":
                    Inicializar.limpar_tela()
                    categoria()
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

    def produto():
        pass

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
                categoria()
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

    while True:
        menu()

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