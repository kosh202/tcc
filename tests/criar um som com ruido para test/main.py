import soundfile as sf
from noisereduce.generate_noise import band_limited_noise
import matplotlib.pyplot as plt
import urllib.request
import io
import numpy as np

# URL do arquivo de áudio
url = "https://raw.githubusercontent.com/timsainb/noisereduce/master/assets/fish.wav"
response = urllib.request.urlopen(url)

# Ler o áudio
data, rate = sf.read(io.BytesIO(response.read()))

# Adicionar ruído
# Defina a intensidade do ruído (por exemplo, 0.005)
# noise_intensity = 0.005
# noise = noise_intensity * np.random.randn(*data.shape)
noise_len = 2 # seconds
noise = band_limited_noise(min_freq=2000, max_freq = 12000, samples=len(data), samplerate=rate)*10
noise_clip = noise[:rate*noise_len]

# Misturar o áudio original com o ruído
audio_clip_band_limited = data + noise

# Plotar o áudio com ruído
plt.figure(figsize=(20, 3))
plt.plot(audio_clip_band_limited)
plt.title("Áudio com Ruído Adicionado")
plt.show()

# Salvar o áudio modificado como um arquivo .wav
sf.write('audio_com_ruido.wav', audio_clip_band_limited, rate)
