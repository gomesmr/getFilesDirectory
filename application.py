import os
from file_filter import FileFilter
from file_processor import FileProcessor

class Application:
    """Classe principal para configurar e executar o processamento."""

    @staticmethod
    def run():
        source_directory = "c:\\Users\\gomes\\Downloads\\123\\apache2"
        output_directory = "output"  # Diretório de saída
        output_file = os.path.join(output_directory, "apache.txt")  # Arquivo de saída

        # Cria o diretório de saída, se não existir
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Configurações de filtros
        file_extensions = ['conf']  # Extensões de arquivos que deseja buscar
        exclude_extensions = ['.md', '.gitignore', '.swp']  # Extensões de arquivos a excluir
        exclude_file_names = ['example.conf', 'test.conf']  # Nomes de arquivos a excluir
        exclude_directories = ['.git', '.idea', 'test', 'js']  # Diretórios a excluir

        # Cria o filtro de arquivos
        file_filter = FileFilter(
            file_extensions=file_extensions,
            exclude_extensions=exclude_extensions,
            exclude_file_names=exclude_file_names,
            exclude_directories=exclude_directories
        )

        # Processa os arquivos
        processor = FileProcessor(source_directory, output_file, file_filter)
        processor.process_files()

        print(f"Conteúdo dos arquivos foi copiado para {output_file}")