import os
import shutil

def organizar_arquivos_na_pasta_do_script():
    # Obtém o caminho da pasta onde o script está localizado
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    
    # Lista todos os arquivos na pasta atual
    for nome_arquivo in os.listdir(pasta_atual):
        caminho_arquivo = os.path.join(pasta_atual, nome_arquivo)
        
        # Verifica se é um arquivo (ignora diretórios)
        if os.path.isfile(caminho_arquivo) and nome_arquivo != os.path.basename(__file__):
            # Obtém a extensão do arquivo
            _, extensao = os.path.splitext(nome_arquivo)
            # Remove o ponto da extensão e converte para minúsculas
            extensao = extensao[1:].lower()
            if not extensao:
                extensao = 'sem_extensao'

            # Cria o caminho da pasta da extensão
            pasta_extensao = os.path.join(pasta_atual, extensao)
            # Cria a pasta se ela não existir
            if not os.path.exists(pasta_extensao):
                os.makedirs(pasta_extensao)
            
            # Move o arquivo para a pasta correspondente
            caminho_destino = os.path.join(pasta_extensao, nome_arquivo)
            # Verifica se o arquivo já existe no destino
            contador = 1
            nome_base, ext = os.path.splitext(nome_arquivo)
            while os.path.exists(caminho_destino):
                novo_nome_arquivo = f"{nome_base}_{contador}{ext}"
                caminho_destino = os.path.join(pasta_extensao, novo_nome_arquivo)
                contador += 1
            shutil.move(caminho_arquivo, caminho_destino)
            print(f"Movido: {caminho_arquivo} -> {caminho_destino}")

if __name__ == "__main__":
    organizar_arquivos_na_pasta_do_script()
