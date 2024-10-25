import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, lfilter

def plot_spectrogram(data, sample_rate, title):
    """Plot the spectrogram of the given audio data."""
    plt.specgram(data, Fs=sample_rate)
    plt.title(title)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')

def remove_noise(data, sample_rate, cutoff=3000, order=5):
    """Apply a low-pass filter to remove noise from the audio data."""
    nyquist = 0.5 * sample_rate
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    filtered_data = lfilter(b, a, data)
    return filtered_data

def save_audio(filtered_data, sample_rate):
    # Abrir um diálogo para salvar o arquivo WAV
    save_path = filedialog.asksaveasfilename(defaultextension=".wav", 
                                               filetypes=[("WAV files", "*.wav")])
    if save_path:
        # Salvar o áudio filtrado
        wavfile.write(save_path, sample_rate, filtered_data.astype(np.int16))

def display_spectrograms(file_path):
    """Load audio file, remove noise, and display spectrograms."""
    # Load the audio file
    sample_rate, data = wavfile.read(file_path)

    # Remove noise from the audio data
    filtered_data = remove_noise(data, sample_rate)

    # Create a figure to display the spectrograms
    plt.figure(figsize=(12, 8))

    # Plot original spectrogram
    plt.subplot(2, 1, 1)
    plot_spectrogram(data, sample_rate, 'Original Spectrogram')

    # Plot filtered spectrogram
    plt.subplot(2, 1, 2)
    plot_spectrogram(filtered_data, sample_rate, 'Noise-Reduced Spectrogram')

    # Adjust layout and show the plots
    plt.tight_layout()
    plt.show()

def process_audio():
    # Abrir um diálogo para selecionar o arquivo WAV
    file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    
    if file_path:
        # Ler o arquivo WAV
        sample_rate, data = wavfile.read(file_path)
        
        # Remover ruído
        filtered_data = remove_noise(data, sample_rate)
        
        # # Plotar espectrograma do áudio original
        # plt.figure(figsize=(10, 4))
        # plt.subplot(2, 1, 1)
        # plt.title('Espectrograma - Original')
        # plot_spectrogram(data, sample_rate)
        
        # # Plotar espectrograma do áudio filtrado
        # plt.subplot(2, 1, 2)
        # plt.title('Espectrograma - Filtrado')
        # plot_spectrogram(filtered_data, sample_rate)
        
        # # Mostrar os espectrogramas em uma nova janela
        # plt.tight_layout()
        # plt.show()

        display_spectrograms(file_path)
        
        # Salvar o áudio filtrado
        save_audio(filtered_data, sample_rate)

def criar_janela():
    # Criar a janela principal
    root = tk.Tk()
    root.title("Retirar Ruído")
    root.geometry("400x300") 

    # Criar os botões

    button = tk.Button(root, text="Carregar WAV e Mostrar Espectrograma", command=process_audio)
    button.pack(pady=20)

    # Iniciar o loop principal da interface gráfica
    root.mainloop()

def main():
    criar_janela()

main()