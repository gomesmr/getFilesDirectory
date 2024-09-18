import os
import __ini__  # Importa o arquivo de configurações


def gather_files_by_extension(source_directory, output_file, file_extensions, exclude_extensions=None, out_list_directories=None):
    out_list_directories = out_list_directories or []  # Define como lista vazia se for None
    exclude_extensions = exclude_extensions or []  # Define como lista vazia se for None
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(source_directory):
            # Remove os diretórios que estão na lista de exclusão
            dirs[:] = [d for d in dirs if d not in out_list_directories]

            for file in files:
                # Se o array de extensões de exclusão estiver vazio, exclui apenas os tipos de arquivo desejados
                if not any(file.endswith(ext) for ext in exclude_extensions):
                    # Se o array de extensões estiver vazio, pega todos os arquivos
                    if not file_extensions or any(file.endswith(ext) for ext in file_extensions):
                        file_path = os.path.join(root, file)

                        # Escreve o nome e o caminho do arquivo no arquivo de saída
                        outfile.write("-" * 40 + "\n")  # Separador para melhor leitura
                        outfile.write(f"Arquivo: {file}\n")
                        outfile.write(f"Caminho: {file_path}\n")
                        outfile.write("=" * 40 + "\n")  # Separador para melhor leitura

                        # Lê e escreve o conteúdo do arquivo no arquivo de saída
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            outfile.write(infile.read())
                            outfile.write("\n\n")  # Adiciona uma nova linha entre arquivos


# Chama a função com os parâmetros definidos no arquivo __ini__.py
gather_files_by_extension(
    __ini__.source_directory,
    __ini__.output_file,
    __ini__.file_extensions,
    __ini__.exclude_extensions,
    __ini__.exclude_directories
)

print(f"Conteúdo dos arquivos foi copiado para {__ini__.output_file}")
