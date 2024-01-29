# Importamos librerias
import pytube
import whisper

# Variable para el video de Youtube
youtubeVideoId = "https://www.youtube.com/watch?v=iBy-7ESrXlI"

# Cargamos el modelo de whisper
model = whisper.load_model('small')

# Recuperamos el video de Yotube con pytube
youtubeVideo = pytube.YouTube(youtubeVideoId)
# Lo transformamos en audio
audio = youtubeVideo.streams.get_audio_only()
# Descargamos el archivo de audio
audio.download(filename='tmp.mp4')

# Guardamos los resultados del modelo
result = model.transcribe('tmp.mp4')

print(result["text"])