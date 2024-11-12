import json
import os

arquivo = os.path.join(os.path.dirname(__file__), 'vendas.json')

def carregar_vendas():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)
    # Carrega o conteúdo do arquivo
    with open(arquivo, 'r') as f:
        return json.load(f)

lista_vendas = carregar_vendas()

def cadastrar_venda():
    venda = {}
    if len(lista_vendas) == 0:
        venda["id"] = 1
    else:
        venda["id"] = lista_vendas[len(lista_vendas)-1]["id"]+1
    venda["itens_pedido"] = itens_venda()
    venda["id_funcionario"] = input('Digite o código do vendedor responsável pela venda: ')
    venda["valor"] = input("Digite o valor total da venda: ")
    lista_vendas.append(venda)
    salvar_vendas()
    print("\nProduto cadastrado com sucesso!")
    
def itens_venda():
    itens = {}
    while True:
        id_item = int(input("Qual o id do produto vendido? "))
        itens[id_item] = int(input("Digite a quantidade de produtos vendidos: "))
        continua = input("Deseja continuar? s ou n: ").lower()
        if continua == 'n':
            return itens
    
def listar_vendas():
    print("\n*** Listando vendas ***\n")
    for venda in lista_vendas:
        print(f"Id da venda: {venda["id"]}")
        print(f"Itens da venda:")
        for item in venda["itens_pedido"]:
            print(f"  ID do Produto: {item} || Quantidade: {venda["itens_pedido"][item]}")            
        print(f"Id do vendedor: {venda["id_funcionario"]}")
        print(f"Valor da venda: {venda["valor"]}\n")
    if len(lista_vendas) == 0:
        print("Nenhuma venda cadastrada\n")
        
def editar_vendas():    
    editar = int(input("Qual venda voce deseja editar? Digite o id: "))
    venda_editada = False
    for venda in lista_vendas:
        if editar == venda["id"]:
            venda["itens_pedido"] = itens_venda()
            venda["id_funcionario"] = input('Digite o código do vendedor responsável pela venda: ')
            venda["valor"] = input("Digite o valor total da venda: ")
            print("Venda editada")
            venda_editada = True
    salvar_vendas()
    if not venda_editada:
        print("\nVenda não encontrada.\n")

            
def deletar_vendas():
    apagar = int(input("Qual venda voce deseja deletar? Digite o id: "))
    venda_deletada = False
    for venda in lista_vendas:
        if apagar == venda["id"]:
            venda_deletada = True
            lista_vendas.remove(venda)
            print("\nVenda deletada\n")
    salvar_vendas()
    if not venda_deletada:
        print("\nVenda não encontrada.\n")


def salvar_vendas():
    with open(arquivo, 'w') as f:
        json.dump(lista_vendas, f, indent=4, ensure_ascii=False)

def buscar_venda():
    busca_id = int(input("Digite o ID da venda que deseja buscar: "))
    venda_encontrada = False
    for venda in lista_vendas:
        if venda["id"] == busca_id:
            venda_encontrada = True
            print(f"\nId da venda: {venda['id']}")
            print(f"Itens da venda:")
            for item in venda["itens_pedido"]:
                print(f"  ID do Produto: {item} || Quantidade: {venda['itens_pedido'][item]}")
            print(f"Id do vendedor: {venda['id_funcionario']}")
            print(f"Valor da venda: {venda['valor']}\n")
            break
    if not venda_encontrada:
        print("\nVenda não encontrada.\n")

def menu_vendas():
    while True:
        escolha = input("\nSelecione a operação desejada:\n1 - Cadastrar venda\n2 - Listar vendas\n3 - Buscar vendas\n4 - Editar vendas\n5 - Deletar vendas\nOutros: voltar ao menu \n")
        match(escolha):
            case '1':
                cadastrar_venda()
            case '2':
                listar_vendas()
            case '3':
                buscar_venda()
            case '4':
                editar_vendas()
            case '5': 
                deletar_vendas()
            case __:
                print("Voltando ao menu")
                break
        

    
            
