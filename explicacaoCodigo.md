# tcc

- [Explicamento do codigo](explicacaoCodigo.md)

- [Interface](README.md)

O código implementa uma interface gráfica simples para gravação de áudio e exibição de seu espectrograma usando as bibliotecas `sounddevice`, `scipy`, `tkinter`, `numpy` e `matplotlib`.

## Importações

- **sounddevice**: para capturar áudio do microfone.
- **scipy.io.wavfile**: para salvar a gravação em formato WAV.
- **tkinter**: para criar a interface gráfica.
- **numpy**: para manipulação de arrays.
- **matplotlib**: para gerar gráficos, como o espectrograma.
- **FigureCanvasTkAgg**: para integrar gráficos do Matplotlib ao Tkinter.

## Configurações de Gravação

```python
duracao = 5  # duração em segundos
fs = 44100  # taxa de amostragem


```

## botão

```python
def on_button_click():
    print("Gravando...")
    label_status.config(text="Gravando...")

    # Gravação do áudio
    gravacao = sd.rec(int(duracao * fs), samplerate=fs, channels=1)
    sd.wait()  # espera até a gravação terminar
    print("Gravação finalizada!")

    # Salvando o arquivo
    wav.write('gravacao.wav', fs, gravacao)
    label_status.config(text="Gravação finalizada! Arquivo 'gravacao.wav' salvo.")

    # Mostrar espectrograma
    mostrar_espectrograma(gravacao.flatten())
```

## função para transformar o audio gravado em espectograma

```python

def mostrar_espectrograma(audio):
    plt.figure(figsize=(8, 4))
    plt.specgram(audio, NFFT=1024, Fs=fs, Fc=0, noverlap=512, cmap='plasma', sides='default', mode='default')
    plt.title('Espectrograma')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Frequência (Hz)')
    plt.colorbar(label='Intensidade')

    # Limpa a figura anterior
    for widget in frame_espectrograma.winfo_children():
        widget.destroy()

    # Adiciona o gráfico ao frame
    canvas = FigureCanvasTkAgg(plt.gcf(), master=frame_espectrograma)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
```

## criação da interface

```python

# Criar a janela principal
root = tk.Tk()
root.title("Interface de Gravação")
root.geometry("600x500")

# Criar um rótulo
label_status = tk.Label(root, text="Clique para gravar")
label_status.pack(pady=10)

# Criar um botão para gravar
button_gravar = tk.Button(root, text="Gravar", command=on_button_click)
button_gravar.pack(pady=10)

# Frame para o espectrograma
frame_espectrograma = tk.Frame(root)
frame_espectrograma.pack(fill=tk.BOTH, expand=True)

# Iniciar o loop da interface
root.mainloop()
```
