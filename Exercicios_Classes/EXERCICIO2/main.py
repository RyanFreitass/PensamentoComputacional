from models.conta import ContaBancaria
conta1 = ContaBancaria("Ryan", 1300.0, 3000.0, [])
conta2 = ContaBancaria("Murilo", 500.0, 2000.0, [])

#TESTE DEPOSITO
conta1.deposito(200.0)
print(conta1.historico)

#TESTE SAQUE
conta1.sacar(500.0)
print(conta1.historico)

#TESTE TRANSFERENCIA
conta1.transferir(100.0, conta2)

print(f"Saldo {conta1.titular}: {conta1.saldo:.2f}")
print(f"Saldo {conta2.titular}: {conta2.saldo:.2f}")
print(f"Histórico {conta1.titular}:", conta1.historico)
print(f"Histórico {conta2.titular}:", conta2.historico)


#EXIBIR HISTORICO
conta1.exibir_historico()

#EXIBIR SALDO
conta1.exibir_saldo()