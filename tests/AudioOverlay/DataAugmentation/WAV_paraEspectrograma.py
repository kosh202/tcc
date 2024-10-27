import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askdirectory

def select_directory(prompt):
    """Abre uma janela para o usuário selecionar um diretório."""
    Tk().withdraw()  # Oculta a janela principal do Tkinter
    directory = askdirectory(title=prompt)
    return directory

def plot_spectrograms(original_dir, augmented_dir):
    # Obter listas de arquivos dos diretórios
    original_files = sorted(os.listdir(original_dir))
    augmented_files = sorted(os.listdir(augmented_dir))

    # Verificar se ambos os diretórios têm o mesmo número de arquivos
    if len(original_files) != len(augmented_files):
        print("Os diretórios devem ter a mesma quantidade de arquivos.")
        return

    # Configurar a figura
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    index = 0

    while True:
        # Carregar os arquivos de áudio
        original_file = original_files[index]
        augmented_file = augmented_files[index]

        # Carregar os áudios
        original_audio, sr_original = librosa.load(os.path.join(original_dir, original_file), sr=None)
        augmented_audio, sr_augmented = librosa.load(os.path.join(augmented_dir, augmented_file), sr=None)

        # Calcular espectrogramas
        S_original = librosa.feature.melspectrogram(y=original_audio, sr=sr_original, n_mels=128)
        S_augmented = librosa.feature.melspectrogram(y=augmented_audio, sr=sr_augmented, n_mels=128)

        # Converter para decibéis
        S_db_original = librosa.power_to_db(S_original, ref=np.max)
        S_db_augmented = librosa.power_to_db(S_augmented, ref=np.max)

        # Plotar os espectrogramas
        axs[0].clear()
        axs[1].clear()

        librosa.display.specshow(S_db_original, sr=sr_original, x_axis='time', y_axis='mel', ax=axs[0])
        axs[0].set_title(f'Original: {original_file}')
        axs[0].label_outer()

        librosa.display.specshow(S_db_augmented, sr=sr_augmented, x_axis='time', y_axis='mel', ax=axs[1])
        axs[1].set_title(f'Augmented: {augmented_file}')
        axs[1].label_outer()

        plt.pause(0.001)

        # Instruções para navegação
        print(f"Comparando {original_file} com {augmented_file}.")
        print("Pressione 'n' para a próxima comparação, 'p' para a anterior ou 'q' para sair.")

        while True:
            action = input("Escolha uma opção (n/p/q): ")
            if action == 'n' and index < len(original_files) - 1:
                index += 1
                break
            elif action == 'p' and index > 0:
                index -= 1
                break
            elif action == 'q':
                plt.close(fig)
                return
            else:
                print("Opção inválida. Tente novamente.")

# Seleção dos diretórios pelo usuário
original_dir = select_directory("Selecione o diretório dos áudios originais")
augmented_dir = select_directory("Selecione o diretório dos áudios somados")

# Executar a comparação de espectrogramas
plot_spectrograms(original_dir, augmented_dir)
