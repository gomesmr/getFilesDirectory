import chardet

class FileConverter:
    """Responsável por converter arquivos para UTF-8."""
    @staticmethod
    def convert_to_utf8(file_path):
        try:
            with open(file_path, 'rb') as f:
                raw_data = f.read()
                detected = chardet.detect(raw_data)
                encoding = detected['encoding']
            with open(file_path, 'r', encoding=encoding, errors='replace') as infile:
                content = infile.read()
            with open(file_path, 'w', encoding='utf-8') as outfile:
                outfile.write(content)
        except Exception as e:
            raise Exception(f"Erro ao converter o arquivo {file_path} para UTF-8: {e}")