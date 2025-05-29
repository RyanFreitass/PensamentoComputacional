import re

'''#em uma string
resultado = re.search(padrão, texto)

#texto inteiro
resultado = re.match(padrão, texto)

#todas as ocorrencias
resultado = re.findall(padrão, texto)

#substituir ocorrencias 
novo_texto = re.sub(padrão, substituição, texto)'''


#validar email
def validar_email(email):
    padrao = r'^[a-z]+\.[a-z]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{1,2}$'
    return bool(re.match(padrao, email))

emails = ['usuario@exemplo.com', 'nome.sobrenome@empresa.com.br',
          'invalido', 'sem_arroba.com', '@dominio.com', 'ryan.+_-p@ienh.com.br']

for email in emails:
    print(f"{email}: {'Válido' if validar_email(email) else 'Inválido'}")


#validar cpf
def validar_cpf(cpf):
    #remove caracteres ñ numericos
    cpf = re.sub(r'[^0-9]', '', cpf)

    #verifica se tem 11 digitos
    if len(cpf) != 11:
        return False
    
    #verificar se n sao todos digitos iguais
    if cpf == cpf[0] * 11:
        return False
    
    #formato para exibição: 123.456.789-00
    padrao_formatado = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'


    return True

#teste
cpf_formatado = '123.456.789-09'
print(f"CPF {cpf_formatado}: {'Válido' if re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf_formatado) else 'Formato Inválido'}")