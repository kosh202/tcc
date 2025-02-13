import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Função para plotar o som original e o espectro de frequência
def plot_audio_and_fft(file_path):
    # Lê o arquivo de áudio
    sample_rate, data = wavfile.read(file_path)

    # Se o áudio for estéreo, pega apenas um canal
    if len(data.shape) > 1:
        data = data[:, 0]

    # Normaliza os dados
    data = data / np.max(np.abs(data))

    # Calcula o FFT
    fft_result = np.fft.fft(data)
    fft_magnitude = np.abs(fft_result)
    fft_freq = np.fft.fftfreq(len(fft_magnitude), 1/sample_rate)

    # Eixo de tempo em segundos
    time = np.linspace(0, len(data) / sample_rate, num=len(data))

    # Plota o som original
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.title('Som Original')
    plt.plot(time, data)
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')

    # Plota o espectro de frequência (log escala para magnitude)
    plt.subplot(2, 1, 2)
    plt.title('Espectro de Frequência (FFT)')
    plt.semilogy(fft_freq[:len(fft_freq)//2], fft_magnitude[:len(fft_magnitude)//2])  # Escala log no eixo y
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Magnitude (log)')

    plt.tight_layout()
    plt.show()

# Caminho para o arquivo de áudio
file_path = './seg_1.wav'  # Substitua pelo caminho do seu arquivo
plot_audio_and_fft(file_path)
