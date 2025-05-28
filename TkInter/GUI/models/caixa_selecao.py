import tkinter as tk   

def mostrar_estado():
    if var.get():
        rotulo.config(text="Selecionado!")
    else:
        rotulo.config(text="Não selecionado.")


janela = tk.Tk()
janela.title("Exemplo Checkbutton")
janela.geometry("250x120")

var = tk.BooleanVar()
check = tk.Checkbutton(janela, text="Opção", variable=var, command=mostrar_estado)
check.pack(pady=10)

rotulo = tk.Label(janela, text="Não selecionado.")
rotulo.pack(pady=5)
janela.mainloop()

