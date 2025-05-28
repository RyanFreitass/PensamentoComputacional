import tkinter as tk

def mostrar_tela(frame):
    frame.tkraise()

janela = tk.Tk()
janela.title("Exemplo de Múltiplas Telas")
janela.geometry("300x200")

# Configura o grid para os frames ocuparem o mesmo espaço
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

# Tela 1
tela1 = tk.Frame(janela)
tela1.grid(row=0, column=0, sticky="nsew")
tk.Label(tela1, text="Tela 1").pack(pady=20)
tk.Button(tela1, text="Ir para Tela 2", command=lambda: mostrar_tela(tela2)).pack()

# Tela 2
tela2 = tk.Frame(janela)
tela2.grid(row=0, column=0, sticky="nsew")
tk.Label(tela2, text="Tela 2").pack(pady=20)
tk.Button(tela2, text="Voltar para Tela 1", command=lambda: mostrar_tela(tela1)).pack()

# Começa mostrando a tela 1
mostrar_tela(tela1)

janela.mainloop()