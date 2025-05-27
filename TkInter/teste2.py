from tkinter import *

#janela tkinter
janela = Tk()    
janela.title("Login Banco")

#fonte padrao
fonte_padrao = ("Arial", 12)

#primeiro container
primeiro_container = Frame(janela)
primeiro_container["pady"] = 20
primeiro_container.pack()

titulo = Label(primeiro_container, text="Banco", font=("Arial", 20, "bold"))
titulo.pack()

#descricao container 1,5
descricao_container = Frame(janela)
descricao_container["pady"] = 20
descricao_container.pack()

descricao = Label(descricao_container, text="Entre com os seus dados corretamente para acessar o sistema.")
descricao.pack()


#segundo container
segundo_container = Frame(janela)
segundo_container["padx"] = 20
segundo_container.pack()

nomeLabel = Label(segundo_container, text="Nome:", font=fonte_padrao)
nomeLabel.pack(side=LEFT)

nome = Entry(segundo_container)
nome["width"] = 20
nome["font"] = fonte_padrao
nome.pack(side=LEFT)


#terceiro container
terceiro_container = Frame(janela)
terceiro_container["padx"] = 20
terceiro_container.pack()

senhaLabel = Label(terceiro_container, text="Senha:", font=fonte_padrao)
senhaLabel.pack(side=LEFT)

senha = Entry(terceiro_container)
senha["width"] = 20
senha["show"] = "*"
senha["font"] = fonte_padrao
senha.pack(side=LEFT)


#quarto container
quarto_container = Frame(janela)
quarto_container["padx"] = 20
quarto_container.pack()

cpfLabel = Label(quarto_container, text="CPF:", font=fonte_padrao)
cpfLabel.pack(side=LEFT)

cpf = Entry(quarto_container)
cpf["width"] = 20
cpf["font"] = fonte_padrao
cpf.pack(side=LEFT)

#quinto container
quinto_container = Frame(janela)
quinto_container["pady"] = 20
quinto_container.pack()

def verificar_login():
    usuario = nome.get()
    senhas = senha.get()
    cpfs = cpf.get()

    if usuario == 'Ryan Vitor Freitas' and senhas == '1234' and cpfs == '12345678900':
        mensagem["text"]="Acesso Permitido"
    else:
        mensagem["text"]= "Acesso Negado!!!"


botao_autenticar = Button(quinto_container)
botao_autenticar["text"] = "Autenticar"
botao_autenticar["font"] = ("Calibri", 10)
botao_autenticar["width"] = 12
botao_autenticar["command"] = verificar_login
botao_autenticar.pack()

mensagem = Label(quinto_container, text="", font=fonte_padrao)
mensagem.pack()



    

janela.mainloop()