import soundfile as sf
from noisereduce.generate_noise import band_limited_noise
import matplotlib.pyplot as plt
import numpy as np

# Caminho do arquivo de áudio local
file_path = "tt1.wav" 
data, rate = sf.read(file_path)

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

# Salvar o áudio modificado como um arquivo .wav
sf.write('audio_com_ruido.wav', audio_clip_band_limited, rate)
