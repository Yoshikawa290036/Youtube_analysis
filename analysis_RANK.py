from get_chat_speed import dataout
import sys
from download import download


def analysis(RANK_file_list, fname):
    datas = []
    for rank_file in RANK_file_list:
        rank_file = rank_file.strip()
        print(rank_file)
        if len(rank_file) < 3:
            continue
        url = get_url_by_fname(rank_file)
        with open(rank_file, 'r', encoding='utf-16') as f:
            line = f.readline()
        lc = line.strip().split()
        datas.append([url, lc[0], lc[1], lc[2], float(lc[3]), rank_file])
    sorted_datas = sorted(datas, key=lambda x: x[4], reverse=True)
    outdatas = []
    for line in sorted_datas:
        sline = f"{line[0]}\t{line[1]}\t{line[2]}\t{line[3]}\t{line[4]}\t{line[5]}"+"\n"
        outdatas.append(sline)
    dataout(fname, outdatas)
    return sorted_datas


def get_url_by_fname(fname):
    fff = fname.strip().split('/')
    key = fff[len(fff)-1].replace('_speed_RANK.tsv', '')
    return f'https://youtube.com/watch?v={key}'


if __name__ == '__main__':
    listfname = sys.argv[1]
    ofname = listfname.replace('_list', '')
    with open(listfname, 'r') as f:
        fnames = f.readlines()
    # print(fnames)
    ranklist = analysis(fnames, ofname)

    dirname = listfname.replace('/RANK_list.tsv', '/videos/')
    for i in range(min(len(ranklist), 10)):
        if len(ranklist[i]) < 3:
            continue
        dir = f"{dirname}{i+1}-"
        URL = ranklist[i][0]
        TIME = int(ranklist[i][1])
        download(URL, dir, TIME-60, TIME+60)
