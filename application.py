import os
from file_filter import FileFilter
from file_processor import FileProcessor
import config  # Importa as configurações do arquivo config.py


class Application:
    """Classe principal para configurar e executar o processamento."""

    @staticmethod
    def run():
        # Carrega as configurações do arquivo config.py
        source_directory = config.source_directory
        output_file = config.output_file
        file_extensions = config.file_extensions
        exclude_extensions = config.exclude_extensions
        exclude_file_names = config.exclude_file_names
        exclude_directories = config.exclude_directories

        # Diretório de saída (baseado no caminho do arquivo de saída)
        output_directory = os.path.dirname(output_file)

        # Cria o diretório de saída se não existir e verificar permissões
        os.makedirs(output_directory, exist_ok=True)

        # Se o arquivo de saída já existir, remove para evitar dados duplicados
        if os.path.exists(output_file):
            os.remove(output_file)

        # Criar e aplicar o filtro de arquivos
        file_filter = FileFilter(
            file_extensions=file_extensions,
            exclude_extensions=exclude_extensions,
            exclude_file_names=exclude_file_names,
            exclude_directories=exclude_directories
        )

        # Processa os arquivos
        processor = FileProcessor(source_directory, output_file, file_filter)
        processor.process_files()

        print(f"✅ Processamento concluído! O conteúdo foi salvo em: {output_file}")


if __name__ == "__main__":
    Application.run()
