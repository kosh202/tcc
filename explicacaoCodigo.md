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
