import tkinter as tk
from tkinter import filedialog
import sounddevice as sd
from scipy.io import wavfile
import numpy as np

def esolherAudio():
    # Open a dialog to select the WAV file
    file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    
    if file_path:
        # Read the WAV file
        sample_rate, data = wavfile.read(file_path)
        
        # Optionally process audio here
        # filtered_data = remove_noise(data, sample_rate)
        
        # Display spectrograms if needed
        # display_spectrograms(file_path)
        
        # Optionally save the processed audio
        # save_audio(filtered_data, sample_rate)

def gravacao(label_status, duracao, fs):
    print("Gravando...")
    label_status.config(text="Gravando...")
    
    # Record audio
    recording = sd.rec(int(duracao * fs), samplerate=fs, channels=1, dtype='float64')
    sd.wait()  # Wait until recording is finished
    print("Gravação finalizada!")

    # Save the audio file
    wavfile.write('gravacao.wav', fs, (recording * 32767).astype(np.int16))
    label_status.config(text="Gravação finalizada! Arquivo 'gravacao.wav' salvo.")
  
def main():
    duracao = 2  # duration in seconds
    fs = 44100  # sample rate

    # Create the main window
    janela = tk.Tk()
    janela.title("Interface Simples")
    janela.geometry("400x300")  # window size

    # Create a button to start recording
    gravar = tk.Button(janela, text="Gravar", command=lambda: gravacao(label_status, duracao, fs))
    gravar.pack(pady=10)

    # Create a button to choose a file
    escolherArquivo = tk.Button(janela, text="Escolher Arquivo", command=esolherAudio)
    escolherArquivo.pack(pady=10)

    # Create a label to display messages
    label_status = tk.Label(janela, text=" ")
    label_status.pack(pady=10)

    # Start the GUI main loop
    janela.mainloop()

main()
