import numpy as np
import librosa
import soundfile as sf
import matplotlib.pyplot as plt

# Passo 1: Carregar o áudio
audio, sr = librosa.load('audio.wav', sr=None)

# Passo 2: Aplicar a Transformada Rápida de Fourier (FFT)
audio_fft = np.fft.fft(audio)

# Passo 3: Visualizar o espectro de frequências
frequencies = np.fft.fftfreq(len(audio), 1/sr)

plt.figure(figsize=(10, 6))
plt.plot(frequencies[:len(frequencies)//2], np.abs(audio_fft)[:len(frequencies)//2])
plt.title('Espectro de Frequências do Áudio')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
plt.grid()
plt.show()

# Passo 4: Identificar e remover ou atenuar frequências de ruído
# Defina as faixas de frequências do ruído
# Exemplo: supomos que o ruído está entre 1000Hz e 2000Hz
frequencias_ruido = (frequencies > 1000) & (frequencies < 2000)

# Atenuar as frequências de ruído
audio_fft[frequencias_ruido] = 0
audio_fft[-frequencias_ruido] = 0  # Atenuar as frequências negativas (simétricas)

# Passo 5: Reconstruir o áudio no domínio do tempo
audio_filtrado = np.fft.ifft(audio_fft)

# Converter o áudio filtrado para valores reais (descartar parte imaginária devido a erro numérico)
audio_filtrado = np.real(audio_filtrado)

# Passo 6: Salvar o áudio filtrado
sf.write('audio_filtrado.wav', audio_filtrado, sr)

# Opcional: Reproduzir o áudio filtrado (caso queira ouvir)
import sounddevice as sd
sd.play(audio_filtrado, sr)
sd.wait()
