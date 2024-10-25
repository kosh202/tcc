from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Função para abrir o diálogo de seleção de arquivo
def selecionar_arquivo():
    Tk().withdraw()  # Oculta a janela principal
    arquivo = askopenfilename(title="Selecione um arquivo de áudio", filetypes=[("Arquivos de Áudio", "*.mp3;*.wav;*.ogg")])
    return arquivo

# Função para plotar espectrograma
def plotar_espectrograma(ax, audio, titulo):
    samples = np.array(audio.get_array_of_samples())
    if audio.channels == 2:
        samples = samples[::2]  # Usa apenas um dos canais
    Pxx, freqs, bins, im = ax.specgram(samples, NFFT=1024, Fs=audio.frame_rate, noverlap=512)
    ax.set_title(titulo)
    ax.set_xlabel("Tempo (s)")
    ax.set_ylabel("Frequência (Hz)")
    plt.colorbar(im, ax=ax, label='Intensidade')

# Função para ajustar o volume do áudio
def ajustar_volume(audio, db):
    return audio + db  # db positivo aumenta o volume, negativo diminui

# Selecionar os arquivos de áudio
print("Selecione o primeiro arquivo de áudio:")
audio1_path = selecionar_arquivo()
print("Selecione o segundo arquivo de áudio:")
audio2_path = selecionar_arquivo()

# Carregar os áudios
audio1 = AudioSegment.from_file(audio1_path)
audio2 = AudioSegment.from_file(audio2_path)

# Ajustar o volume dos áudios (exemplo: diminuir 6 dB)
audio1 = ajustar_volume(audio1, -6)  # Ajuste o valor conforme necessário
audio2 = ajustar_volume(audio2, -6)  # Ajuste o valor conforme necessário

# Criar a figura e os eixos para os espectrogramas
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# Plotar espectrogramas
plotar_espectrograma(axs[0], audio1, "Espectrograma do Áudio 1")
plotar_espectrograma(axs[1], audio2, "Espectrograma do Áudio 2")

# Sobrepor os áudios
audio_final = audio1.overlay(audio2)

# Plotar espectrograma do áudio final
plotar_espectrograma(axs[2], audio_final, "Espectrograma do Áudio Final")

# Ajustar layout e mostrar todos os espectrogramas
plt.tight_layout()
plt.show()

# Exportar o áudio final
audio_final.export("audio_final.mp3", format="mp3")
print("Áudio final exportado como 'audio_final.mp3'")
