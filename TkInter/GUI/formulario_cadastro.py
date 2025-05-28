import tkinter as tk
from tkinter import messagebox

def cadastrar():
    nome = entrada_nome.get()
    email = entrada_email.get()
    if nome and email:
        messagebox.showinfo("Cadastro", f"Nome: {nome}\nEmail: {email}")
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")

janela = tk.Tk()
janela.title("Cadastro")
janela.geometry("300x200")

tk.Label(janela, text="Nome:").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Email:").pack()
entrada_email = tk.Entry(janela)
entrada_email.pack()

tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=10)

janela.mainloop()
