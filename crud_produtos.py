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
        print("Produto não encontrado :/")

def deletar_produtos():
    produtos = carregar_produtos()
    id_produto = input("Digite o código do produto que você deseja apagar: ")
    produto_encontrado = next((p for p in produtos if p['id'] == id_produto), None)
    
    if produto_encontrado:
        produtos.remove(produto_encontrado)
        with open(arquivo, 'w') as f:
            json.dump(produtos, f, indent=4, ensure_ascii=False)
        
        print("Produto excluído com sucesso!")
    else:
        print("Produto não encontrado :/")