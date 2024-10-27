import os
import random
from pydub import AudioSegment


def limited_overlay(source_dir, noise_dir, output_dir, max_noise_usage=2):
    # Verificar se já existem arquivos no diretório de saída
    if os.path.exists(output_dir) and os.listdir(output_dir):
        resposta = input(f"O diretório de saída '{output_dir}' já contém arquivos. Deseja continuar? (s/n): ")
        if resposta.lower() != 's':
            print("Operação cancelada.")
            return

    # Obter lista de arquivos no diretório de origem e lista de ruídos
    source_files = sorted(os.listdir(source_dir))  # Mantenha a ordem cronológica
    noise_files = sorted(os.listdir(noise_dir))

    # Contagens de arquivos
    print(f"Atualmente existem: {len(source_files)} áudios e {len(noise_files)} áudios de Noise.")

    # Controle de uso para cada arquivo de ruído
    noise_usage_count = {noise: 0 for noise in noise_files}

    # Criar o diretório de saída, se não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for idx, audio_file in enumerate(source_files):
        # Carregar o áudio de origem
        audio_path = os.path.join(source_dir, audio_file)
        audio = AudioSegment.from_file(audio_path)

        # Selecionar um ruído aleatório que ainda tenha menos de max_noise_usage
        available_noises = [noise for noise, count in noise_usage_count.items() if count < max_noise_usage]

        if available_noises:
            noise_file = random.choice(available_noises)
            noise_path = os.path.join(noise_dir, noise_file)
            noise = AudioSegment.from_file(noise_path)

            # Atualizar o contador do ruído selecionado
            noise_usage_count[noise_file] += 1

            # Ajustar duração do ruído ao áudio, se necessário
            if len(noise) > len(audio):
                noise = noise[:len(audio)]
            elif len(noise) < len(audio):
                noise = noise * (len(audio) // len(noise) + 1)
                noise = noise[:len(audio)]

            # Realizar o overlay e salvar o novo arquivo
            output_filename = f"{audio_file.split('.')[0]}+{noise_file.split('.')[0]}.wav"
            combined_audio = audio.overlay(noise)
            combined_audio.export(os.path.join(output_dir, output_filename), format="wav")

            # Mensagens de saída para monitoramento do processo
            print(f"Somando {audio_file} com Noise ({noise_file}) -> Salvo como {output_filename}")


# Caminhos para os diretórios
anomaly_dir = r"C:\Users\looui\OneDrive\Área de Trabalho\TCC\Projeto\tcc\dataset\Modificado\Treinamento\AudioOriginal\Renomeado\Anomaly"  # Diretório dos arquivos "Anomaly"
noise_dir = r"C:\Users\looui\OneDrive\Área de Trabalho\TCC\Projeto\tcc\dataset\Modificado\Treinamento\AudioOriginal\Renomeado\Noise"  # Diretório dos arquivos "Noise"
output_dir_anomaly = r"C:\Users\looui\OneDrive\Área de Trabalho\TCC\Projeto\tcc\dataset\Modificado\Treinamento\Augmented Audio\Overlay\Limited Overlay\Anomaly_Aug"  # Diretório de saída para os áudios Anomaly

# Executar o overlay balanceado para "Anomaly"
limited_overlay(anomaly_dir, noise_dir, output_dir_anomaly)
