# Arquivo __init__.py com as configurações do script

# Diretório onde estão os arquivos a serem processados
source_directory = "c:\\Users\\gomes\\Downloads\\123\\apache2"

# Arquivo onde será salvo o conteúdo processado
output_file = "apache.txt"

# Extensões de arquivos que deseja buscar, deixe vazio para pegar todos os arquivos
file_extensions = ['conf']  # Ou deixe vazio []

# Extensões de arquivos que você deseja excluir
exclude_extensions = ['.md', '.gitignore', '.swp']  # Por exemplo, exclua arquivos temporários ou logs

# Diretórios que você deseja excluir (exemplo: excluir o diretório .git)
exclude_directories = ['.git', '.idea', 'test', 'js']
