import time

class conta_banco:

    '''
    Classe que implementa métodos para manipular uma conta bancária.add()
    Atributos: titular (str), saldo (float), limite (float), e histórico (lista de dicionários)

    OBS: Operações no histórico: 0 - sacar, 1- depositar, 2 - transferir

    '''

    def __init__(self, titular: str, saldo: float, limite: float, chave_pix: list, historico: list):

        self.titular = titular # type: ignore
        self.saldo = saldo
        self.limite = limite
        self.historico = historico 
        self.chave_pix = chave_pix
        
        

        '''
        Construtor da classe conta_banco
        '''
    

    def __str__(self):
        return f"Titular: {self.titular}, Saldo: {self.saldo}, Limite: {self.limite}"

    def depositar(self, valor: float, remetente: str = None) -> bool:
        '''
        Método que realiza o depósito na conta bancária
        Entradas: Valor (float) e remetente (str)
        Return: True (se a operação foi realizada com sucesso.)
                False (se a operação não foi realizada.)
        '''
        op = 1
        # Detecta se é uma transferência
        if remetente != None:
            op = 2

        if valor > 0:
            self.saldo += valor
            self.historico.append({'operacao': op,
                                   'remetente': remetente,
                                    'destinatario': self.titular, 
                                    'valor': valor,
                                    'saldo': self.saldo,
                                    'data/tempo': int(time.time())})
            return True
        else:
            print(f'O valor {valor} é inválido')
            return False

    def sacar(self, valor: float, destinatario: str = None) -> bool: 
        '''
        Método que realiza o saque da conta bancária
        Entradas: Valor (float) e destinatario (str)
        Return: True (se a operação foi realizada com sucesso.)
                False (se a operação não foi realizada.)
        '''
        op = 0
        # Detecta se é uma transferência
        if destinatario != None:
            op = 2
                
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append({'operacao': op,
                                   'remetente': self.titular,
                                    'destinatario': destinatario, 
                                    'valor': valor,
                                    'saldo': self.saldo,
                                    'data/tempo': int(time.time())})
            print('saque realizado!')
            return True
        else: 
            a = input(f"deseja utilizar o limite de R$ {self.limite}? (s) para continuar")
            if a == 's':
                if (self.saldo + self.limite) >= valor:
                    self.saldo -= self.limite
                    print('Saque realizado!')
                    return True
                else:
                    print('Saldo e limite insuficientes!')
            else:
                print('Operação com limite cancelada!')
        return False
    
    def transferir(self, destinatario: str, valor: float):
        '''
        Objetivo: metódo para transferir um valor entre duas contas 
        Entradas: valor (float) e objeto da classe conta_banco do destinatário
        Saída: True (se a operação foi realizada com sucesso.)
            False (se a operação não foi realizada.) 
        '''
            # Se o saque ocorrer com sucesso
        if self.sacar(valor, destinatario.titular):
            # Deposita na conta do destinatário
            destinatario.depositar(valor, self.titular)

    def exibir_historico(self) -> None:
        print('Histórico de transações:')
        print('_'*150)
        for item in self.historico:
            dt = time.localtime(item['data/tempo'])
            print('Op:', item['operacao'],
                '\n . Remetente:', item['remetente'],
                '\n . Destinatário:', item['destinatario'],
                '\n . Saldo:', item['saldo'],
                '\n . Valor:', item['valor'],
                '\n . Data e Tempo:',
                str(dt.tm_hour) + ':' + str(dt.tm_min) + ':' + str(dt.tm_sec) + ' / DIA:' + str(dt.tm_mday) + ' MÊS:' + str(dt.tm_mon) + ' ANO:' + str(dt.tm_year))

    def pix(self) -> list:
        return self.chave_pix
    


    '''for conta in banco:
        for chave in conta.chave_pix:
            if chave == chave_pix:
                print'''