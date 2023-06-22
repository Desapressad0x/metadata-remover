import os
import shutil
from PIL import Image
import taglib
import sys

def limpar_video(caminho_arquivo) -> None:
    nome_arquivo, extensao_arquivo = os.path.splitext(caminho_arquivo)
    novo_nome_arquivo = f"{nome_arquivo}-cleaned{extensao_arquivo}"
    
    shutil.copyfile(caminho_arquivo, novo_nome_arquivo)
    arquivo = taglib.File(novo_nome_arquivo)
    tags = list(arquivo.tags.keys())
    for tag in tags:
        del arquivo.tags[tag]
    arquivo.save()
    
    print(f'[!] The file {caminho_arquivo} has been cleaned and saved as {novo_nome_arquivo}.')
    sys.exit()

def limpar_imagem(caminho_arquivo) -> None:
    nome_arquivo, extensao_arquivo = os.path.splitext(caminho_arquivo)
    novo_nome_arquivo = f"{nome_arquivo}-cleaned{extensao_arquivo}"
   
    imagem = Image.open(caminho_arquivo)
    pixels = list(imagem.getdata())
    imagem2 = Image.new(imagem.mode, imagem.size)
    imagem2.putdata(pixels)
    imagem2.save(novo_nome_arquivo)

    print(f'[!] The file {caminho_arquivo} has been cleaned and saved as {novo_nome_arquivo}.')
    sys.exit()

def argumentos() -> None:
    formatos_imagem = ["jpeg", "jpg"]
    formatos_video = ["mp4"]
    if len(sys.argv) != 2:
        print(f"Use: {sys.argv[0]} [name of the file]")
        sys.exit()
    caminho_arquivo = sys.argv[1]
    if os.path.exists(caminho_arquivo):
        extensao_arquivo = caminho_arquivo.split('.')[-1]
        if extensao_arquivo in formatos_imagem:
            limpar_imagem(caminho_arquivo)
        elif extensao_arquivo in formatos_video:
            limpar_video(caminho_arquivo)
        else:
            print('[X] Unknown file format.')
            sys.exit()
    else:
        print('[X] The file was not found.')
        sys.exit()
        
if __name__ == "__main__":
    argumentos()
