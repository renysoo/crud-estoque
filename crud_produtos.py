import json 
import os
from time import sleep 

arquivo = os.path.join(os.path.dirname(__file__), 'crud_produtos.json')

def carregar_produtos():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)

    with open(arquivo, 'r') as f:
        return json.load(f)

def adicionar_produto(id, nome, quantidade, valor):

    if not all([id, nome]) or quantidade <= 0 or valor <= 0:
        print("\nAtenção! todos os campos devem ser preenchidos corretamente.")
        return 

    produtos = carregar_produtos()

    produtos.append({'id': id, 'nome' : nome, 'quantidade' : quantidade, 'valor' : valor}) 
    
    with open(arquivo, 'w') as f: 
        json.dump(produtos, f, indent=4, ensure_ascii=False)
    print("\nProduto adicionado!")

def listar_produtos():
    produtos=carregar_produtos()

    if produtos:
        print("~" *50)
        print("Todos os produtos neste estoque:")
        print("~" *50)

        for produto in produtos:
            print(f"produto {produto['id']} \n id: {produto['id']}\n nome: {produto['nome']}\n quantidade: {produto['quantidade']}\n valor: {produto['valor']}")

            print("*" *50) 
    else:
        print("\nNão há produtos cadastrados.")

def buscar_produto(id):
    produtos = carregar_produtos()

    for produto in produtos:
        if(produto['id']==id):
            print("\nProduto encontrado!")
            print(f'\n produto {produto['id']} \n id: {produto['id']}\n nome: {produto['nome']}\n quantidade: {produto['quantidade']}\n valor: {produto['valor']}')
        else: 
            print("\nProduto não encontrado!")
            break

def atualizar_produtos():
    produtos = carregar_produtos()
    id_atualizar = input("Informe o código do produto que você deseja atualizar: ")

    produto_encontrado = next((p for p in produtos if p['id'] == id_atualizar), None)

    if produto_encontrado:
        novo_nome = input("Digite o novo nome do produto: ")
        novo_id = input("Digite o novo ID para o produto: ")
        novo_valor_produto = input("Digite o novo valor em R$: ")
        nova_qtd_produtos = input("Digite a nova quantidade no estoque: ")

        produto_encontrado['nome'] = novo_nome
        produto_encontrado['id'] = novo_id
        produto_encontrado['valor'] = float(novo_valor_produto)
        produto_encontrado['quantidade'] = int(nova_qtd_produtos)

        with open(arquivo, 'w') as f:
            json.dump(produtos, f, indent=4, ensure_ascii=False)
        
        print(f"\nProduto '{novo_nome}' foi alterado com sucesso!")
    else:
        print("\nProduto não encontrado :/")

def deletar_produtos():
    produtos = carregar_produtos()
    id_produto = input("Digite o código do produto que você deseja apagar: ")
    produto_encontrado = next((p for p in produtos if p['id'] == id_produto), None)
    
    if produto_encontrado:
        produtos.remove(produto_encontrado)
        with open(arquivo, 'w') as f:
            json.dump(produtos, f, indent=4, ensure_ascii=False)
        
        print("\nProduto excluído com sucesso!")
    else:
        print("\nProduto não encontrado :/")
    
def menu_inicial():
    print(" ---->>> Produtos <<<---- ")
    print("          1 - Manejar Produtos")
    print("          2 - Sair ")

def exibir_menu():
    print("\nMENU:")
    print("1. Adicionar novo produto")
    print("2. Listar os produtos cadastrados")
    print("3. Buscar um produto")
    print("4. Atualizar um produto")
    print("5. Deletar um produto")
    print("6. Retornar ao menu principal")


def main():
    
    while True:
        menu_inicial()
        opcao_inicial = int(input("Informe uma opção: "))

        if opcao_inicial == 1:
                while True: 

                    exibir_menu()
                    opcao = input("Indique a sua opção:\n>>>")

                    if opcao == '1':
                        id = input("Código de identificação do produto (id):\n>>>")
                        nome = input("Nome do produto:\n>>>")
                        quantidade = int(input("Quantidade do produto:\n>>>"))
                        valor = float(input("Valor do produto: R$\n>>>"))
                        adicionar_produto(id, nome, quantidade, valor)
                    elif opcao == '2':
                        listar_produtos()
                    elif opcao == '3':
                        id = input("Insira o id para buscar o produto: ")
                        buscar_produto(id)
                    elif opcao == '4':
                        atualizar_produtos()
                    elif opcao == '5':
                        deletar_produtos()
                    elif opcao == '6':
                        print("Você retornará ao menu principal")
                        sleep(3)
                        break
                    else:
                        print("Opção inválida. Por favor, tente novamente")
        elif opcao_inicial == 2:
                print("Encerrando...")
                sleep(3)
                break
        else:
                print("Opção inválida. Por favor, tente novamente")

if __name__ == "__main__":
    main()
