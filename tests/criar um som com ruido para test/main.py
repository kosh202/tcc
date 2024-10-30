import soundfile as sf
from noisereduce.generate_noise import band_limited_noise
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog
import os

def escolher_arquivo():
    """Abre uma janela para o usuário escolher o arquivo de áudio."""
    root = tk.Tk()
    root.withdraw()  # Não exibe a janela principal
    file_path = filedialog.askopenfilename(title="Escolha o arquivo de áudio", filetypes=[("Arquivo WAV", "*.wav")])
    return file_path

def escolher_pasta_destino():
    """Abre uma janela para o usuário escolher a pasta de destino para salvar o áudio com ruído."""
    root = tk.Tk()
    root.withdraw()  # Não exibe a janela principal
    folder_path = filedialog.askdirectory(title="Escolha a pasta para salvar o áudio com ruído")
    return folder_path

# Escolher o arquivo de áudio
file_path = escolher_arquivo()
if not file_path:
    print("Nenhum arquivo de áudio selecionado.")
    exit()

try:
    # Ler o arquivo de áudio
    data, rate = sf.read(file_path)
except Exception as e:
    print(f"Erro ao ler o arquivo de áudio: {e}")
    exit()

# Adicionar ruído
noise_len = 2  # segundos
noise = band_limited_noise(min_freq=2000, max_freq=12000, samples=len(data), samplerate=rate) * 10
audio_clip_band_limited = data + noise

# Criar a janela para os gráficos
plt.figure(figsize=(20, 8))

# Gráfico do áudio original
plt.subplot(1, 2, 1)
plt.plot(data)
plt.title("Áudio Original")
plt.xlabel("Amostras")
plt.ylabel("Amplitude")

# Gráfico do áudio modificado
plt.subplot(1, 2, 2)
plt.plot(audio_clip_band_limited)
plt.title("Áudio com Ruído Adicionado")
plt.xlabel("Amostras")
plt.ylabel("Amplitude")

# Exibir os gráficos
plt.tight_layout()
plt.show()

# Escolher a pasta de destino para salvar o arquivo
folder_path = escolher_pasta_destino()
if not folder_path:
    print("Nenhuma pasta selecionada.")
    exit()

# Definir o nome do arquivo de saída
output_file = os.path.join(folder_path, "audio_com_ruido.wav")

try:
    # Salvar o áudio modificado como um arquivo .wav na pasta escolhida
    sf.write(output_file, audio_clip_band_limited, rate)
    print(f"Áudio com ruído salvo em: {output_file}")
except Exception as e:
    print(f"Erro ao salvar o arquivo de áudio: {e}")
