# codigo simples

import librosa
import noisereduce

# Carregar o áudio
audio, sr = librosa.load('audio.wav')

# Reduzir o ruído
reduced_noise = noisereduce.reduce_noise(y=audio, sr=sr)

# Salvar o áudio processado
librosa.output.write_wav('audio_processado.wav', reduced_noise, sr)