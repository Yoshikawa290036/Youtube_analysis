import pytchat
from collections import defaultdict


def get_chat_speed_by_file(fname):
    print('Anarysis Chat Speed')
    timed = defaultdict(int)
    ofname = fname.replace('.tsv', '_speed.tsv')
    sprankname = fname.replace('.tsv', '_speed_RANK.tsv')
    with open(fname, 'r', encoding='utf-16') as f:
        lines = f.readlines()
    if len(lines) == 0:
        return 'None'
    mintime, maxtime = get_min_max_time(lines)
    # print(mintime, maxtime)
    for line in lines[:]:
        if len(line) < 3:
            continue
        lc = line.strip().split()
        timekey = time2int(lc[0])
        timed[timekey] += 1
        # print(lc[0], int2time(timekey), timekey)
    outdata = chat_speed_ave(mintime, maxtime, timed, 10)
    ranklist = analysis_speed(outdata)
    dataout(ofname, outdata)
    dataout(sprankname, ranklist)
    return sprankname


def time2int(str):
    isM = True if '-' in str else False
    nstr = str.replace('-', '') if isM else str

    strl = nstr.strip().split(':')
    sec = int(strl[len(strl)-1])
    min = int(strl[len(strl)-2])
    hou = int(strl[len(strl)-3]) if len(strl) >= 3 else 0

    # print(str, nstr, isM, hou, min, sec)
    timei = -(sec+(60*min)+(3600*hou)) if isM else (sec+(60*min)+(3600*hou))
    return timei


def int2time(timei):
    isM = True if timei < 0 else False
    abstimei = abs(timei)
    hou = abstimei//3600
    abstimei %= 3600
    min = abstimei//60
    sec = abstimei % 60
    timestr = '-' if isM else ''
    timestr += str(hou).zfill(2)+':'+str(min).zfill(2)+':'+str(sec).zfill(2)
    return timestr


def get_min_max_time(lines):
    lc = lines[0].strip().split()
    mintime = time2int(lc[0])

    for line in reversed(lines):
        if len(line) < 5:
            continue
        lc = line.strip().split()
        maxtime = time2int(lc[0])
        break
    return [mintime, maxtime]


def chat_speed_ave(mintime, maxtime, timedict, width):
    txtlist = [f"{str(mintime).zfill(5)}\t{int2time(mintime)}\t{timedict[mintime]}\t"]
    cntsum = [timedict[mintime]]
    pre = cntsum[0]
    for t in range(mintime+1, maxtime+1, 1):
        txtlist.append(f"{str(t).zfill(5)}\t{int2time(           t)}\t{timedict[t]}\t")
        Sum = timedict[t]+pre
        cntsum.append(Sum)
        pre = Sum
    for i in range(width):
        ave = (cntsum[i]/(i+1))
        txtlist[i] = txtlist[i]+f"{ave}\n"
    for i in range(width, len(cntsum)):
        ave = ((-cntsum[i-width+1]+cntsum[i])/width)
        txtlist[i] = txtlist[i]+f"{ave}\n"
    return txtlist


def analysis_speed(outdata):
    datalist = []
    for i in range(len(outdata)):
        if len(outdata[i]) < 4:
            continue
        lc = outdata[i].strip().split()
        datalist.append([lc[0], lc[1], lc[2], float(lc[3])])

    sored_data = sorted(datalist, key=lambda x: x[3], reverse=True)
    # for i in range(10):
    #     print(sored_data[i])
    i = 0
    output = [f"{sored_data[i][0]}\t{sored_data[i][1]}\t{sored_data[i][2]}\t{sored_data[i][3]}"+"\n"]
    visit = [int(sored_data[i][0])]
    cnt = 1
    i = 1
    while (cnt < 30):
        for v in visit:
            if abs(v-int(sored_data[i][0])) <= 5:
                break
        else:
            cnt += 1
            output.append(f"{sored_data[i][0]}\t{sored_data[i][1]}\t{sored_data[i][2]}\t{sored_data[i][3]}"+"\n")
            visit.append(int(sored_data[i][0]))
        i += 1
    return output


def dataout(fname, datalist):
    with open(fname, 'w', encoding='utf-16', newline='\n') as f:
        f.writelines(datalist)
    print('Create file  : ', fname)

# def dataout(mintime, maxtime, timedict, fname):
#     txtout = []
#     for t in range(mintime, maxtime+1, 1):
#         txtout.append(f"{str(t).zfill(5)}\t{int2time(t)}\t{timedict[t]}\n")
#     with open(fname, 'w', encoding='utf-16', newline='\n') as f:
#         f.writelines(txtout)
#     print('Create chat speed file  : ', fname)


def get_chat_speed(video_id):
    txt_in = []
    livechat = pytchat.LiveChat(video_id=video_id, processor=pytchat.SpeedCalculator(capacity=20))
    # livechat = pytchat.create(video_id=video_id)
    while livechat.is_alive():
        chatspeed = livechat.get()
        # print(type(chatspeed))
        print(chatspeed)
        # time.sleep(3)
    # with open(outdir + video_id + '_chatdata.csv', 'w', encoding='utf-16', newline='\n') as f:
    #     f.writelines(txt_in)


if __name__ == '__main__':
    get_chat_speed_by_file('data/AGE72oBfo0k.tsv')
