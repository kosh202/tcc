
# sounddevice: Esta biblioteca permite a gravação e reprodução de áudio usando dispositivos de som disponíveis no sistema.
# scipy.io.wavfile: Esta parte do SciPy é usada para ler e escrever arquivos WAV
import sounddevice as sd
import scipy.io.wavfile as wav

# cria a interface
import tkinter as tk

# Configurações de gravação
duracao = 5  # duração em segundos
fs = 44100  # taxa de amostragem

def on_button_click():
    print("Gravando...")
    # Gravação do áudio
    gravacao = sd.rec(int(duracao * fs), samplerate=fs, channels=1)
    sd.wait()  # espera até a gravação terminar
    print("Gravação finalizada!")

    # Salvando o arquivo
    wav.write('gravacao.wav', fs, gravacao)
    

# Criar a janela principal
root = tk.Tk()
root.title("interfaze test")
root.geometry("300x200")

# Criar um rótulo
label = tk.Label(root, text="comecar gravacao")
label.pack(pady=10)

# Criar um botão
button = tk.Button(root, text="gravar", command=on_button_click)
button.pack(pady=10)

# Iniciar o loop da interface
root.mainloop()