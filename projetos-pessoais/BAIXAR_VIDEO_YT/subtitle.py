from pytubefix import YouTube
from pytubefix.cli import on_progress

# url = str(input("Cole a Url aqui: "))

url = "https://www.youtube.com/watch?v=ZLfcZR0Bzzw"

yt = YouTube(url)

print(yt.captions)

lingua = str(yt.captions)

legenda = yt.captions[lingua[2:6]]
#texto = str(legenda.generate_srt_captions()) #RESUME DE PARTES EM PARTES


texto = legenda.generate_txt_captions()

print(texto)