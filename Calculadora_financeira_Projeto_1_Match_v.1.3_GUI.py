import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def validar_renda(renda):
    limite_minimo = 1000
    return renda >= limite_minimo

def calcular_prestacoes(valor_emprestimo, taxa_juros, prazo):
    try:
        taxa_juros_decimal = taxa_juros / 100
        prestacao = (valor_emprestimo * (taxa_juros_decimal / 12)) / (1 - (1 + (taxa_juros_decimal / 12)) ** (-prazo))
        return prestacao
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Divisão por zero")

def calculate_loan():
    renda = float(renda_entry.get())
    if validar_renda(renda):
        valor_emprestimo = float(valor_emprestimo_entry.get())
        if valor_emprestimo > renda * 10:
            messagebox.showerror("Erro", "O valor do empréstimo excede 10x a renda!")
        else:
            prazo = int(prazo_entry.get())
            if prazo < 0:
                messagebox.showerror("Erro", "O prazo informado é menor do que zero")
            else:
                taxa_juros = float(taxa_juros_entry.get())
                taxa_juros_mensal = ((1 + taxa_juros / 100) ** (1 / 12) - 1) * 100
                prestacao = calcular_prestacoes(valor_emprestimo, taxa_juros, prazo)
                custo_total = prestacao * prazo

                renda_label.config(text=f'Renda mensal informada: R$ {renda:.4f}')
                valor_emprestimo_label.config(text=f'Valor tomado como empréstimo: R$ {valor_emprestimo:.4f}')
                taxa_juros_label.config(text=f"Taxa de Juros anual: {taxa_juros}% ao ano")
                taxa_juros_mensal_label.config(text=f"Taxa de Juros mensal: {taxa_juros_mensal:.4f}% ao mês")
                prazo_label.config(text=f"Prazo em meses: {prazo} meses")
                prestacao_label.config(text=f"Valor das Prestações Mensais: R$ {prestacao:.4f}")
                custo_total_label.config(text=f"Custo Total do Empréstimo: R$ {custo_total:.4f}")
    else:
        messagebox.showerror("Erro", "Desculpe, sua renda não atende aos requisitos mínimos para o empréstimo.")

# Create the main window
window = tk.Tk()
window.title("Calculadora de Empréstimo")

# Create and configure the input fields
renda_label = ttk.Label(window, text="Renda Mensal:")
renda_label.pack()
renda_entry = ttk.Entry(window)
renda_entry.pack()

valor_emprestimo_label = ttk.Label(window, text="Valor do Empréstimo:")
valor_emprestimo_label.pack()
valor_emprestimo_entry = ttk.Entry(window)
valor_emprestimo_entry.pack()

prazo_label = ttk.Label(window, text="Prazo (em meses):")
prazo_label.pack()
prazo_entry = ttk.Entry(window)
prazo_entry.pack()

taxa_juros_label = ttk.Label(window, text="Taxa de Juros Anual (%):")
taxa_juros_label.pack()
taxa_juros_entry = ttk.Entry(window)
taxa_juros_entry.pack()

calculate_button = ttk.Button(window, text="Calcular", command=calculate_loan)
calculate_button.pack()

# Create and configure labels for the results
renda_label = ttk.Label(window, text="")
renda_label.pack()

valor_emprestimo_label = ttk.Label(window, text="")
valor_emprestimo_label.pack()

taxa_juros_label = ttk.Label(window, text="")
taxa_juros_label.pack()

taxa_juros_mensal_label = ttk.Label(window, text="")
taxa_juros_mensal_label.pack()

prazo_label = ttk.Label(window, text="")
prazo_label.pack()

prestacao_label = ttk.Label(window, text="")
prestacao_label.pack()

custo_total_label = ttk.Label(window, text="")
custo_total_label.pack()

window.mainloop()
