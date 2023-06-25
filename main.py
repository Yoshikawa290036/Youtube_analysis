from get_chat_data_by_pytchat import get_chat_data
from get_chat_speed import get_chat_speed_by_file
from extract_video_id import extract_video_id
from getURL import getURL
from make import make
from analysis_RANK import analysis
import os
import sys
import threading


speed_RANK_files = []


def getdata(video_id, outdir):
    # video_id, video_data = extract_video_id(url)
    fname = get_chat_data(video_id, outdir)
    RANK_fname = get_chat_speed_by_file(fname)
    speed_RANK_files.append(RANK_fname)


def isGet(datestr, sdate, edate):
    date = int(datestr)
    # print('date : ', date)
    return True if (sdate <= date and date <= edate) else False


def main(root, gen, c_name, stime, etime):
    print('From '+str(stime)+' to '+str(etime))
    dirname = root+'/'+gen+'_'+c_name
    with open(dirname+'/URL_list.tsv', 'r', encoding='utf-16') as f:
        lines = f.readlines()
    for line in lines:
        if len(line) < 3:
            continue
        print('------------------------------------------------')
        print('myID          : ', gen)
        print('Channel Name  : ', c_name)
        URL = line.strip().split()[0]
        video_id, video_date = extract_video_id(URL)
        if isGet(video_date, stime, etime):
            print('GET DATA !!!')
            getdata(video_id, dirname+'/')
        print()
    


if __name__ == '__main__':
    be = sys.argv[1]
    en = sys.argv[2]
    gen = sys.argv[3]
    c_name = sys.argv[4]
    root = be+"-"+en
    main(root, gen, c_name, int(be), int(en))
    print("FINISHED !!!!!!!!")
    print()
