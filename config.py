# Diretório onde estão os arquivos a serem processados
source_directory = r"C:\Users\gomes\PhpstormProjects\mauricio-araujo"

# Arquivo onde será salvo o conteúdo processado
output_file = "output/araja.txt"

# Extensões de arquivos que deseja buscar, deixe vazio para pegar todos os arquivos
file_extensions = []  # Ou deixe vazio []

# Extensões de arquivos que você deseja excluir
exclude_extensions = ['log', 'csr', 'key', 'pem', 'txt', 'gz',
                      'ini']  # Por exemplo, exclua arquivos temporários ou logs

# Nomes de arquivos que você deseja excluir
exclude_file_names = []

# Diretórios que você deseja excluir (exemplo: excluir o diretório .git)
exclude_directories = [
    '.idea',
    '.venv',
    'output',
    '.git',
    '__pycache__',
    'data',
    '.composer',
    'cms',
    '.scpts',
    'ssl',
    'backup-drupal-files'
    '.scpts',
    '.ssh',
    'backup-drupal-files',
    'database',
    'images',
    'scripts'
]
