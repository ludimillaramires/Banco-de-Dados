""" 
Autor: Ludimilla Alves Ramires Rodrigues 
Curso: Análise e Desenvolvimento de Sistemas 
 
""" 
import json

def mostrar_menu_principal():
    print("\n=Menu Principal=")
    print("1. Estudantes\n2. Professores\n3. Disciplinas\n4. Turmas")
    print("5. Matrículas\n6. Sair")
    return input("Escolha uma opção: ")


def mostrar_menu_operacoes():
    print("\nMenu de Operações\n1. Incluir\n2. Listar\n3. Atualizar\n4. Excluir\n5. Voltar")
    return input ("Escolha uma opção: ")

def incluir_cadastro(nome_arquivo):
    lista_qualquer = ler_arquivo(nome_arquivo)

    try:
        codigo = input("Digite o código: ")
    except EOFError:
        print("\nEntrada interrompida. Cadastro cancelado.")
        return

    for item in lista_qualquer:
        if item["cod"] == codigo:
            print("Erro: Código já existe!")
            return
        
    novo_cadastro = {"cod": codigo}

    try:
        if "estudantes" in nome_arquivo or "professores" in nome_arquivo:
            nome = input("Digite o nome: ")
            cpf = input("Digite o CPF: ")
            novo_cadastro["nome"] = nome
            novo_cadastro["cpf"] = cpf

        elif "disciplinas" in nome_arquivo:
            nome = input("Digite o nome da disciplina: ")
            novo_cadastro["nome"] = nome

        elif "turmas" in nome_arquivo:
            cod_prof = input("Digite o código do professor: ")
            cod_disc = input("Digite o código da disciplina: ")
            novo_cadastro["cod_professor"] = cod_prof
            novo_cadastro["cod_disciplina"] = cod_disc

        elif "matriculas" in nome_arquivo:
            cod_turma = input("Digite o código da turma: ")
            cod_estudante = input("Digite o código do estudante: ")
            novo_cadastro["cod_turma"] = cod_turma
            novo_cadastro["cod_estudante"] = cod_estudante

        else:
            print("Arquivo desconhecido. Não foi possível incluir.")
            return
    except EOFError:
        print("\nEntrada interrompida. Cadastro cancelado.")
        return

    lista_qualquer.append(novo_cadastro)
    salvar_arquivo(lista_qualquer, nome_arquivo)
    print(f"Cadastro {codigo} incluído com sucesso!")

def mostrar_cadastros(nome_arquivo):
    lista_qualquer = ler_arquivo(nome_arquivo)
    if len(lista_qualquer) == 0:
        print("Nenhum registro encontrado.")
        return
    
    for i, cadastro in enumerate(lista_qualquer, 1):
        print(f"\nCadastro {i}")
        for chave, valor in cadastro.items():
            print(f"{chave.capitalize()}: {valor}")

def editar_cadastro(codigo, nome_arquivo):
    lista_qualquer = ler_arquivo(nome_arquivo)
    for cadastro in lista_qualquer:
        if cadastro["cod"] == codigo:
            
            if "professores" in nome_arquivo or "estudantes" in nome_arquivo:
                cadastro["nome"] = input("Digite o novo nome: ")
                cadastro["cpf"] = input("Digite o novo CPF: ")

            elif "disciplinas" in nome_arquivo:
                cadastro["nome"] = input("Digite o novo nome da disciplina: ")

            elif "turmas" in nome_arquivo:
                cadastro["cod_professor"] = input("Digite o novo código do professor: ")
                cadastro["cod_disciplina"] = input("Digite o novo código da disciplina: ")

            elif "matriculas" in nome_arquivo:
                cadastro["cod_turma"] = input("Digite o novo código da turma: ")
                cadastro["cod_estudante"] = input("Digite o novo código do estudante: ")

            salvar_arquivo(lista_qualquer, nome_arquivo)
            print("Cadastro atualizado com sucesso! ")
            return
        
    print("Código não encontrado.")

def remover_cadastro(codigo, nome_arquivo):
    cadastro_para_remover = None
    lista_qualquer = ler_arquivo(nome_arquivo)
    for cadastro in lista_qualquer:
        if cadastro["cod"] == codigo:
            cadastro_para_remover = cadastro
            break

    if cadastro_para_remover is not None:
        lista_qualquer.remove(cadastro_para_remover)
        salvar_arquivo(lista_qualquer, nome_arquivo)
        print("Cadastro removido com sucesso! ")
    else:
        print("Código não encontrado. ")

def salvar_arquivo(lista_qualquer, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo_aberto:
        json.dump(lista_qualquer, arquivo_aberto)
    
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_aberto:
            lista_qualquer = json.load(arquivo_aberto)

        return lista_qualquer
    except FileNotFoundError:
        return []

def processar_menu_operacoes(opcao_secundaria, nome_arquivo):

    if opcao_secundaria == "1": # Incluir cadastro
        incluir_cadastro(nome_arquivo)
                 
    elif opcao_secundaria == "2": # Listar cadastros 
        mostrar_cadastros(nome_arquivo)

    elif opcao_secundaria == "3": # Atualizar
        codigo = input("Digite o código para editar:" )
        editar_cadastro(codigo, nome_arquivo)

    elif opcao_secundaria == "4": # Excluir
        codigo = input("Digite o código para remover: ")
        remover_cadastro(codigo, nome_arquivo)

    elif opcao_secundaria == "5": # Voltar ao Menu Principal 
        print("Voltando ao menu principal...")
        return False
    else:
        print("Opção inválida, tente novamente. ")
    
    return True

arquivo_estudantes = "estudantes.json"
arquivo_professores = "professores.json"
arquivo_disciplinas = "disciplinas.json"
arquivo_turmas = "turmas.json"
arquivo_matriculas = "matriculas.json"

def processar_menu_principal(): 
    while True: 
        opcao = mostrar_menu_principal()
 
        if opcao == "1": 
            print(f"Você escolheu Estudantes") 
            while True:  
                opcao_secundaria = mostrar_menu_operacoes()
                if not processar_menu_operacoes(opcao_secundaria, arquivo_estudantes):
                    break
                
        elif opcao == "2": 
            print(f"Você escolheu Professores") 
            while True:  
                opcao_secundaria = mostrar_menu_operacoes()
                if not processar_menu_operacoes(opcao_secundaria, arquivo_professores):
                    break

        elif opcao == "3": 
            print(f"Você escolheu Disciplinas") 
            while True:  
                opcao_secundaria = mostrar_menu_operacoes()
                if not processar_menu_operacoes(opcao_secundaria, arquivo_disciplinas):
                    break

        elif opcao == "4": 
            print(f"Você escolheu Turmas") 
            while True:  
                opcao_secundaria = mostrar_menu_operacoes()
                if not processar_menu_operacoes(opcao_secundaria, arquivo_turmas):
                    break

        elif opcao == "5": 
            print(f"Você escolheu Matriculas") 
            while True:  
                opcao_secundaria = mostrar_menu_operacoes()
                if not processar_menu_operacoes(opcao_secundaria, arquivo_matriculas):
                    break

        elif opcao == "6":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida, tente novamente")
 
# Iniciar o menu principal 
processar_menu_principal()