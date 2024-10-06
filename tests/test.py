import sounddevice as sd
import scipy.io.wavfile as wav
import tkinter as tk
from tkinter import messagebox

# Configurações de gravação
duracao = 5  # duração em segundos
fs = 44100  # taxa de amostragem

def on_button_click():
    print("Gravando...")
    label_status.config(text="Gravando...")
    # Gravação do áudio
    gravacao = sd.rec(int(duracao * fs), samplerate=fs, channels=1)
    sd.wait()  # espera até a gravação terminar
    print("Gravação finalizada!")
    label_status.config(text="Gravação finalizada! Arquivo salvo como 'gravacao.wav'.")
    
    # Salvando o arquivo
    wav.write('gravacao.wav', fs, gravacao)

def play_audio():
    try:
        fs, audio_data = wav.read('gravacao.wav')
        print("Reproduzindo...")
        sd.play(audio_data, fs)
        sd.wait()  # espera até a reprodução terminar
        print("Reprodução finalizada!")
        label_status.config(text="Reprodução finalizada!")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível reproduzir o áudio: {e}")

# Criar a janela principal
root = tk.Tk()
root.title("Interface de Gravação")
root.geometry("300x200")

# Criar um rótulo
label_status = tk.Label(root, text="Clique para gravar")
label_status.pack(pady=10)

# Criar um botão para gravar
button_gravar = tk.Button(root, text="Gravar", command=on_button_click)
button_gravar.pack(pady=10)

# Criar um botão para reproduzir o áudio
button_play = tk.Button(root, text="Reproduzir", command=play_audio)
button_play.pack(pady=10)

# Iniciar o loop da interface
root.mainloop()
