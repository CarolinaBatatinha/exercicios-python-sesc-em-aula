import tkinter as tk

def btn_click(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(num))

def btn_clear():
    entry.delete(0, tk.END)

def btn_equal():
    equation = entry.get()
    try:
        result = eval(equation)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")

# Configuração da janela principal
window = tk.Tk()
window.title("Calculadora")

# Entrada de texto
entry = tk.Entry(window, width=20, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4)

# Botões de números
btn_1 = tk.Button(window, text="1", padx=15, pady=10, command=lambda: btn_click(1))
btn_2 = tk.Button(window, text="2", padx=15, pady=10, command=lambda: btn_click(2))
btn_3 = tk.Button(window, text="3", padx=15, pady=10, command=lambda: btn_click(3))
btn_4 = tk.Button(window, text="4", padx=15, pady=10, command=lambda: btn_click(4))
btn_5 = tk.Button(window, text="5", padx=15, pady=10, command=lambda: btn_click(5))
btn_6 = tk.Button(window, text="6", padx=15, pady=10, command=lambda: btn_click(6))
btn_7 = tk.Button(window, text="7", padx=15, pady=10, command=lambda: btn_click(7))
btn_8 = tk.Button(window, text="8", padx=15, pady=10, command=lambda: btn_click(8))
btn_9 = tk.Button(window, text="9", padx=15, pady=10, command=lambda: btn_click(9))
btn_0 = tk.Button(window, text="0", padx=15, pady=10, command=lambda: btn_click(0))

btn_1.grid(row=1, column=0)
btn_2.grid(row=1, column=1)
btn_3.grid(row=1, column=2)
btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_7.grid(row=3, column=0)
btn_8.grid(row=3, column=1)
btn_9.grid(row=3, column=2)
btn_0.grid(row=4, column=0)

# Botões de operações
btn_plus = tk.Button(window, text="+", padx=15, pady=10, command=lambda: btn_click("+"))
btn_minus = tk.Button(window, text="-", padx=15, pady=10, command=lambda: btn_click("-"))
btn_multiply = tk.Button(window, text="*", padx=15, pady=10, command=lambda: btn_click("*"))
btn_divide = tk.Button(window, text="/", padx=15, pady=10, command=lambda: btn_click("/"))

btn_plus.grid(row=1, column=3)
btn_minus.grid(row=2, column=3)
btn_multiply.grid(row=3, column=3)
btn_divide.grid(row=4, column=3)

# Botões de igualdade e limpar
btn_equal = tk.Button(window, text="=", padx=15, pady=10, command=btn_equal)
btn_clear = tk.Button(window, text="Limpar", padx=7, pady=10, command=btn_clear)

btn_equal.grid(row=4, column=1)
btn_clear.grid(row=4, column=2)

window.mainloop()
