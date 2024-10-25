import os
import librosa

# Diretório onde os arquivos de áudio estão localizados
directory = r"C:\Users\looui\OneDrive\Área de Trabalho\TCC\Projeto\tcc\dataset\Modificado\Treinamento\AudioOriginal"

# Inicializando contadores e lista para armazenar a duração dos áudios
anomaly_count = 0
noise_count = 0
ok_count = 0
durations = []

# Percorrer todos os arquivos no diretório
for filename in os.listdir(directory):
    if filename.endswith(".wav"):  # Verificar se o arquivo é um áudio (ou outro formato se necessário)
        filepath = os.path.join(directory, filename)

        # Carregar o áudio e calcular a duração
        audio, sr = librosa.load(filepath, sr=None)  # sr=None mantém a taxa de amostragem original
        duration = librosa.get_duration(y=audio, sr=sr)
        durations.append(duration)

        # Contar a categoria de acordo com o nome do arquivo
        if filename.startswith("Anomaly"):
            anomaly_count += 1
        elif filename.startswith("Noise"):
            noise_count += 1
        elif filename.startswith("OK"):
            ok_count += 1

# Exibindo as informações
print(f"Total de arquivos 'Anomaly': {anomaly_count}")
print(f"Total de arquivos 'Noise': {noise_count}")
print(f"Total de arquivos 'OK': {ok_count}")
print(f"Duração média dos áudios: {sum(durations) / len(durations):.2f} segundos")
