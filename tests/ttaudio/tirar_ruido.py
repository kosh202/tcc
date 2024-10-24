import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.io import wavfile

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
    if file_path:
        plot_spectrogram(file_path)

def plot_spectrogram(file_path):
    # Lê o arquivo de áudio
    sample_rate, data = wavfile.read(file_path)

    # Limpa a figura anterior
    for widget in frame.winfo_children():
        widget.destroy()

    # Cria uma nova figura
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.specgram(data, Fs=sample_rate, NFFT=2048, noverlap=1024, cmap='plasma')
    ax.set_title('Espectrogram')
    ax.set_xlabel('Tempo (s)')
    ax.set_ylabel('Frequência (Hz)')
    plt.colorbar(ax.get_children()[0], ax=ax, label='Intensidade')

    # Integra a figura com o Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Criação da interface
root = tk.Tk()
root.title("Selecione um arquivo de áudio")

# Botão para abrir o arquivo
button = tk.Button(root, text="Selecionar Arquivo .wav", command=open_file)
button.pack(pady=20)

# Frame para o espectrograma
frame = tk.Frame(root)
frame.pack(pady=20)

# Iniciar o loop da interface
root.mainloop()
