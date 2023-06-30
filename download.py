# https://qiita.com/MultiplicationSign/items/96c9118f9cfa55000aa3

from yt_dlp import YoutubeDL
from moviepy.editor import *


def download(url, video_dir, thumbnal_dir, start_time, end_time):
    print('Download URL  :', url)
    id = url.replace('https://youtube.com/watch?v=', '')

    def set_download_ranges(info_dict, self):
        duration_opt = [{
            'start_time': start_time,
            'end_time': end_time
        }]
        return duration_opt

    ydl_video_opts = {
        'outtmpl': 'video.mp4',
        'format': 'bestvideo/best',
        'download_ranges': set_download_ranges
    }
    ydl_audio_opts = {
        'outtmpl': 'audio.mp3',
        'format': 'bestaudio/best',
        'download_ranges': set_download_ranges
    }
    ydl_thumbnail_opts = {
        'outtmpl': thumbnal_dir+'%(id)s',
        'format': 'best',
        'skip_download': True,
        'writethumbnail': True
    }

    with YoutubeDL(ydl_video_opts) as ydl:
        ydl.download([url])
    with YoutubeDL(ydl_audio_opts) as ydl:
        ydl.download([url])
    with YoutubeDL(ydl_thumbnail_opts) as ydl:
        ydl.download([url])

    videoclip = VideoFileClip("video.mp4")
    audioclip = AudioFileClip("audio.mp3")
    output_video = videoclip.set_audio(audioclip)
    output_video.write_videofile(video_dir + id + ".mp4")
    os.remove('video.mp4')
    os.remove('audio.mp3')
    print()


if __name__ == '__main__':
    dir1 = 'aaaaaa'
    dir2 = 'aaaaaa'
    url = 'https://youtube.com/watch?v=CiVGCuVuvH8'

    download(url, dir1, dir2, 1762-60, 1762+60)
