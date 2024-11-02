import tkinter as tk
from tkinter import filedialog, messagebox
import sounddevice as sd
from scipy.io import wavfile
import numpy as np
from PIL import Image, ImageTk

def escolherAudio():
    file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    if file_path:
        sample_rate, data = wavfile.read(file_path)
        messagebox.showinfo("Arquivo Carregado", f"Arquivo '{file_path}' carregado com sucesso!")

def gravacao(label_status, duracao, fs):
    label_status.config(text="Gravando...")
    janela.update()  # Atualiza a interface

    try:
        recording = sd.rec(int(duracao * fs), samplerate=fs, channels=1, dtype='float64')
        sd.wait()
        wavfile.write('gravacao.wav', fs, (recording * 32767).astype(np.int16))
        label_status.config(text="Gravação finalizada! Arquivo 'gravacao.wav' salvo.")
    except Exception as e:
        label_status.config(text="Erro na gravação.")
        messagebox.showerror("Erro", str(e))

def mostrarImgOk():
    # Carregar e exibir uma imagem
    try:
        imagem = Image.open("./img/ok.png")  # Substitua pelo caminho da sua imagem
        imagem = imagem.resize((200, 200), Image.LANCZOS)  # Redimensiona a imagem
        img_tk = ImageTk.PhotoImage(imagem)

        label_imagem = tk.Label(janela, image=img_tk)
        label_imagem.image = img_tk  # Manter uma referência à imagem
        label_imagem.place(x=100, y=90)  # Posição da imagem
    except Exception as e:
        messagebox.showerror("Erro ao carregar imagem", str(e))


def main():
    duracao = 2  # duração em segundos
    fs = 44100  # taxa de amostragem

    global janela
    janela = tk.Tk()
    janela.title("Interface Simples")
    janela.geometry("400x300")

    # Label de status
    label_status = tk.Label(janela, text="oi")
    label_status.place(x=30, y=20)

    # Botão de gravação
    gravar = tk.Button(janela, text="Gravar", command=lambda: gravacao(label_status, duracao, fs), width=15, height=2)
    gravar.place(x=25, y=40)

    # Botão para escolher arquivo
    escolherArquivo = tk.Button(janela, text="Escolher Arquivo", command=escolherAudio, width=20, height=2)
    escolherArquivo.place(x=230, y=40)

    mostrarImgOk()

    janela.mainloop()

main()
