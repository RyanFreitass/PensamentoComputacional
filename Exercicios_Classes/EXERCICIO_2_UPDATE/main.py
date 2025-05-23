from models.conta import conta_banco

banco = []

banco.append(conta_banco("Ryan", 1000, 500, ["51999149465", "04044331030", "ryanfreitas@ienh.com"], []))
banco.append(conta_banco("Lucas", 2000, 1000, ["384738438", "433343434", "lucas@ienh.com"], []))

print("##"*10)
print("--- Banco IENH ---")
print("##"*10)
while True:
    print("--"*12)
    resposta = input("Criar conta? [1]\nExibir Saldo? [2]\nSacar? [3]\nDepositar? [4]\nRealizar transferência? [5]\nRealizar um pix? [6]\nExibir Histórico de Transações? [7]\nCriar chave PIX? [8]\nExcluir conta? [9]\nSair? [10]: ")
    print("--"*12)

    if resposta == '1':
        for i in range(1):
            nome = input("Digite o nome do Titular: ")
            saldo = float(input("Digite o saldo da conta: "))
            limite = float(input("Digite o limite da conta: "))
            chave_pix1 = input("Digite a chave pix I: ")
            chave_pix2 = input("Digite a chave pix II: ")
            chave_pix3 = input("Digite a chave pix III: ")
            banco.append(conta_banco(nome, saldo, limite, [chave_pix1, chave_pix2, chave_pix3], []))

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
        titular = input("Digite o titular da conta que deseja realizar uma transferencia: ")
        conta_destino = input("Digite o titular que irá receber a transferencia: ")
        for conta in banco:
            if conta.titular == titular:
                valor = float(input("Digite o valor para transferencia: "))
                for conta2 in banco:
                    if conta2.titular == conta_destino:
                        conta.transferir(conta2, valor)


    elif resposta == '6':
        titular = input("Titular da conta: ")
        chave_pix = input("Chave Pix do destinatário: ")
        valor = float(input("Valor do Pix: "))

        for conta in banco:
            if conta.titular == titular:
                for destino in banco:
                    if chave_pix in destino.chave_pix:
                        if conta.pix(destino, valor):
                            print("Pix realizado com sucesso!")
                        else:
                            print("Erro ao realizar o Pix.")
                        break
                else:
                    print("Destinatário não encontrado.")
                break
        else:
            print("Titular não encontrado.")


    elif resposta == '7':
        titular = input("Digite o titular da conta que deseja ver o histórico: ")
        for conta in banco:
            if conta.titular == titular:
                conta.exibir_historico()

    elif resposta == '8':
        titular = input("Digite o titular da conta que deseja criar uma chave pix: ")
        for conta in banco:
            if conta.titular == titular:
                chave_pix = input("Digite a nova chave pix: ")
                conta.criar_chave_pix(chave_pix)
                print(f"A chave {chave_pix} foi criada com sucesso!")
    
    elif resposta == '9':
        titular = input("Digite o titular da conta que deseja excluir: ")
        resposta2 = input("Deseja realizar uma transferencia para o saldo restante? [1] --- Deseja realizar um deposito para zerar a conta? [2] --- Apenas excluir a conta? [3]: ")
        if resposta2 == '1':
            destinatario = input("Digite o titular que irá receber o seu saldo restante: ")
            for conta in banco:
                if conta.titular == titular:
                    valor = float(input("Digite o valor para transferencia: "))
                    for conta2 in banco:
                        if conta2.titular == destinatario:
                            conta.transferir(conta2, valor)

        elif resposta2 == '2':
            for conta in banco:
                if conta.titular == titular:
                    valor = float(input("Digite o valor para deposito: "))
                    conta.depositar(valor)
        
        elif resposta2 == '3':
            for conta in banco:
                if conta.titular == titular:
                    banco.remove(conta)
                    print(f"A conta de {titular} foi excluída com sucesso!")

    
       
    else:
        print("BANCO ENCERRADO!!!")
        break
