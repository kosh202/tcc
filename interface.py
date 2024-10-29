import tkinter as tk


# Criar a janela principal
janela = tk.Tk()
janela.title("Interface Simples")
janela.geometry("400x300") 


# Criar um campo de entrada
# entrada = tk.Entry(janela)
# entrada.pack(pady=10)



# Criar um botão
gravar = tk.Button(janela, text="gravar")
gravar.pack(pady=10)

escolherArquivo = tk.Button(janela, text="gravar")
escolherArquivo.pack(pady=10)


# Criar um label para exibir a mensagem
mensagem_label = tk.Label(janela, text="")
mensagem_label.pack(pady=10)

# Iniciar o loop da interface
janela.mainloop()
