# https://ai-study.hatenablog.com/entry/2019/07/10/210000
from liver_data_class import Liver_data
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from yt_dlp import YoutubeDL
import os
import time

def get_stream_date(url):
    with YoutubeDL({'ignoreerrors': True}) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        date = info_dict.get("upload_date")
        return int(date)


def get_page_source(Liver_data):
    options = Options()
    options.add_argument('--disable-logging')
    options.add_argument('--log-level=3')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get(Liver_data.channel_streams_url)
    time.sleep(3)
    return driver.page_source


def parse_video_title_and_url(Liver_data : Liver_data, current_html):
    soup = BeautifulSoup(current_html, 'html.parser')
    for i in soup.find_all("a"):
        # print(i)
        title = (i.get("title"))
        url = (i.get("href"))
        aria_label = (i.get("aria-label"))
        if title is None:
            continue
        if url is None:
            continue
        if aria_label is None:
            continue
        # print(title)
        # print(url)
        # print(aria_label)
        if "/watch?v=" in url and 'に配信済み' in aria_label:
            stream_url = Liver_data.youtube_url+url
            stream_id = url.replace("/watch?v=", "")
            date = get_stream_date(stream_url)
            if Liver_data.start_date <= date and date <= Liver_data.end_date:
                Liver_data.stream_url.append(stream_url)
                Liver_data.stream_id.append(stream_id)
                Liver_data.stream_title.append(title)
                Liver_data.stream_date.append(date)
                outfile = os.path.join(Liver_data.output_dir, stream_id)
                Liver_data.chat_data_file.append(f"{outfile}.tsv")
                Liver_data.chat_speed_file.append(f"{outfile}_speed.tsv")
                Liver_data.chat_speed_rank_file.append(f"{outfile}_speed_RANK.tsv")
                Liver_data.stream_num += 1


def youtube_scrape(Liver_data: Liver_data):
    html = get_page_source(Liver_data)
    parse_video_title_and_url(Liver_data, html)
    Liver_data.output_url_list()


if __name__ == '__main__':
    test = Liver_data(c_name='@OozoraSubaru', generation='2-15', start_date='20230620', end_date='20230624')
    youtube_scrape(test)
