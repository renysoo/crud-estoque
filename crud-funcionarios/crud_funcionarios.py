import json
import os
from time import sleep

funcionarios_json = os.path.join(os.path.dirname(__file__), 'funcionarios.json')

def validar_salario(salario):
    while True:
        try:
            entrada = float(salario)
            return entrada
        except:
            entrada = input("Por favor, insira um valor numérico: R$")


def limpar_terminal():
    sistema = os.name
    if sistema == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def atualizarJSON(funcionarios):
    with open(funcionarios_json, 'w') as f:
        json.dump(funcionarios, f, indent=4, ensure_ascii=False)
    

def carregar_funcionarios():
    if not os.path.exists(funcionarios_json):
        with open(funcionarios_json, 'w') as f:
            json.dump([], f, indent = 4)
        
    with open(funcionarios_json, 'r') as f:
        return json.load(f)
    
def adicionar_funcionario():
    print("\n|--------| Cadastro de Funcionário |--------|")

    funcionarios = carregar_funcionarios()
    
    nome = input("\nInsira o nome do funcionário novo: ")
    cargo = input("Insira o cargo do funcionário novo: ")
    
    salario = validar_salario((input("Insira o salario do funcionário novo (minimo R$400): R$")))
    while salario < 400:
        salario = validar_salario(input("Por favor, insira pelo menos R$400: R$"))
        
    setor = input("Insira o setor que o funcionário pertence: ")

    if funcionarios == []:
        id = 1
    else:
        for funcionario in funcionarios:
            if funcionario:
                id = funcionario['id'] + 1
    

    funcionarios.append({'id': id, 'nome': nome, 'cargo' : cargo, 'salario' : salario, 'setor' : setor})

    atualizarJSON(funcionarios)
    print(f"{nome} adicionado com sucesso!")
    
def listar_funcionarios():
    funcionarios = carregar_funcionarios()

    if(funcionarios):
        print("\n|--------| Lista de Funcionários |--------|")
        
        for funcionario in funcionarios:
            print(f"\nid: {funcionario['id']}")
            print(f"Nome: {funcionario['nome']}")
            print(f"Cargo: {funcionario['cargo']}")
            print(f"Salário: {funcionario['salario']}")
            print(f"Setor: {funcionario['setor']}")

    else:
        print("Sem funcionários cadastrados")

def atualizar_funcionario():
    print("\n|--------| Atualizar Funcionário |--------|")

    funcionarios = carregar_funcionarios()
    listar_funcionarios()
    atributos_validos = ['nome', 'cargo', 'salario', 'setor']
        
    id = int(input("\nInsira o id correspondente ao funcionário a ser editado: "))
        
    for funcionario in funcionarios:
        if funcionario['id'] == id:
            print(f"\nDados atuais: ")
            print(f"\nNome: {funcionario['nome']}")
            print(f"Cargo: {funcionario['cargo']}")
            print(f"Salário: {funcionario['salario']}")
            print(f"Setor: {funcionario['setor']}")
            
                
            dado_alterado = input("\nDigite o que deseja mudar: ").lower()
            
            if dado_alterado in atributos_validos:
                novo_dado = input(f"\nInsira o novo {dado_alterado}: ")
                print(f"{funcionario['nome']} alterado com sucesso!") 
                funcionario[f'{dado_alterado}'] = novo_dado
                
                atualizarJSON(funcionarios)
                print(f"\nNovos dados: ")
                listar_funcionarios()
                
                
            else:
                print("Atributo inválido.")
            
            return
    print(f"Nenhum funcionário com o id {id} encontrado.")
    
    atualizarJSON(funcionarios)
    

def buscar_funcionario():
    print("\n|--------| Busca de Funcionário |--------|")

    funcionarios = carregar_funcionarios()
    
    id = int(input("Insira o id do funcionário que deseja buscar: "))
    
    for funcionario in funcionarios:
        if funcionario['id'] == id:
            print(f"Nome: {funcionario['nome']}")
            print(f"Cargo: {funcionario['cargo']}")
            print(f"Salário: {funcionario['salario']}")
            print(f"Setor: {funcionario['setor']}")
            
            return
    print("Nenhum funcionário com este id cadastrado no sistema.")
            
def deletar_funcionario(id):
    print("\n|--------| Deletar Funcionário |--------|")

    funcionarios = carregar_funcionarios()

    for funcionario in funcionarios:  
        if funcionario['id'] == id:
            funcionarios.remove(funcionario)
            print(f"{funcionario['nome']} excluido com sucesso!")
            break

    atualizarJSON(funcionarios)


def menu():
    print("\n|------------| Gestão de Funcionários |------------|")
    print("\n1- Cadastrar funcionário.")
    print("2- Listar funcionários.")
    print("3- Atualizar dados de um funcionário.")
    print("4- Buscar funcionário.")
    print("5- Deletar funcionário.")
    print("\n6- Encerrar programa.")
    return input("\nInsira o código da sua atividade:")



