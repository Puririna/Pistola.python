#Estudo de caso, atividade 2
class ArquivoMidia:
    def tocar(self):
        print("Reproduzindo mídia genérica...")

class ArquivoAudio(ArquivoMidia):
    def tocar(self):
        print("Tocando áudio...")

class ArquivoVideo(ArquivoMidia):
    def tocar(self):
        print("Mostrando vídeo e tocando som...")


audio = ArquivoAudio()
video = ArquivoVideo()
midia = ArquivoMidia()

audio.tocar()   
video.tocar()   
midia.tocar()   
