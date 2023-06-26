# https://qiita.com/MultiplicationSign/items/96c9118f9cfa55000aa3

from yt_dlp import YoutubeDL


def download(url, dirname, start_time, end_time):
    print('Download URL  :',url)

    def set_download_ranges(info_dict, self):
        duration_opt = [{
            'start_time': start_time,
            'end_time': end_time
        }]
        return duration_opt

    ydl_opts = {
        'outtmpl': dirname+'%(id)s'+'.mp4',
        'format': 'best',
        'download_ranges': set_download_ranges
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    print()

if __name__ == '__main__':
    dir = '20230617-20230623/videos/'
    url = 'https://youtube.com/watch?v=CiVGCuVuvH8'

    download(url, dir, 1762-60, 1762+60)
