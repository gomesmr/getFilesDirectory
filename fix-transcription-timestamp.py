import re

def processa_arquivo(entrada, saida):
    # Abre o arquivo de entrada e lê todas as linhas
    with open(entrada, 'r', encoding='utf-8') as file:
        linhas = file.readlines()

    novas_linhas = []
    # Expressão regular para identificar linhas que contenham somente um horário (por exemplo, 34:05)
    padrao = re.compile(r'^\d{1,2}:\d{2}$')
    i = 0
    while i < len(linhas):
        linha_atual = linhas[i].rstrip("\n")
        # Se a linha atual for um horário conforme o padrão
        if padrao.match(linha_atual):
            # Verifica se existe uma próxima linha para realizar a junção
            if i + 1 < len(linhas):
                proxima_linha = linhas[i+1].rstrip("\n")
                # Junta o horário com a linha seguinte usando " - "
                nova_linha = f"{linha_atual} - {proxima_linha}"
                novas_linhas.append(nova_linha)
                i += 2  # Pula a próxima linha, pois já foi processada
                continue
        # Se a linha não corresponder ao padrão, adiciona normalmente
        novas_linhas.append(linha_atual)
        i += 1

    # Escreve o resultado no arquivo de saída
    with open(saida, 'w', encoding='utf-8') as file:
        for linha in novas_linhas:
            file.write(linha + "\n")

if __name__ == "__main__":
    arquivo_entrada = r"g:\Meu Drive\iCBT\library\Saúde da Mente\Aula 2 Identificando os sintomas da depressão - transcrição.md"   # Nome do arquivo de entrada
    arquivo_saida = "saida.txt"       # Nome do arquivo de saída
    processa_arquivo(arquivo_entrada, arquivo_saida)
