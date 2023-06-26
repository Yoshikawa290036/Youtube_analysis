import pytchat
import time


def get_chat_data(video_id, outdir):
    txt_in = []
    livechat = pytchat.create(video_id=video_id)
    cnt=0
    while livechat.is_alive():
        chatdata = livechat.get()
        # print(type(chatdata))
        if type(chatdata) is list:
            print('CANNOT GET DATA.')
            print('file count : ',cnt)
            break
        # print(len(chatdata.items))
        cnt += len(chatdata.items)
        # print(type(chatdata))
        # print(len(chatdata.items))
        for c in chatdata.items:
            # print(f"{c.datetime} {c.elapsedTime} {c.message} {c.amountString}")
            # txt_in.append(f'{c.elapsedTime}\t{c.type}\t{c.message}\t{c.author.name}\t{c.amountString}\t{c.currency}\t{c.amountValue}\t{c.bgColor}\n')
            txt_in.append('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(c.elapsedTime, c.type, c.message, c.author.name, c.amountString, c.currency, c.amountValue, c.bgColor))
        # time.sleep(3)
    fname = outdir + video_id + '.tsv'
    with open(fname, 'w', encoding='utf-16', newline='\n') as f:
        f.writelines(txt_in)
    print('Create chat data file  : ', fname)
    return fname
