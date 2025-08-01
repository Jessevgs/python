import tkinter as tk
from tkinter import scrolledtext

# Função que simula uma resposta da IA
def get_ai_response(user_input):
    # Para simplicidade, apenas retornamos uma resposta padrão
    return f"Você disse: {user_input}. Isso é interessante!"

# Função que lida com o envio de mensagens
def send_message():
    user_input = entry.get()
    if user_input:
        chat_area.insert(tk.END, "Você: " + user_input + "\n")
        entry.delete(0, tk.END)  # Limpa a entrada
        ai_response = get_ai_response(user_input)
        chat_area.insert(tk.END, "Chat AI: " + ai_response + "\n")

# Configuração da janela principal
root = tk.Tk()
root.title("Chat AI")

# Área de texto para o chat
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Campo de entrada de mensagem
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=10, side=tk.LEFT)

# Botão de envio
send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.pack(padx=10, pady=10, side=tk.RIGHT)

# Executa o loop principal
root.mainloop() 
