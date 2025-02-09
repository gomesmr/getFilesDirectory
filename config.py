import os

# Diretório onde estão os arquivos a serem processados
source_directory = os.getenv("SOURCE_DIRECTORY", r"C:\Users\gomes\PycharmProjects\getFilesDirectory")

# Arquivo onde será salvo o conteúdo processado
output_file = os.getenv("OUTPUT_FILE", "output/script.txt")

# Extensões de arquivos que deseja buscar (deixe vazio para incluir todos)
file_extensions = os.getenv("FILE_EXTENSIONS", "").split(",") if os.getenv("FILE_EXTENSIONS") else []

# Extensões de arquivos que você deseja excluir
exclude_extensions = os.getenv("EXCLUDE_EXTENSIONS", "log,csr,key,pem,txt,gz").split(",")

# Nomes de arquivos que você deseja excluir
exclude_file_names = os.getenv("EXCLUDE_FILE_NAMES", "php.ini").split(",")

# Diretórios que você deseja excluir
exclude_directories = [
    ".idea",
    ".venv",
    "output",
    ".git",
    "__pycache__",
    "data",
    ".composer",
    "cms",
    "ssl",
    "backup-drupal-files",
    ".ssh",
    "database",
    "images",
    "scripts"
]
