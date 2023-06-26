from yt_dlp import YoutubeDL


def extract_video_id(url):
    with YoutubeDL({'ignoreerrors':True}) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        # print(info_dict.get("live_status"))
        id = info_dict.get("id", None)
        date = info_dict.get("upload_date")
        print('ID           : ', id)
        print('Upload_DATE  : ', date)
        return [id, date]


if __name__ == '__main__':
    # extract_video_id('https://www.youtube.com/watch?v=G_ulCc3zizw&t=3s')
    # extract_video_id('https://www.youtube.com/watch?v=7OCcgg0sYjY')
    extract_video_id('https://www.youtube.com/watch?v=9v1kqGF-rvU')
