#OS DEFS
	
from asclasses import *#importa as classes
import os


banco_one = Banco()
senha_adm = "ADMINISTRADOR07"#definir a senha pro adm

def menu(): #Menu principal do banco
    print("======================================================")
    print("BEM VINDO AO ONE BANK")
    print("======================================================")
    print("O que deseja fazer?\n1. Login\n2. Cadastrar\n3. Entrar como ADM\n4. Sair")
    print("======================================================")
    escolha = int(input("--> "))
    return escolha

def cadastrar(): #Menu para cadastrar uma nova conta
    print("======================================================")
    print("CADASTRAR UMA CONTA")
    print("======================================================")
    nome = input("Informe seu nome: ")
    cpf = int(input("Informe seu CPF: "))
    senha = input("Informe sua senha: ")
    cliente_cadastrado = Cliente(nome, cpf, senha)#instancia o cliente
    #clientes.append(cliente_cadastrado)
    banco_one.adicionar_cliente(cliente_cadastrado)#adiciona o cliente instanciado na lista cliente
    while True:
            try:
                print("======================================================")
                print("Qual o tipo de conta que deseja cadastrar\n")
                print("1. Conta corrente\n2. Conta poupança")
                tipo_conta = int(input("--> "))#pede o tipo da conta
                match tipo_conta:
                    case 1:
                        conta = Contacorrente()#defini a conta como corrente
                    case 2:
                        conta = Contapoupanca()#defini a conta como poupanca
                    case _:
                        os.system("cls")
                        print('Informacao incorreta')
                        os.system('pause')
                        

                conta.setSaldo(0)#defini o saldo como 0

                cliente_cadastrado.adicionarConta(conta)#ele passa o objeto e usa o metodo adicionar_conta passando o parametro conta
                print("======================================================")
                print("Sua conta foi criada com sucesso :)")
                os.system('pause')
                os.system("cls")
                return cliente_cadastrado
            
            except Exception as e:
                    os.system('cls')
                    print(f'Opção inválida, o erro foi {e}')
                    os.system('pause')
                    os.system("cls")


def login(): #Menu quando o usuário fizer o login após ter feito o cadastro
    os.system("cls")
    print("======================================================")
    print("FAZER LOGIN")
    print("======================================================")
    cpf = int(input("Informe seu CPF: "))
    senha = input("Informe sua senha: ")

    for i in banco_one.clientes():
        if cpf == i.get_cpf() and senha == i.get_senha(): #Se o CPF estiver no get_cpf e a senha estiver dentro do get_senha, a pessoa entra na conta
            os.system("pause")
            os.system("cls")
            print("======================================================")
            print(f"Seja bem vindo(a), {i.get_nome()}!")
            return i
    print("")
    print("CPF ou senha incorretos.") #Se não, ou o cpf ou a senha estão incorretos
    os.system("pause")
    os.system("cls")
    return None#sair da funcao



def menu_cliente(cliente): #O menu do cliente após ele fazer o login
    while True:
        print("======================================================")
        print("O que deseja fazer?\n1. Ver informações da conta\n2. Depositar\n3. Sacar\n4. Transferir\n5. Adicionar ou remover conta\n6. Sair")
        print("======================================================")
        try:
            escolha = int(input("--> "))
            match escolha:
                case 1:
                    os.system("cls")
                    print("======================================================")
                    print("INFORMAÇÕES DA CONTA")
                    print(f"Nome: {cliente.get_nome()}")
                    print(f"CPF: {cliente.get_cpf()}")
                    for conta in cliente.contas():#ele percorre a lista contas
                        print(f"Tipo de conta: {conta.tipo}, Saldo: R${conta.consultarSaldo()}")
                    print("")
                    os.system('pause')
                    os.system("cls")

                case 2: 
                    os.system("cls")
                    print("======================================================")
                    print("REALIZAR DEPOSITO")
                    print("======================================================")
                    print("Qual conta deseja depositar?")
                    contas_cliente = cliente.contas()#ele cria uma variavel que armazena a lista de contas(conta corrente ou conta poupanca)
                    count_dep = 1#contador para deposito
                    for dep in contas_cliente:#percorre a variavel criada 
                        print(f"{count_dep}° conta: {dep.tipo}, Saldo: R${dep.consultarSaldo()}")
                        count_dep += 1
                    escolha_depositar = int(input("--> "))
                    os.system('cls')
                    print("")
                    if escolha_depositar > count_dep:
                        
                        print("Opção inválida")
                        os.system('pause')
                        os.system('cls')

                    else:
                        valor = float(input("Digite o valor que deseja depositar: R$"))
                        contas_cliente[escolha_depositar-1].depositar(valor)
                        print("Deposito realizado com sucesso!")
                        os.system('cls')
                        os.system('cls')








                case 3: #ARRUMAR O SAQUE
                    os.system("cls")
                    print("======================================================")
                    print("REALIZAR SAQUE")
                    print("======================================================")
                    print("De qual conta deseja sacar?")
                    contas_cliente2 = cliente.contas()
                    count_saq = 1
                    for saq in contas_cliente2:
                        print(f"{count_saq}° conta: {saq.tipo}, Saldo: R${saq.consultarSaldo()}")
                        count_saq += 1
                    escolha_sacar = int(input("--> "))
                    print("")
                    try:
                        if escolha_sacar > count_saq or escolha_sacar <= 0:
                            os.system('cls')
                            print("Opção inválida")
                            os.system('pause')
                            os.system('cls')
                        

                        else:
                            valor_saq = float(input("Digite o valor que deseja sacar: R$"))
                            for i in contas_cliente2:
                                if i.tipo == "Conta poupança":
                                    if valor_saq < 100:
                                        os.system('cls')
                                        print('voce nao pode realizar um saque menor que R$100,00 reais')
                                        os.system('pause')
                                        os.system('cls')

                                    else:
                                        contas_cliente2[escolha_sacar-1].sacar(valor_saq)
                                        os.system('cls')
                                        print("Saque realizado com sucesso!")
                                        os.system('pause')
                                        os.system('cls')

                                else:
                                    contas_cliente2[escolha_sacar-1].sacar(valor_saq)
                                    print("Saque realizado com sucesso!")
                                    os.system('pause')
                                    os.system('cls')

                                    
                    except Exception as e:
                            print(f'Opção inválida, o erro foi {e}')

                case 4:
                        os.system("cls")
                        print("======================================================")
                        print("MENU DE TRANSFERÊNCIA")
                        print("======================================================")
                        
                        while True:
                            print("O que você deseja fazer?")
                            print("1. Transferir dinheiro para uma conta\n2. Sair")
                            transferir = int(input("-->"))
                            
                            if transferir == 1:
                                contas_cliente3 = cliente.contas()
                                print("Suas contas:")
                                for i, conta in contas_cliente3:
                                    print(f"{i+1}° conta: {conta.tipo}, Saldo: R${conta.consultarSaldo()}")
                                escolha_conta = input(("Qual conta você deseja escolher? \n --> "))


                                transferencia = float(input("Insira o valor da transferência: R$ "))
                                cpf_destino = input("Insira o CPF do destinatário: ")
                

                                if transferencia <= 0:
                                    print("Valor inválido. Insira um valor positivo.")

                                elif contas_cliente3[escolha_conta].tipo == "Contapoupanca":
                                    print("Não é possível transferir de uma conta poupança.")

                                elif transferencia > contas_cliente3[escolha_conta].consultarSaldo():
                                    print("Você não tem dinheiro suficiente para fazer a transferência.")

                                else:
                                    contas_cliente3[escolha_conta].transferir(cpf_destino, transferencia)
                                    print("Transferência realizada com sucesso!")
                            
                            elif transferir == 2:
                                print("Saindo...")
                                return
                            
                            else:
                                print("Opção inválida. Tente novamente.")

                case 5:
                    import os

                    while True:
                        os.system("cls") 
                        print("======================================================")
                        print("ADICIONAR OU REMOVER CONTAS")
                        print("======================================================")
                        print("O que deseja fazer?\n1. Adicionar conta\n2. Remover uma conta\n3. Voltar")

                        try:
                            add_rmv_conta = int(input("--> "))
                            os.system('cls')
                            match add_rmv_conta:
                                case 1:
                                    try:
                                        contas_cliente2 = cliente.contas()
                                        if len(contas_cliente2) == 0:  # Corrigido aqui
                                            print('1. Adicionar Conta Poupança ')
                                            print('2. Adicionar Conta Corrente')
                                            print('3. Sair')
                                            escolha = int(input('Qual opção você deseja? \n--> '))
                                            os.system('cls')
                                            match escolha:
                                                case 1:
                                                    tipo_conta = Contapoupanca()
                                                    tipo_conta.setSaldo(0)
                                                    cliente.adicionarConta(tipo_conta)
                                                    print("Conta adicionada com sucesso!") 
                                                case 2:
                                                    tipo_conta = Contacorrente()
                                                    tipo_conta.setSaldo(0)
                                                    cliente.adicionarConta(tipo_conta)
                                                    print("Conta adicionada com sucesso!") 
                                                case 3:
                                                    pass
                                                case _:
                                                    print("Opção inválida\nTente novamente")
                                        else:
                                            for i in contas_cliente2:
                                                if i.tipo == "Conta poupança":
                                                    print('1. Adicionar Conta Corrente ')
                                                    print('2. Sair')
                                                    escolha = int(input('Qual opcao deseja\n--> '))
                                                    os.system('cls')
                                                    match escolha:
                                                        case 1:
                                                            tipo_conta = Contacorrente()
                                                            tipo_conta.setSaldo(0)
                                                            cliente.adicionarConta(tipo_conta)
                                                            print("Conta adicionada com sucesso!") 
                                                        case 2:
                                                            pass  # Sair
                                                        case _:
                                                            print("Opção inválida\nTente novamente")

                                                elif i.tipo == "Conta Corrente":
                                                    print('1. Adicionar Conta Poupança ')
                                                    print('2. Sair')
                                                    escolha = int(input('Qual opção você deseja? \n--> '))
                                                    os.system('cls')
                                                    match escolha:
                                                        case 1:
                                                            tipo_conta = Contapoupanca()
                                                            tipo_conta.setSaldo(0)
                                                            cliente.adicionarConta(tipo_conta)
                                                            print("Conta adicionada com sucesso!") 

                                    except ValueError:
                                        print("Por favor, insira um número válido.")
                                    except Exception as e:
                                        print(f'Ocorreu um erro: {e}')

                                case 2:
                                    print("Qual conta deseja remover?")
                                    count = 1
                                    contas = cliente.contas()
                                    for rmv in contas:
                                        print(f"{count}° conta: {rmv.tipo}, Saldo: R${rmv.consultarSaldo()}")
                                        count += 1
                                    
                                    try:
                                        rmv_conta = int(input("Qual conta você deseja remover?\n--> "))
                                        if 1 <= rmv_conta <= len(contas):
                                            cliente.removerConta(rmv_conta - 1)
                                            print("A conta foi excluída com sucesso!")
                                        else:
                                            print("Número da conta inválido.")
                                    except ValueError:
                                        print("Por favor, insira um número válido.")
                                    except Exception as e:
                                        print(f'Ocorreu um erro: {e}')

                                case 3:
                                    os.system('cls')
                                    print('...')  # Implementar lógica de saída se necessário
                                    break
                                case _:
                                    print("Opção inválida\nTente novamente")

                        except ValueError:
                            print("Por favor, insira um número válido.")
                        except Exception as e:
                            print(f'Ocorreu um erro: {e}')

                        os.system('pause')


                case 6:
                    print("Saindo...")
                    os.system("pause")
                    os.system("cls")
                    break

                case _:
                    print("Opção inválida")

        except Exception as e:
            print(f'Opção inválida, o erro foi {e}')

def menu_adm():
    while True:
        print("======================================================")
        print("SESSÃO DO ADM")
        print("======================================================")
        print("")
        print("Para entrar como administrador, insira a senha\ndigite 0 para sair!")
        verificação = input("--> ")
        if verificação == "0":
            print("Saindo...")
            break
        
        if verificação == senha_adm:
            os.system("cls")
            while True:
                try:
                    print("======================================================")
                    print("BEM VINDO ADMINISTRADOR!")
                    print("======================================================")
                    print("O que deseja fazer?\n1. Adicionar cliente\n2. Remover cliente\n3. Ver clientes\n4. Sair")
                    print("======================================================")
                    
                    escolha = int(input("--> "))
                    break

                except Exception as e:
                    print(f'Opção inválida, o erro foi {e}')

                if escolha == 1:
                    os.system('pause')
                    os.system("cls")
                    print("======================================================")
                    print("ADICIONAR CLIENTE")
                    print("======================================================")
                    nome = input("Informe seu nome: ")
                    cpf = int(input("Informe seu CPF: "))
                    senha = input("Informe sua senha: ")
                    cliente_cadastrado = Cliente(nome, cpf, senha)
                    banco_one.adicionar_cliente(cliente_cadastrado)
                    print("======================================================")
                    try:
                        print("Qual o tipo de conta que deseja cadastrar\n")
                        print("1. Conta corrente\n2. Conta poupança")
                        tipo_conta = int(input("--> "))
                        break

                    except Exception as e:
                        print(f'Opção inválida, o erro foi {e}')
                        
                    match tipo_conta:
                        case 1:
                            conta = Contacorrente()
                        case 2:
                            conta = Contapoupanca()
                            
                        case _:
                            print('Informação invalida')
                        
                    conta.setSaldo(0)
                    
                    cliente_cadastrado.adicionarConta(conta)
                    print("======================================================")
                    print("O Cliente foi criado com sucesso :)")
                    os.system('pause')
                    os.system("cls")
                
                elif escolha == 2:
                    os.system('pause')
                    os.system("cls")
                    print("======================================================")
                    print("REMOVER CLIENTE")
                    cpf_remover = input("Digite o CPF do cliente a ser removido: ")
                    cliente_remover = banco_one.remover_cliente(cpf_remover)
                    if cliente_remover:
                        print("Cliente removido com sucesso!")
                    else:
                        print("Cliente não encontrado.")

                
                elif escolha == 3:
                    os.system('pause')
                    os.system("cls")
                    print("======================================================")
                    print("LISTA DE CLIENTES CADASTRADOS")
                    print("")

                    contas_cliente2 = banco_one.clientes()
                    count_cli = 1
                    for cli in contas_cliente2:
                        print(f"{count_cli}° Cliente: {cli.get_nome()}, CPF: {cli.get_cpf()}")
                        count_cli += 1
                    os.system('pause')
                    os.system("cls")

                elif escolha == 4:
                    print("Saindo...")
                    os.system('pause')
                    os.system("cls")
                    break
            
                else:
                    print("Opção inválida. Tente novamente.")
                    os.system("pause")
            
        else:
                print("Senha inválida!")
                os.system('pause')
                os.system('cls')