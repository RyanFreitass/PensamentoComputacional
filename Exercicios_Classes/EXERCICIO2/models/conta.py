class ContaBancaria:
    def __init__(self, titular, saldo, limite, historico):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = []
    
    def deposito(self, valor: float):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Valor de depósito: {valor:.2f}")
            print(f"Valor de depósito: {valor:.2f}")
        else:
            print("Valor de depósito invalido!!!")
        
    def sacar(self, valor: float):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            self.historico.append(f"Valor do saque: {valor:.2f}")
            print(f"Valor do saque: {valor:.2f}")
        else:
            print("Saldo Insuficiente!!!")

    def transferir(self, valor: float, conta_destino):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.historico.append(f"Transferencia de {valor:.2f} para {conta_destino.titular}")
            conta_destino.historico.append(f"Transferencia de {valor:.2f} recebida de {self.titular}")
            print(f"Transferencia de {valor:.2f} para {conta_destino.titular} realizada com sucesso.")
        else:
            print("Saldo Insuficiente!!!")

    def exibir_historico(self):
        if not self.historico:
            print("Nenhuma transação realizada")
        else:
            for transacao in self.historico:
                print(transacao)

    def exibir_saldo(self):
        limite_disponivel = self.saldo + self.limite
        print(f"Saldo Atual: {self.saldo:.2f}, Limite Disponivel: {self.limite:.2f}, Total Disponivel: {limite_disponivel:.2f} ")