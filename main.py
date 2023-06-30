from get_chat_data_by_pytchat import get_chat_data
from get_chat_speed import get_chat_speed
import sys
import io
import os
from liver_data_class import Liver_data
from scrape_stream_url import youtube_scrape


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', buffering=1)
sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', buffering=1)
sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', buffering=1)


def getdata(liver: Liver_data):
    # video_id, video_data = extract_video_id(url)
    get_chat_data(liver)
    get_chat_speed(liver)


def isGet(datestr, sdate, edate):
    date = int(datestr)
    # print('date : ', date)
    return True if (sdate <= date and date <= edate) else False


def main(liver: Liver_data):
    print('From '+str(liver.start_date)+' to '+str(liver.end_date))
    youtube_scrape(liver)
    print("Start getting chat data")
    for i in range(liver.stream_num):
        print('------------------------------------------------')
        print(f'  {i+1} / {liver.stream_num}')
        print('Stream URL    : ', liver.stream_url[i])
        print('Stream Date   : ', liver.stream_date[i])
        # print('Stream Title  : ', liver.stream_title[i])
        print('Stream ID     : ', liver.stream_id[i])
        liver.pos = i
        getdata(liver)
        print()
    liver.save_data()


if __name__ == '__main__':
    be = sys.argv[1]
    en = sys.argv[2]
    gen = sys.argv[3]
    c_name = sys.argv[4]
    liver = Liver_data(c_name, gen, be, en)
    main(liver)
    print("FINISHED !!!!!!!!")
