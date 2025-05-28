import tkinter as tk
def calcular():
    try:
        resultado = eval(entrada.get())
        rotulo_resultado.config(text=f"Resultado: {resultado}")
    except Exception:
        rotulo_resultado.config(text="Erro!")

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x150")

entrada = tk.Entry(janela, width=20)
entrada.pack(pady=10)

botao = tk.Button(janela, text="Calcular", command=calcular)
botao.pack(pady=5)

rotulo_resultado = tk.Label(janela, text="Resultado:")
rotulo_resultado.pack(pady=5)

janela.mainloop()