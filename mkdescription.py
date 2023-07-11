import os
import pprint


def ymd(date: str):
    yea = int(date[:4])
    mon = int(date[4:6])
    day = int(date[6:8])
    return f"{yea}年{mon}月{day}日"


def Make_title(start_date: str, end_date: str):
    sdatejp = ymd(start_date)
    edatejp = ymd(end_date)
    with open(os.path.join("format", "Video_title.txt"),
              "r", encoding='utf-16') as f:
        tit_lines = f.readlines()
    for i in range(len(tit_lines)):
        tit_lines[i] = tit_lines[i].replace("{{{{sdate}}}}", sdatejp)
        tit_lines[i] = tit_lines[i].replace("{{{{edate}}}}", edatejp)
    with open(os.path.join(f"{start_date}-{end_date}", "Video_title.txt"),
              "w", encoding="utf-16") as f:
        f.writelines(tit_lines)
    print("Create ", os.path.join(f"{start_date}-{end_date}", "Video_title.txt"))


def Make_description(urls, titles, start_date, end_date):
    sdate_jp = ymd(start_date)
    edate_jp = ymd(end_date)
    with open(os.path.join("format", "Video_description.txt"),
              "r", encoding='utf-16') as f:
        des_form = f.readlines()
    for i in range(len(des_form)):
        if "{{{{日付}}}}" in des_form[i]:
            des_form[i] = des_form[i].replace("{{{{日付}}}}", f"{sdate_jp}～{edate_jp}")
            break

    for i in range(10):
        key_url = "{{{{" + str(i+1) + "th_URL}}}}"
        key_title = "{{{{" + str(i+1) + "th_TITLE}}}}"

        flag1, flag2 = False, False
        for j in range(len(des_form)):
            if key_url in des_form[j]:
                des_form[j] = des_form[j].replace(key_url, urls[i])
                flag1 = True
            if key_title in des_form[j]:
                des_form[j] = des_form[j].replace(key_title, titles[i])
                flag2 = True
            if flag1 and flag2:
                break
    with open(os.path.join(f"{start_date}-{end_date}", "Video_description.txt"),
              "w", encoding="utf-16") as f:
        f.writelines(des_form)
    print("Create ", os.path.join(f"{start_date}-{end_date}", "Video_description.txt"))

def go_Make_description(top10_rank_fname: str, sdate: str, edate: str):
    with open(top10_rank_fname, "r", encoding="utf-16") as f:
        lines = f.readlines()
    urls = []
    titles = []
    for i in range(10):
        lc = lines[i].strip().split(':,:')
        urls.append(lc[0])
        titles.append(lc[3])
    Make_description(urls, titles, sdate, edate)
    Make_title(sdate, edate)


if __name__ == '__main__':
    urls = [
        "https://www.youtube.com/watch?v=7mfrD0trqb8&t=2088s",
        "https://www.youtube.com/watch?v=GX6ijfo6iJA&t=6392s",
        "https://www.youtube.com/watch?v=ge9kpGBgnBA&t=252s ",
        "https://www.youtube.com/watch?v=4j2vS3Lt4ag&t=2664s",
        "https://www.youtube.com/watch?v=mpX1QWpYU0M&t=6044s",
        "https://www.youtube.com/watch?v=cnV04aXJqB0&t=3120s",
        "https://www.youtube.com/watch?v=sAOVlEPsQyU&t=7965s",
        "https://www.youtube.com/watch?v=QJtYqxTm2os&t=1495s",
        "https://www.youtube.com/watch?v=hd5Kj4WA-r8&t=4051s",
        "https://www.youtube.com/watch?v=Kx5frPW1Jog&t=2573s"
    ]
    titles = [
        "あああ7mfrD0trqb8&t=2088s",
        "あああGX6ijfo6iJA&t=6392s",
        "あああge9kpGBgnBA&t=252s ",
        "あああ4j2vS3Lt4ag&t=2664s",
        "あああmpX1QWpYU0M&t=6044s",
        "あああcnV04aXJqB0&t=3120s",
        "あああsAOVlEPsQyU&t=7965s",
        "あああQJtYqxTm2os&t=1495s",
        "あああhd5Kj4WA-r8&t=4051s",
        "あああKx5frPW1Jog&t=2573s"
    ]
    Make_description(urls, titles, "20230717", "20230623")
