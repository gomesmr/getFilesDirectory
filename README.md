# **File Processing Project Documentation**

This project is designed to process files from a specified directory, filter them based on user-defined criteria, and output the processed content to a file. The project follows clean code principles and adheres to the SOLID design principles for better maintainability and scalability.

---

## **Features**

- Convert files to UTF-8 encoding.
- Filter files by extensions, names, and directories.
- Modularized structure for better code organization.
- Output processed file content to a specified file.

---

## **Modules Overview**

### **1. `Application`**

The main entry point of the project. It orchestrates the file processing by configuring filters and invoking the processing logic.

#### Example Usage:

```python
if __name__ == "__main__":
    Application.run()
```

---

### **2. `FileFilter`**

Handles filtering logic for files and directories.

#### Features:
- Filter files by extensions.
- Exclude specific file names.
- Exclude specific directories.

#### Example:

```python
file_filter = FileFilter(
    file_extensions=['conf'],
    exclude_extensions=['.md', '.gitignore', '.swp'],
    exclude_file_names=[],
    exclude_directories=['.git', '.idea', 'test', 'js']
)
```

---

### **3. `FileProcessor`**

Processes files based on the filters and writes the output to a specified file.

#### Features:
- Walks through the directory structure.
- Converts files to UTF-8 encoding.
- Writes file metadata and content to the output file.

#### Example:

```python
processor = FileProcessor(source_directory, output_file, file_filter)
processor.process_files()
```

---

### **4. `FileConverter`**

Converts files to UTF-8 encoding to ensure compatibility.

#### Example:

```python
FileConverter.convert_to_utf8(file_path)
```

---

## **Configuration**

The project uses a configuration file (`config.py`) to define the following parameters:
- **`source_directory`**: Directory containing the files to be processed.
- **`output_file`**: File where the processed content will be saved.
- **`file_extensions`**: List of file extensions to include.
- **`exclude_extensions`**: List of file extensions to exclude.
- **`exclude_directories`**: List of directories to exclude.
- **`exclude_file_names`**: List of specific file names to exclude.

#### Example Configuration:

```python
source_directory = "c:\\Users\\gomes\\Downloads\\123\\apache2"
output_file = "output/apache.txt"
file_extensions = ['conf']
exclude_extensions = ['.md', '.gitignore', '.swp']
exclude_directories = ['.git', '.idea', 'test', 'js']
exclude_file_names = []
```

---

## **How to Run**

- Clone the repository.
- Update the configuration in `config.py` as per your requirements.
- Run the project:

```bash
python main.py
```

---

## **Output**

The processed content will be saved in the file specified in the `output_file` configuration. The output includes:
- File metadata (name and path).
- File content.

---

## **Example Output**

```plaintext
----------------------------------------
Arquivo: example.conf
Caminho: c:\Users\gomes\Downloads\123\apache2\example.conf
========================================
<file content here>
----------------------------------------
Arquivo: another.conf
Caminho: c:\Users\gomes\Downloads\123\apache2\another.conf
========================================
<file content here>
```

---

## **Release Notes**

### **Version 1.1.0**
- Refactored `Application` to load configurations from `config.py`.
- Updated `output_file` to include a directory path for better organization.
- Added support for excluding specific file names.

---

## **Future Enhancements**

- Add support for parallel processing to improve performance.
- Implement a logging mechanism for better debugging and monitoring.
- Add unit tests for all modules.

---

## **Contributors**

- Marcelo Renato Gomes

For any issues or feature requests, please open an issue in the repository.

