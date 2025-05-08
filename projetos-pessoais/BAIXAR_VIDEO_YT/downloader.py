from pytubefix import YouTube
from pytubefix.cli import on_progress
import pandas as pd
def link():
    txt = "BAIXAR VIDEOS DO YOUTUBE"
    print("-"*len(txt))
    print(txt)
    print("-"*len(txt))
    url = str(input("Digite a url do video:"))
    return url

def download(url):
    video = YouTube(url , on_progress_callback=on_progress)
    print(f"titulo do video: {video.title}")
    video_dwn = video.streams.get_highest_resolution()
    video_dwn.download(output_path="C:/Users/yurib/Documents/python/BAIXAR_VIDEO_YT/videos_baixados")
    print("Link da pasta: ")

def legenda(url):
    yt = YouTube(url)
    lingua = str(yt.captions)
    legenda = yt.captions[lingua[2:6]]
    texto = legenda.generate_txt_captions()
    arquivo = open("legendas.txt" , "a")
    arquivo.write(texto)
    arquivo.close()


if __name__ == "__main__":
    x = link()
    download(x)
    legenda(x)
