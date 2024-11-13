from crud_funcionarios import *

def menu_funcionarios():
    while True:
        op = menu()
        if op == '1':
            limpar_terminal()
            adicionar_funcionario()
        
        elif op == '2':
            limpar_terminal()
            listar_funcionarios()
        
        elif op == '3':
            limpar_terminal()
            atualizar_funcionario()
        
        elif op == '4':
            limpar_terminal()
            buscar_funcionario() 
        elif op == '5':
            limpar_terminal()
            listar_funcionarios()
            
            id = int(input("Insira o id do funcionário o qual deseja deletar: "))
            
            deletar_funcionario(id)
        elif op == '6':
            print("Encerrando o sistema...")
            break    
        else:
            print("Valor inválido!! Por favor, insira um valor de 1 á 5")
    