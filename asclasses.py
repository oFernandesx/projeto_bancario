#as classes

from abc import *#importacao do abstract bases class

class Conta(ABC):#definir a classe como forma abstrata
    @abstractmethod#decorator, define a classe abstrata, por ser abstrata ela nao pode ser instanciada
    def __init__(self, saldo:float = 0):#construtor , definir o saldo como tipo float e o valor inicial de 0
        self.__saldo = saldo#atributo

    def depositar(self, valor:float):#metodo 
        self.__saldo += valor#atributo 

    def sacar(self, valor:float):#metodo
        self.__saldo -= valor#atributo 


    def transferir(self, cpf_destino: str, valor: float):
            if valor > self.__saldo:
                print("Você não tem dinheiro suficiente para fazer a transferência.")
                return
            else:
                self.__saldo -= valor #Tira da conta
            conta_destino.depositar(valor) #Deposita o dinheiro para outra conta
            print(f"Transferência de R${valor} realizada com sucesso para o CPF {cpf_destino}.") 

            conta_destino = Conta.contas.get(cpf_destino)
            if conta_destino is None: #Se a conta não existe, para isso o "is none"
                print("Conta de destino não encontrada.")
                return


    def consultarSaldo(self):
        return self.__saldo
    def setSaldo(self, saldo:float):
        self.__saldo = saldo


class Contacorrente(Conta):#classe que herda de conta(classe abstrata) e puxa o atributo com o super
    def __init__(self, saldo:float=0):
        super().__init__(saldo)
        self.tipo = "Conta Corrente"
    
            


class Contapoupanca(Conta):#classe que herda de conta(classe abstrata) e puxa o atributo com o super
    def __init__(self, saldo:float=0):#contrutor
        super().__init__(saldo)
        self.tipo = "Conta poupança"
    

            
        

class Cliente:
    def __init__(self, nome:str, cpf:str, senha: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = senha
        self.__contas = []
    
    def adicionarConta(self, conta):
        self.__contas.append(conta)
    def removerConta(self, conta):
        self.__contas.pop(conta)

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_senha(self):
        return self.__senha

    def contas(self):
        return self.__contas



class Extrato:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, descricao: str, valor: float):
        transacao = f"{descricao}: R${valor: }"
        self._transacoes.append(transacao)

    def consultar_extrato(self):#metodo que retorna a lista "self.__transacoes"
        return self._transacoes



class Banco:
    def __init__(self):
        self._clientes = []

    def adicionar_cliente(self, cliente:str):
        self._clientes.append(cliente)

    def remover_cliente(self, cliente:str):
        if cliente in self._clientes:
            self._clientes.pop(cliente)
        
    def clientes(self):#metodo que retorna a lista "self._clientes"
        return self._clientes