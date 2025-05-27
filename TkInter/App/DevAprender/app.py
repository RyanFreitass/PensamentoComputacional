import customtkinter as ctk

#Aparencia
ctk.set_appearance_mode('dark')

#funções de funcionalidades
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == 'ryan' and senha == '1234':
        resultado_login.configure(text='Login feito com sucesso', text_color = 'green')
    
    else:
        resultado_login.configure(text='Login Incorreto', text_color='red')
        

#Janela Principal
app = ctk.CTk()
app.title("Sistema de Login")
app.geometry("300x300")

#Criação de Campos
#Label1
label_usuario = ctk.CTkLabel(app, text='Usuário:')
label_usuario.pack(pady=10)
#Entry1
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)

#Label2
label_senha = ctk.CTkLabel(app, text='Senha:')
label_senha.pack(pady=10)
#Entry2
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show="*")
campo_senha.pack(pady=10)

#Button
botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=10)

#campo feedback button
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)



#Aplicação
app.mainloop()