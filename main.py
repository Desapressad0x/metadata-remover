import os
import shutil
from PIL import Image
import taglib
import sys

def clear_vid(arq):
    modd = arq.split('.')
    modd = f"{modd[0]}-new.{modd[1]}"
    
    shutil.copyfile(arq, modd)
    v = taglib.File(modd)
    keys = v.tags.keys()
    for tag in list(keys):
        del v.tags[tag]
    v.save()
    
    print(f'[!] The file {arq} has been cleaned and saved as {modd}')
    sys.exit()
    
def clear_img(arq):
    modd = arq.split('.')
    modd = f"{modd[0]}-new.{modd[1]}"
   
    imagem = Image.open(arq)
    dd = list(imagem.getdata())
    imagem2 = Image.new(imagem.mode, imagem.size)
    imagem2.putdata(dd)
    imagem2.save(modd)

    print(f'[!] The file {arq} has been cleaned and saved as {modd}')
    sys.exit()

def arguments():
    imgs = ["jpeg", "jpg"]
    videos = ["mp4"]
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} [file name]")
        sys.exit()
    arq = sys.argv[1]
    if os.path.exists(arq):
        if arq.split('.')[1] in imgs:
            clear_img(arq)
        elif arq.split('.')[1] in videos:
            clear_vid(arq)
        else:
            print('[X] Unknown file format.')
            sys.exit()
    else:
        print('[X] The file was not found.')
        sys.exit()
        
if __name__ == "__main__":
    arguments()
