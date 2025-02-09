import os
import re

from file_converter import FileConverter


class FileProcessor:
    """Responsável por processar arquivos e gerar a saída."""
    def __init__(self, source_directory, output_file, file_filter):
        self.source_directory = source_directory
        self.output_file = output_file
        self.file_filter = file_filter

    def process_files(self):
        """Processa os arquivos e escreve as informações no arquivo de saída."""
        with open(self.output_file, 'w', encoding='utf-8') as outfile:
            for root, dirs, files in os.walk(self.source_directory):
                # Filtra os diretórios
                dirs[:] = self.file_filter.filter_directories(dirs)
                for file in files:
                    if self.file_filter.should_process_file(file):
                        file_path = os.path.join(root, file)
                        self._process_single_file(file_path, file, outfile)

    def _process_single_file(self, file_path, file_name, outfile):
        """Processa um único arquivo."""
        try:
            # Converte o arquivo para UTF-8
            FileConverter.convert_to_utf8(file_path)

            # Lê o conteúdo do arquivo
            with open(file_path, 'r', encoding='utf-8', errors='replace') as infile:
                content = infile.read()

            # Remove padrões como [;,#].[A-z]*.*
            content = re.sub(r'[;,#].[A-Za-z]*\..*', '', content)

            # Substitui recursivamente \n\n por \n
            while '\n\n' in content:
                content = content.replace('\n\n', '\n')

            # Escreve as informações do arquivo no arquivo de saída
            outfile.write("-" * 40 + "\n")  # Separador para melhor leitura
            outfile.write(f"Arquivo: {file_name}\n")
            outfile.write(f"Caminho: {file_path}\n")
            outfile.write("=" * 40 + "\n")  # Separador para melhor leitura
            outfile.write(content)
            outfile.write("\n\n")  # Adiciona uma nova linha entre arquivos
        except Exception as e:
            print(f"Erro ao processar o arquivo {file_path}: {e}")