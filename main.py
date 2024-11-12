import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'crud-funcionarios'))

from crud_vendas import menu_vendas 
from crud_produtos import menu_produtos
from painel_funcionarios import menu_funcionarios

def menu():
    while True:
        print("\nQue operação deseja realizar?\n")
        print("1. Gerenciar Produtos")
        print("2. Gerenciar Vendas")
        print("3. Gerenciar Funcionários")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            menu_produtos()
        elif escolha == '2':
            menu_vendas()
        elif escolha == '3':
            menu_funcionarios()
        elif escolha == '4':
            print('*** Encerrando programa ***')
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()