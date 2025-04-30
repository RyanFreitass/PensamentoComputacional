#1: Solicitar nomes de filmes
    #(Uso de while)
#2: Armazenar os dados
    #Array com capacidade de até 1000 filmes
#3: Registrar avaliações
    # 0.0 ATÉ 10.0 // serão armazenadas em um array paralelo
#4: Exibir resultados:
    #Listar todos os filmes cadastrado
    #Calcular e exibir a nota média de todos os filmes

filmes = []
notas = []
comentarios = []
indicacoes = []
indicacao_num = 0
maximo = 1000
nota_perfeito = 0   #CASO O FILME RECEBA NOTA 10
nota_mtbom = 0      #CASO O FILME RECEBA NOTA DE 8 A 9.9
nota_bom = 0        #CASO O FILME RECEBA NOTA DE 6 A 7.9
nota_fraco = 0      #CASO O FILME RECEBA NOTA DE 4 A 5.9
nota_ruim = 0       #CASO O FILME RECEBA NOTA DE 0 A 3.9

print("--"*13)
print("CADASTRO DE FILMES e NOTAS")
print("--"*13)

# Cadastro de filmes e notas
while len(filmes) < maximo:
    filme = input("Digite o nome do filme ou STOP para parar o cadastro: ")
    if filme.upper() == 'STOP':
        break

    if filme in filmes:
      print("Filme já cadastrado, digite novamente!!!")

    else:
      nota = float(input(f"Digite a nota do filme '{filme}': "))
      if 0.0 <= nota <= 10.0:
          filmes.append(filme)
          notas.append(nota)

          if nota == 10:
            nota_perfeito += 1

          elif nota >= 8 and nota <= 9.9:
            nota_mtbom += 1

          elif nota >= 6 and nota <= 7.9:
            nota_bom += 1

          elif nota >= 4 and nota <= 5.9:
            nota_fraco += 1

          else:
            nota_ruim += 1

      else:
          print("Nota inválida. Digite uma nota entre 0.0 e 10.0.")

    comentario = input(f"Digite um comentario para o filme '{filme}': ")
    comentarios.append(comentario)

    indicacao = input(f"Você recomenda esse filme para seus amigos ou familiares? [SIM] ou [NAO]: ")
    if indicacao == 'SIM':
      indicacao_num += 1
      indicacoes.append(filme)


if len(filmes) == maximo:
    print("\nLimite de 1000 filmes atingido.")

# Exibição dos filmes e suas notas
print("\n--- Filmes cadastrados ---")
for i in range(len(filmes)):
    print(f"O filme '{filmes[i]}' recebeu nota {notas[i]:.1f} da crítica.")

# Exibir a quantidade de filmes em cada escala
print("\n--- Categorias de Filmes em relação as notas ---")
print(f"Nota 10 [PERFEITO]: {nota_perfeito}")
print(f"Nota 8 a 9.9 [MUITO BOM]: {nota_mtbom}")
print(f"Nota 6 a 7.9 [BOM]: {nota_bom}")
print(f"Nota 4 a 5.9 [FRACO]: {nota_fraco}")
print(f"Nota 0 a 3.9 [RUIM]: {nota_ruim}")

# Comentários
print("\n--- Comentários dos Filmes: ---")
for i in range(len(comentarios)):
    print(f"Um comentário do filme '{filmes[i]}': '{comentarios[i]}'")

# Indicações
print("\n--- Indicações para Filmes: ---")
print(f"Filmes indicados: {indicacao_num}")
for i in range(len(indicacoes)):
    print(f"Os filmes indicados foram: {indicacoes[i]}")



# Cálculo da média das notas
if notas:
    media = sum(notas) / len(notas)
    print(f"\nNota média de todos os filmes: {media:.2f}")
else:
    print("\nNenhum filme foi avaliado.")