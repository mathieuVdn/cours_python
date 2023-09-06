from pytube import YouTube
import ffmpeg
import os
import app

BG_COLOR = "#e8e2e9"
BASE_YOUTUBE_URL = "https://www.youtube.com"


def on_download_progress_bar(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = round(int(bytes_downloaded * 100 / stream.filesize))
    app.progress_bar_download["value"] = percent


def download_video(url):
    if url[:len(BASE_YOUTUBE_URL)] != BASE_YOUTUBE_URL or not url.lower().startswith(BASE_YOUTUBE_URL):
        print("ERREUR : Vous devez rentrer une URL de vidéo Youtube valide")
        return

    youtube_video = YouTube(url)
    youtube_video.register_on_progress_callback(on_download_progress_bar)

    video_stream = youtube_video.streams.filter(progressive=False, file_extension='mp4', type="video").order_by(
        'resolution').desc().first()
    audio_stream = youtube_video.streams.filter(progressive=False, file_extension='mp4', type="audio").order_by(
        'abr').desc().first()

    if not video_stream or not audio_stream:
        print("ERREUR : Aucun flux vidéo ou audio disponible pour cette vidéo.")
        return

    print(f"Téléchargement {youtube_video.title}...")
    video_stream.download("video")
    audio_stream.download("audio")

    audio_filename = os.path.join("audio", video_stream.default_filename)
    video_filename = os.path.join("video", video_stream.default_filename)
    output_filename = video_stream.default_filename

    ffmpeg.output(ffmpeg.input(audio_filename), ffmpeg.input(video_filename), output_filename, vcodec="copy",
                  acodec="copy", loglevel="quiet").run(overwrite_output=True)
    print("OK")

    os.remove(audio_filename)
    os.remove(video_filename)
    os.rmdir("audio")
    os.rmdir("video")
