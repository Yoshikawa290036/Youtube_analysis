from yt_dlp import YoutubeDL


def download(url, dirname):
    print('Download URL  :',url)
    ydl_opts = {
        'outtmpl': dirname+'%(id)s'+'.mp4',
        'format': 'best'
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print()

if __name__ == '__main__':
    dir = '20230617-20230623/videos/'
    url = 'https://www.youtube.com/watch?v=AkTLxzKcrfk'

    download(url, dir)
