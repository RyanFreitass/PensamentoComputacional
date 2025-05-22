def div (a, b):
    if b == 0:
        return "Divisão por zero não é permitida"
    return a / b

while True:
    try:
        n1 = float(input("Digite o primeiro número, ou somente 'sair' para sair: "))
        if n1 == 'SAIR':
            break
        n1 = float(n1)
        n2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Por favor insira numeros validos")
        continue
    
    resultado = div(n1, n2)
    print(f"O resultado da divisão é {resultado}")