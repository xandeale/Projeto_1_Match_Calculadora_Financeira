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

                results_text.set(
                    f'Renda mensal informada: R$ {renda:.4f}\n'
                    f'Valor tomado como empréstimo: R$ {valor_emprestimo:.4f}\n'
                    f"Taxa de Juros anual: {taxa_juros}% ao ano\n"
                    f"Taxa de Juros mensal: {taxa_juros_mensal:.4f}% ao mês\n"
                    f"Prazo em meses: {prazo} meses\n"
                    f"Valor das Prestações Mensais: R$ {prestacao:.4f}\n"
                    f"Custo Total do Empréstimo: R$ {custo_total:.4f}"
                )
    else:
        messagebox.showerror("Erro", "Desculpe, sua renda não atende aos requisitos mínimos para o empréstimo.")

# Create the main window
window = tk.Tk()
window.title("Calculadora de Empréstimo")

# Create and configure the input fields
style = ttk.Style()
style.configure("TLabel", foreground="blue", font=("Arial", 12))
style.configure("TButton", foreground="white", background="blue", font=("Arial", 12))

frame = ttk.Frame(window)
frame.pack(padx=20, pady=20)

ttk.Label(frame, text="Renda Mensal:").grid(row=0, column=0, padx=10, pady=5)
renda_entry = ttk.Entry(frame)
renda_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(frame, text="Valor do Empréstimo:").grid(row=1, column=0, padx=10, pady=5)
valor_emprestimo_entry = ttk.Entry(frame)
valor_emprestimo_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(frame, text="Prazo (em meses):").grid(row=2, column=0, padx=10, pady=5)
prazo_entry = ttk.Entry(frame)
prazo_entry.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(frame, text="Taxa de Juros Anual (%):").grid(row=3, column=0, padx=10, pady=5)
taxa_juros_entry = ttk.Entry(frame)
taxa_juros_entry.grid(row=3, column=1, padx=10, pady=5)

calculate_button = ttk.Button(frame, text="Calcular", command=calculate_loan)
calculate_button.grid(row=4, columnspan=2, padx=10, pady=10)

# Create a label for displaying the results
results_text = tk.StringVar()
results_label = ttk.Label(window, textvariable=results_text)
results_label.pack(pady=10)

window.mainloop()
