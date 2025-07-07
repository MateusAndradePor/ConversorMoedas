import tkinter as tk
from tkinter import messagebox
import requests

# Site para obter a API: app.freecurrencyapi.com
# Autorização da API:
API_KEY = 'fca_live_ePFvqJfxkqaQaABh1wZUr23d489Yyl4eQeK2FDfh'

# Obtendo a taxa de conversão pela API:
def taxa_conversao(base, path):
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}&currencies={path.upper()}&base_currency={base.upper()}"
    # print(f"Consultando URL: {url}") # Debug
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        # print("Resposta da API:", dados) # Debug
        return dados["data"].get(path.upper())
    except Exception as e:
        print("Erro ao obter taxa:", e)
        return None

def converter():
    base = entrada_base.get().strip().upper()
    path = entrada_path.get().strip().upper()
    valor_str = entrada_valor.get().strip()

    if not base or not path or not valor_str:
        messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
        return

    try:
        valor = float(valor_str)
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido.")
        return

    taxa = taxa_conversao(base, path)
    if taxa:
        convertido = valor * taxa
        resultado_var.set(f"{valor:.2f} {base} = {convertido:.2f} {path}")
    else:
        messagebox.showerror("Erro", "Não foi possível obter a taxa de conversão.")


# Criando a interface:
if __name__ == "__main__":
    janela = tk.Tk()
    janela.title("Conversor de Moedas")
    janela.geometry("300x250")
    janela.resizable(False, False)

    tk.Label(janela, text="Moeda de origem (ex: BRL):").pack(pady=5)
    entrada_base = tk.Entry(janela)
    entrada_base.pack()

    tk.Label(janela, text="Moeda de destino (ex: USD):").pack(pady=5)
    entrada_path = tk.Entry(janela)
    entrada_path.pack()

    tk.Label(janela, text="Valor a converter:").pack(pady=5)
    entrada_valor = tk.Entry(janela)
    entrada_valor.pack()

    tk.Button(janela, text="Converter", command=converter).pack(pady=10)

    resultado_var = tk.StringVar()
    tk.Label(janela, textvariable=resultado_var, font=("Arial", 12, "bold")).pack(pady=10)

    janela.mainloop()
