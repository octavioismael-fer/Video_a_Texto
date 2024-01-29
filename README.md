# YouTube Video to Text Converter

## Descripción del Proyecto

Este proyecto permite convertir el audio de videos de YouTube a texto de manera sencilla. Utiliza las bibliotecas Pytube, Whisper y FFmpeg para lograr una transcripción automática eficiente.

## Requisitos

- Python 3.9.18
- [Anaconda](https://www.anaconda.com/) (para crear el entorno virtual)
- Librerías:
  - Pytube
  - Whisper
- FFmpeg

## Instalación

1. Crea un entorno virtual con Anaconda:
   ```
   conda create --name tu_entorno_virtual python=3.9.18
   conda activate tu_entorno_virtual
   ```

2. Instala las librerías necesarias:
   ```
   pip install pytube whisper
   ```
   
3. Instala FFmpeg:
   ```
   conda install -c conda-forge ffmpeg
   ```

## Uso

1. Ingresa el enlance del video de YouTube:
   ```
   youtubeVideoId = "https://www.youtube.com/la-ulr-del-video"
   ```

2. Ejecuta el script principal.
   ```
   python convertidor.py
   ```

3. ¡Obtén la transcripción del audio en cuestión de minutos!

## Notas

- Asegúrate de tener una conexión a Internet estable.
- Asegúrate de instalar las librerias y ffmpeg.
- Ajusta las configuraciones según sea necesario en el script principal.

¡Disfruta convirtiendo tus videos favoritos de YouTube a texto con facilidad!
