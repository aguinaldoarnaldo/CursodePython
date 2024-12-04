print('Olá, Mundo')
# Importa a biblioteca Tkinter
import tkinter as tk
from tkinter import messagebox


def somar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        messagebox.showinfo("Resultado", f"A soma é: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")


def multiplicar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 * num2
        messagebox.showinfo("Resultado", f"A multiplicação é: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")


# Cria a janela principal
window = tk.Tk()
window.title("Calculadora Simples")

# Cria os widgets da interface
label_num1 = tk.Label(window, text="Número 1:")
label_num1.pack()

entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Número 2:")
label_num2.pack()

entry_num2 = tk.Entry(window)
entry_num2.pack()

botao_somar = tk.Button(window, text="Somar", command=somar)
botao_somar.pack()

botao_multiplicar = tk.Button(window, text="Multiplicar", command=multiplicar)
botao_multiplicar.pack()

# Inicia o loop principal da interface
window.mainloop()
