import pytchat
import time
from liver_data_class import Liver_data

def get_chat_data(liver : Liver_data):
    txt_in = []
    livechat = pytchat.create(video_id=liver.stream_id[liver.pos])
    # cnt=0
    while livechat.is_alive():
        chatdata = livechat.get()
        # print(type(chatdata))
        if type(chatdata) is list:
            # print('CANNOT GET DATA.')
            # print('file count : ',cnt)
            break
        # print(len(chatdata.items))
        # cnt += len(chatdata.items)
        # print(type(chatdata))
        # print(len(chatdata.items))
        for c in chatdata.items:
            # print(f"{c.datetime} {c.elapsedTime} {c.message} {c.amountString}")
            # txt_in.append(f'{c.elapsedTime},{c.type},{c.message},{c.author.name},{c.amountString},{c.currency},{c.amountValue},{c.bgColor}\n')
            txt_in.append('{},{},{},{},{},{},{},{}\n'.format(c.elapsedTime,
                                                                    c.type,
                                                                    c.message,
                                                                    c.author.name,
                                                                    c.amountString,
                                                                    c.currency,
                                                                    c.amountValue,
                                                                    c.bgColor))
        # time.sleep(3)
    fname = liver.chat_data_file[liver.pos]
    with open(fname, 'w', encoding='utf-16', newline='\n') as f:
        f.writelines(txt_in)
    print('Create chat data file  : ', fname)
