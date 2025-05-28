import tkinter as tk
import random

'''def mostrar_opcao():
    rotulo.config(text=f"Escolheu: {opcao.get()}")

janela = tk.Tk()
janela.title("Exemplo Radiobutton")
janela.geometry("250x150")

opcao = tk.StringVar(value="A")
tk.Radiobutton(janela, text="Opção A", variable=opcao, value="A", command=mostrar_opcao).pack()
tk.Radiobutton(janela, text="Opção B", variable=opcao, value="B", command=mostrar_opcao).pack()
tk.Radiobutton(janela, text="Opção C", variable=opcao, value="C", command=mostrar_opcao).pack()

rotulo = tk.Label(janela, text="Escolheu: A")
rotulo.pack(pady=10)

janela.mainloop()'''

def mostrar_opcao():
    texto = f"Escolheu: {opcao1.get()}"
    texto += f" {opcao2.get()}"
    texto += f" {opcao3.get()}"
    rotulo.config(text= texto)

    op = [opcao1.get(), opcao2.get(), opcao3.get()]
    if op.count(True) == 3:
        rand = random.randint(0, 2)
        if rand == 0:
            opcao1.set(False)
        if rand == 1:
            opcao2.set(False)
        if rand == 2:
            opcao3.set(False)
        
janela = tk.Tk()
janela.title("Exercicio Botoes Radio")
janela.geometry("600x400")
fonte_padrao = ("Arial", 12)

opcao1 = tk.BooleanVar()
opcao2 = tk.BooleanVar()
opcao3 = tk.BooleanVar()

tk.Radiobutton(janela, text="Dinheiro", variable=opcao1, value=True, command=mostrar_opcao, font=fonte_padrao).pack()
tk.Radiobutton(janela, text="Tempo", variable=opcao2, value=True, command=mostrar_opcao, font=fonte_padrao).pack()
tk.Radiobutton(janela, text="Saúde", variable=opcao3, value=True, command=mostrar_opcao, font=fonte_padrao).pack()

rotulo = tk.Label(janela, text="Escolheu:", font=fonte_padrao)
rotulo.pack(pady=10)

janela.mainloop()
