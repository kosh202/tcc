import os
def rename_files_in_directory(directory, prefix, log_file):
    # Obter a lista de arquivos no diretório e inicializar um contador
    files = sorted(os.listdir(directory))
    counter = 1
    with open(log_file, 'w') as log:
        log.write("Original Name -> New Name\n")

        for filename in files:
            # Definir o novo nome com prefixo e contador
            new_name = f"{prefix} {counter}.wav"
            original_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)

            # Renomear o arquivo
            os.rename(original_path, new_path)

            # Escrever no log o mapeamento do nome antigo para o novo
            log.write(f"{filename} -> {new_name}\n")

            # Incrementar o contador para o próximo arquivo
            counter += 1


# Caminhos dos diretórios e prefixos para cada caso
directories = {
    "anomaly": r"C:\Users\looui\OneDrive\Área de Trabalho\TCC\Projeto\tcc\dataset\Modificado\Treinamento\AudioOriginal\Renomeado\Anomaly",
    "noise": r"C:\Users\looui\OneDrive\Área de Trabalho\TCC\Projeto\tcc\dataset\Modificado\Treinamento\AudioOriginal\Renomeado\Noise",
    "ok": r"C:\Users\looui\OneDrive\Área de Trabalho\TCC\Projeto\tcc\dataset\Modificado\Treinamento\AudioOriginal\Renomeado\OK"
}


# Renomear arquivos e gerar logs para cada categoria
for category, path in directories.items():
    prefix = category.capitalize()  # Define o prefixo (Anomaly, Noise, OK)
    log_file = f"{path}/{prefix}_rename_log.txt"  # Arquivo de log para os mapeamentos
    rename_files_in_directory(path, prefix, log_file)
