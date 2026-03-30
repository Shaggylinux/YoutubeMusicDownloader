import yt_dlp
import os

class Descargador:     
    @staticmethod
    def Downloader(MusicFolder="Downloads", MusicList="MusicList.txt"):
        if not os.path.exists(MusicFolder):
            os.makedirs(MusicFolder)
            print(f"Carpeta creada: {MusicFolder}")

        ydl_opts = {
            'format': 'bestaudio/best',
            'cookiefile': 'cookies.txt',
            'noplaylist': True,
            'outtmpl': os.path.join(MusicFolder, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192', 
            }]
        }

        if not os.path.exists(MusicList):
            with open(MusicList, "w") as f:
                f.write("")
            print(f"Archivo creado: {MusicList}. ¡Pega tus links ahí!")
        else:
            with open(MusicList, "r") as f:
                urls = [line.strip() for line in f if line.strip()]
                
                if not urls:
                    print("El archivo de lista está vacío.")
                    return

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    for url in urls:
                        try:
                            print(f"Descargando: {url}")
                            ydl.download([url])
                        except Exception as e:
                            print(f"Error con {url}: {e}")

Descargador.Downloader("MisRolas", "MusicList.txt")