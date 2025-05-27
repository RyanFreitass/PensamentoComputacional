import tkinter as tk

def clique():
    if rotulo["text"] == "Olá, Mundo!!!":
        rotulo.config(text="Olá, Turma!!!")
    else:
        rotulo.config(text="Olá, Mundo!!!")
    

janela = tk.Tk()
janela.title("Exemplo Botao")
janela.geometry("600x400")

rotulo = tk.Label(janela, text="Clique no botao", font=("Arial", 16))
rotulo.pack(pady=10)

botao = tk.Button(janela, text="Clique Aqui", command=clique, font=("Arial", 16))

botao.pack(pady=10)
janela.mainloop()
