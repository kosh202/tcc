# import librosa
# import noisereduce
# import soundfile as sf

# # Carregar o áudio
# audio, sr = librosa.load('audio.wav')

# # Reduzir o ruído
# reduced_noise = noisereduce.reduce_noise(y=audio, sr=sr)

# # Salvar o áudio processado
# sf.write('audio_processado.wav', reduced_noise, sr)


import tkinter as tk
from tkinter import filedialog
import librosa
import numpy as np
import matplotlib.pyplot as plt
import noisereduce as nr
import librosa.display

def carregar_audio():
    arquivo = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3;*.flac")])
    if arquivo:
        y, sr = librosa.load(arquivo)
        mostrar_espectrograma(y, sr)

def reduzir_ruido_e_mostrar():
    arquivo = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3;*.flac")])
    if arquivo:
        y, sr = librosa.load(arquivo)
        # Reduzir ruído
        y_reduzido = nr.reduce_noise(y=y, sr=sr)
        # Mostrar espectrograma do áudio tratado
        mostrar_espectrograma(y_reduzido, sr)

def mostrar_espectrograma(y, sr):
    # Calcular o espectrograma
    espectrograma = librosa.feature.melspectrogram(y=y, sr=sr)
    espectrograma_db = librosa.power_to_db(espectrograma, ref=np.max)

    # Plotar o espectrograma
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(espectrograma_db, sr=sr, x_axis='time', y_axis='mel', cmap='coolwarm')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Espectrograma')
    plt.tight_layout()
    plt.show()

# Criar a interface
root = tk.Tk()
root.title("Visualizador de Espectrograma")

botao_carregar = tk.Button(root, text="Selecionar Áudio", command=carregar_audio)
botao_carregar.pack(pady=10)

botao_reduzir_ruido = tk.Button(root, text="Reduzir Ruído e Mostrar Espectrograma", command=reduzir_ruido_e_mostrar)
botao_reduzir_ruido.pack(pady=10)

root.mainloop()

