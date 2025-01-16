class FileFilter:
    """Responsável por filtrar arquivos e diretórios."""
    def __init__(self, file_extensions=None, exclude_extensions=None, exclude_file_names=None, exclude_directories=None):
        self.file_extensions = file_extensions or []
        self.exclude_extensions = exclude_extensions or []
        self.exclude_file_names = exclude_file_names or []
        self.exclude_directories = exclude_directories or []

    def should_process_file(self, file_name):
        """Verifica se o arquivo deve ser processado."""
        if file_name in self.exclude_file_names:
            return False
        if any(file_name.endswith(ext) for ext in self.exclude_extensions):
            return False
        if not self.file_extensions or any(file_name.endswith(ext) for ext in self.file_extensions):
            return True
        return False

    def filter_directories(self, directories):
        """Remove diretórios que estão na lista de exclusão."""
        return [d for d in directories if d not in self.exclude_directories]