from get_chat_speed import dataout
import sys
from download import download
from liver_data_class import Conbined_Liver_data
import os


def analysis_RANK(RANK_file_list, URL_list, titles, stream_num, fname):
    datas = []
    for i in range(stream_num):
        rank_file = RANK_file_list[i]
        title = titles[i]
        url = URL_list[i]
        print(rank_file, url)
        with open(rank_file, 'r', encoding='utf-16') as f:
            line = f.readline()
        if len(line) < 2:
            continue
        lc = line.strip().split(',')
        datas.append([url, lc[0], lc[1], lc[2], float(lc[3]), title, rank_file])
    sorted_datas = sorted(datas, key=lambda x: x[4], reverse=True)
    outdatas = []
    for line in sorted_datas:
        sline = f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]},{line[5]},{line[6]}"+"\n"
        outdatas.append(sline)
    dataout(fname, outdatas)
    return sorted_datas


def get_live_url(id, start):
    start = start-10
    # https://www.youtube.com/live/CiVGCuVuvH8?feature=share&t=1019
    return f"https://www.youtube.com/watch?v={id}&t={start}s"


def make_ranking(livers: Conbined_Liver_data):
    ranklist = analysis_RANK(livers.chat_speed_rank_files, livers.urls,
                             livers.titles, livers.stream_num, 
                             livers.ranking_file_name)
    top10_fname = os.path.join(f"{livers.start_date}-{livers.end_date}","Top10_RANK.csv")
    print(top10_fname)
    speed_top10 = []
    for i in range(min(len(ranklist), 10)):
        video_head = os.path.join(livers.video_directory, f"{i+1}-")
        thumbnail_head = os.path.join(livers.thumbnail_directory, f"{i+1}-")
        URL = ranklist[i][0]
        ID = URL.replace('https://www.youtube.com/watch?v=', '')
        TIME = int(ranklist[i][1])
        thumbnail_fname = os.path.join(f"{livers.start_date}-{livers.end_date}","thumbnails",f"{i+1}-{ID}.webp")
        start = TIME-45
        end = TIME+20
        speed_top10.append(f"{get_live_url(ID, start)}  ,{ranklist[i][4]},{thumbnail_fname},{ranklist[i][5]}\n")
        download(URL, video_head, thumbnail_head, start, end)
    dataout(os.path.join(f"{livers.start_date}-{livers.end_date}","Top10_RANK.csv"), speed_top10)
    # dataout(top10_fname, speed_top10)


def get_url_by_fname(fname):
    fff = fname.strip().split('/')
    key = fff[len(fff)-1].replace('_speed_RANK.csv', '')
    return f'https://youtube.com/watch?v={key}'


if __name__ == '__main__':
    listfname = sys.argv[1]
    ofname = listfname.replace('_list', '')
    with open(listfname, 'r') as f:
        fnames = f.readlines()
    # print(fnames)
    ranklist = analysis(fnames, ofname)

    dirname = listfname.replace('/RANK_list.csv', '/videos/')
    for i in range(min(len(ranklist), 10)):
        if len(ranklist[i]) < 3:
            continue
        dir = f"{dirname}{i+1}-"
        URL = ranklist[i][0]
        TIME = int(ranklist[i][1])
        download(URL, dir, TIME-45, TIME+20)
