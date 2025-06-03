import sqlite3
import os

def conectar_banco():
    """
    Conecta ao banco de dados SQLite e cria a tabela se não existir
    Retorna: tupla (conexao, cursor)
    """
    # Estabelece conexão com o banco (cria o arquivo se não existir)
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    
    # Criar tabela usuarios se ela não existir
    # IF NOT EXISTS evita erro se a tabela já existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            email TEXT
        )
    ''')
    
    # Salva as mudanças no banco
    conn.commit()
    return conn, cursor

def adicionar_usuario():
    """
    Função para adicionar um novo usuário ao banco de dados
    Solicita dados do usuário e valida antes de inserir
    """
    print("\n" + "="*40)
    print("ADICIONAR NOVO USUARIO")
    print("="*40)
    
    # Solicita e valida o nome do usuário
    nome = input("Nome: ").strip()
    if not nome:
        print("Erro: Nome nao pode estar vazio!")
        return
    
    # Solicita e valida a idade
    try:
        idade = int(input("Idade: "))
        # Verifica se a idade está em um range válido
        if idade < 0 or idade > 120:
            print("Erro: Idade deve estar entre 0 e 120 anos!")
            return
    except ValueError:
        print("Erro: Idade deve ser um numero valido!")
        return
    
    # Solicita email (opcional)
    email = input("Email (opcional): ").strip()
    # Se email vazio, define como None para o banco
    if not email:
        email = None
    
    # Tenta inserir os dados no banco
    try:
        # Conecta ao banco
        conn, cursor = conectar_banco()
        
        # Executa o comando INSERT com placeholders (?) para segurança
        cursor.execute(
            "INSERT INTO usuarios (nome, idade, email) VALUES (?, ?, ?)",
            (nome, idade, email)
        )
        
        # Salva as mudanças
        conn.commit()
        print(f"Sucesso: Usuario '{nome}' adicionado com sucesso!")
        
    except sqlite3.Error as e:
        # Captura erros específicos do SQLite
        print(f"Erro ao adicionar usuario: {e}")
    finally:
        # Sempre fecha a conexão, mesmo em caso de erro
        conn.close()

def listar_usuarios():
    """
    Lista todos os usuários cadastrados no banco de dados
    Exibe em formato tabular organizado
    """
    try:
        # Conecta ao banco
        conn, cursor = conectar_banco()
        
        # Busca todos os usuários ordenados por nome
        cursor.execute("SELECT id, nome, idade, email FROM usuarios ORDER BY nome")
        usuarios = cursor.fetchall()
        
        # Verifica se há usuários cadastrados
        if not usuarios:
            print("\nNenhum usuario cadastrado ainda!")
            return
        
        # Exibe cabeçalho da tabela
        print("\n" + "="*60)
        print("USUARIOS CADASTRADOS")
        print("="*60)
        print(f"{'ID':<4} {'Nome':<20} {'Idade':<6} {'Email':<25}")
        print("-"*60)
        
        # Percorre e exibe cada usuário
        for usuario in usuarios:
            id_user, nome, idade, email = usuario
            # Se email for None, exibe "Nao informado"
            email_display = email if email else "Nao informado"
            print(f"{id_user:<4} {nome:<20} {idade:<6} {email_display:<25}")
        
        # Exibe total de usuários
        print(f"\nTotal de usuarios: {len(usuarios)}")
        
    except sqlite3.Error as e:
        print(f"Erro ao listar usuarios: {e}")
    finally:
        conn.close()

def buscar_usuario():
    """
    Busca usuários por nome (busca parcial)
    Permite encontrar usuários digitando parte do nome
    """
    print("\n" + "="*40)
    print("BUSCAR USUARIO")
    print("="*40)
    
    # Solicita o termo de busca
    nome_busca = input("Digite o nome para buscar: ").strip()
    if not nome_busca:
        print("Erro: Nome nao pode estar vazio!")
        return
    
    try:
        # Conecta ao banco
        conn, cursor = conectar_banco()
        
        # Busca usando LIKE para busca parcial (% = qualquer caractere)
        cursor.execute(
            "SELECT id, nome, idade, email FROM usuarios WHERE nome LIKE ? ORDER BY nome",
            (f"%{nome_busca}%",)
        )
        usuarios = cursor.fetchall()
        
        # Verifica se encontrou usuários
        if not usuarios:
            print(f"Nenhum usuario encontrado com o nome '{nome_busca}'")
            return
        
        # Exibe resultados da busca
        print(f"\nUsuarios encontrados com '{nome_busca}':")
        print("-"*50)
        print(f"{'ID':<4} {'Nome':<20} {'Idade':<6} {'Email':<20}")
        print("-"*50)
        
        for usuario in usuarios:
            id_user, nome, idade, email = usuario
            email_display = email if email else "Nao informado"
            print(f"{id_user:<4} {nome:<20} {idade:<6} {email_display:<20}")
        
    except sqlite3.Error as e:
        print(f"Erro ao buscar usuario: {e}")
    finally:
        conn.close()

def deletar_usuario():
    """
    Deleta um usuário do banco de dados
    Solicita confirmação antes de excluir
    """
    # Primeiro mostra todos os usuários
    listar_usuarios()
    
    # Verifica se existem usuários para deletar
    if not verificar_usuarios_existem():
        return
    
    print("\n" + "="*40)
    print("DELETAR USUARIO")
    print("="*40)
    
    # Solicita o ID do usuário a ser deletado
    try:
        id_usuario = int(input("Digite o ID do usuario para deletar: "))
    except ValueError:
        print("Erro: ID deve ser um numero valido!")
        return
    
    try:
        # Conecta ao banco
        conn, cursor = conectar_banco()
        
        # Verifica se o usuário existe antes de tentar deletar
        cursor.execute("SELECT nome FROM usuarios WHERE id = ?", (id_usuario,))
        usuario = cursor.fetchone()
        
        if not usuario:
            print(f"Erro: Usuario com ID {id_usuario} nao encontrado!")
            return
        
        # Obtém o nome para confirmação
        nome_usuario = usuario[0]
        
        # Solicita confirmação da exclusão
        confirma = input(f"Tem certeza que deseja deletar '{nome_usuario}'? (s/N): ").lower()
        
        if confirma == 's':
            # Executa a exclusão
            cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
            conn.commit()
            print(f"Sucesso: Usuario '{nome_usuario}' deletado com sucesso!")
        else:
            print("Operacao cancelada!")
        
    except sqlite3.Error as e:
        print(f"Erro ao deletar usuario: {e}")
    finally:
        conn.close()

def atualizar_usuario():
    """
    Atualiza os dados de um usuário existente
    Permite manter dados atuais pressionando Enter
    """
    # Mostra usuários existentes
    listar_usuarios()
    
    # Verifica se há usuários para atualizar
    if not verificar_usuarios_existem():
        return
    
    print("\n" + "="*40)
    print("ATUALIZAR USUARIO")
    print("="*40)
    
    # Solicita ID do usuário
    try:
        id_usuario = int(input("Digite o ID do usuario para atualizar: "))
    except ValueError:
        print("Erro: ID deve ser um numero valido!")
        return
    
    try:
        # Conecta ao banco
        conn, cursor = conectar_banco()
        
        # Busca os dados atuais do usuário
        cursor.execute("SELECT nome, idade, email FROM usuarios WHERE id = ?", (id_usuario,))
        usuario = cursor.fetchone()
        
        if not usuario:
            print(f"Erro: Usuario com ID {id_usuario} nao encontrado!")
            return
        
        # Extrai dados atuais
        nome_atual, idade_atual, email_atual = usuario
        
        # Exibe dados atuais
        print(f"\nDados atuais:")
        print(f"Nome: {nome_atual}")
        print(f"Idade: {idade_atual}")
        print(f"Email: {email_atual if email_atual else 'Nao informado'}")
        
        print("\nDigite os novos dados (pressione Enter para manter o atual):")
        
        # Solicita novo nome
        novo_nome = input(f"Novo nome [{nome_atual}]: ").strip()
        if not novo_nome:
            novo_nome = nome_atual
        
        # Solicita nova idade
        nova_idade_input = input(f"Nova idade [{idade_atual}]: ").strip()
        if nova_idade_input:
            try:
                nova_idade = int(nova_idade_input)
                # Valida a nova idade
                if nova_idade < 0 or nova_idade > 120:
                    print("Erro: Idade deve estar entre 0 e 120 anos! Mantendo valor atual.")
                    nova_idade = idade_atual
            except ValueError:
                print("Erro: Idade invalida! Mantendo valor atual.")
                nova_idade = idade_atual
        else:
            # Mantém idade atual se campo vazio
            nova_idade = idade_atual
        
        # Solicita novo email
        novo_email = input(f"Novo email [{email_atual if email_atual else 'Nao informado'}]: ").strip()
        if not novo_email:
            novo_email = email_atual
        
        # Executa a atualização no banco
        cursor.execute(
            "UPDATE usuarios SET nome = ?, idade = ?, email = ? WHERE id = ?",
            (novo_nome, nova_idade, novo_email, id_usuario)
        )
        
        conn.commit()
        print(f"Sucesso: Usuario atualizado com sucesso!")
        
    except sqlite3.Error as e:
        print(f"Erro ao atualizar usuario: {e}")
    finally:
        conn.close()

def verificar_usuarios_existem():
    """
    Verifica se existem usuários cadastrados no banco
    Retorna: True se existem usuários, False caso contrário
    """
    try:
        # Conecta ao banco
        conn, cursor = conectar_banco()
        # Conta o número de usuários
        cursor.execute("SELECT COUNT(*) FROM usuarios")
        count = cursor.fetchone()[0]
        conn.close()
        # Retorna True se há pelo menos 1 usuário
        return count > 0
    except:
        # Em caso de erro, assume que não há usuários
        return False

def estatisticas():
    """
    Mostra estatísticas dos usuários cadastrados
    Inclui total, idades e informações sobre emails
    """
    try:
        # Conecta ao banco
        conn, cursor = conectar_banco()
        
        # Conta total de usuários
        cursor.execute("SELECT COUNT(*) FROM usuarios")
        total = cursor.fetchone()[0]
        
        # Se não há usuários, exibe mensagem e sai
        if total == 0:
            print("\nNenhum usuario cadastrado para mostrar estatisticas!")
            return
        
        # Calcula idade média
        cursor.execute("SELECT AVG(idade) FROM usuarios")
        idade_media = cursor.fetchone()[0]
        
        # Encontra idades mínima e máxima
        cursor.execute("SELECT MIN(idade), MAX(idade) FROM usuarios")
        idade_min, idade_max = cursor.fetchone()
        
        # Conta usuários com email cadastrado
        cursor.execute("SELECT COUNT(*) FROM usuarios WHERE email IS NOT NULL AND email != ''")
        com_email = cursor.fetchone()[0]
        
        # Exibe todas as estatísticas
        print("\n" + "="*40)
        print("ESTATISTICAS DOS USUARIOS")
        print("="*40)
        print(f"Total de usuarios: {total}")
        print(f"Com email cadastrado: {com_email}")
        print(f"Sem email: {total - com_email}")
        print(f"Idade media: {idade_media:.1f} anos")
        print(f"Mais novo: {idade_min} anos")
        print(f"Mais velho: {idade_max} anos")
        
    except sqlite3.Error as e:
        print(f"Erro ao gerar estatisticas: {e}")
    finally:
        conn.close()

def limpar_tela():
    """
    Limpa a tela do terminal
    Funciona em Windows (cls) e Linux/Mac (clear)
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    """
    Função principal que exibe o menu e gerencia as opções
    Controla o fluxo principal do programa
    """
    
    # Inicializa o banco de dados na primeira execução
    try:
        conn, cursor = conectar_banco()
        conn.close()
        print("Banco de dados inicializado com sucesso!")
    except Exception as e:
        print(f"Erro ao inicializar banco: {e}")
        return
    
    # Loop principal do menu
    while True:
        # Exibe o menu
        print("\n" + "="*50)
        print("SISTEMA DE GERENCIAMENTO DE USUARIOS")
        print("="*50)
        print("1. Adicionar usuario")
        print("2. Listar todos os usuarios")
        print("3. Buscar usuario")
        print("4. Atualizar usuario")
        print("5. Deletar usuario")
        print("6. Ver estatisticas")
        print("7. Limpar tela")
        print("0. Sair")
        print("-"*50)
        
        # Solicita opção do usuário
        opcao = input("Escolha uma opcao: ").strip()
        
        # Trata cada opção do menu
        try:
            if opcao == "1":
                adicionar_usuario()
            
            elif opcao == "2":
                listar_usuarios()
            
            elif opcao == "3":
                buscar_usuario()
            
            elif opcao == "4":
                atualizar_usuario()
            
            elif opcao == "5":
                deletar_usuario()
            
            elif opcao == "6":
                estatisticas()
            
            elif opcao == "7":
                limpar_tela()
            
            elif opcao == "0":
                print("\nObrigado por usar o sistema! Ate logo!")
                break
            
            else:
                print("Opcao invalida! Tente novamente.")
        
        except KeyboardInterrupt:
            # Captura Ctrl+C para sair graciosamente
            print("\n\nSaindo do programa...")
            break
        except Exception as e:
            # Captura outros erros inesperados
            print(f"Erro inesperado: {e}")
            print("Tente novamente ou reinicie o programa.")

# Executa o programa apenas se este arquivo for executado diretamente
# (não se for importado como módulo)
if __name__ == "__main__":
    menu_principal()