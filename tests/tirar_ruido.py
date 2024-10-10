import librosa
import noisereduce
import soundfile as sf

# Carregar o áudio
audio, sr = librosa.load('audio.wav')

# Reduzir o ruído
reduced_noise = noisereduce.reduce_noise(y=audio, sr=sr)

# Salvar o áudio processado
sf.write('audio_processado.wav', reduced_noise, sr)
