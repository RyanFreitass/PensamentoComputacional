from models.conta import conta_banco

banco = []

while True:
    resposta = input("Criar uma nova conta? [1] --- Exibir Saldo? [2] --- Sacar? [3] --- Depositar? [4] --- Realizar transferência? [5] --- ENCERRAR O PROGRAMA? [6]: ")
    if resposta == '1':
        for i in range(1):
            nome = input("Digite o nome do Titular: ")
            saldo = float(input("Digite o saldo da conta: "))
            limite = float(input("Digite o limite da conta: "))
            banco.append(conta_banco(nome, saldo, limite, []))

    elif resposta == '2':
        titular = input("Digite o titular da conta que deseja ver o saldo: ")
        for conta in banco:
            if conta.titular == titular:
                print(f"O {titular} tem R${conta.saldo} em conta!")

    elif resposta == '3':
        titular = input("Digite o titular da conta que deseja realizar um saque: ")
        for conta in banco:
            if conta.titular == titular:
                saque = float(input("Digite o valor para saque: "))
                conta.sacar(saque)
    
    elif resposta == '4':
        titular = input("Digite o titular da conta que deseja realizar um deposito: ")
        for conta in banco:
            if conta.titular == titular:
                deposito = float(input("Digite o valor para deposito: "))
                conta.depositar(deposito)
    
    elif resposta == '5':
        titular = input("Digite o titular da conta que deseja realizar um deposito: ")
        for conta in banco:
            if conta.titular == titular:
                deposito = float(input("Digite o valor para deposito: "))
                conta.depositar(deposito)

    else:
        print("PROGRAMA ENCERRADO!!!")
        break    
     