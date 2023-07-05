# https://qiita.com/xKxAxKx/items/2599006005098dc2e299

from PIL import ImageDraw, Image, ImageFont
import os
# from Bunsetu_split import bunsetsuWakachi
import sys
import io
import unicodedata

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-16')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-16')


def add_text_to_image(img, text, font_path, font_size, font_color, height, width, max_length=740):
    position = (width, height)
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(img)
    # if draw.textsize(text, font=font)[0] > max_length:
    #     while draw.textsize(text + '…', font=font)[0] > max_length:
    #         text = text[:-1]
    #     text = text + '…'

    draw.text(position, text, font_color, font=font)

    return img


def text_width_counter(c):
    j = unicodedata.east_asian_width(c)
    if 'F' == j:
        return 2
    elif 'H' == j:
        return 1
    elif 'W' == j:
        return 2
    elif 'Na' == j:
        return 1
    elif 'A' == j:
        return 2
    else:
        return 1


def rank_num2string(rank_num: int):
    if rank_num == 1:
        return "１位"
    if rank_num == 2:
        return "２位"
    if rank_num == 3:
        return "３位"
    if rank_num == 4:
        return "４位"
    if rank_num == 5:
        return "５位"
    if rank_num == 6:
        return "６位"
    if rank_num == 7:
        return "７位"
    if rank_num == 8:
        return "８位"
    if rank_num == 9:
        return "９位"
    if rank_num == 10:
        return "10位"


def make_transition(thumbnail_fname: str, rank_num: int, title: str, speed: float, save_fname: str):
    titles = ['']
    cnt = 0
    for c in title:
        cnt += text_width_counter(c)
        if cnt > 94:
            titles.append(c)
            cnt = text_width_counter(c)
        else:
            titles[len(titles)-1] += c

    BG = Image.new("RGB", (1920, 1080), (255, 255, 255))
    BG.putalpha(0)
    thumbnail_original = Image.open(thumbnail_fname).copy()
    w = int(1280*1.1)
    h = int(720*1.1)
    left_top = int(1980/2-w/2+20)
    thumbnail = thumbnail_original.resize(size=(w, h))
    BG.paste(thumbnail, (left_top, 0))
    # BG.save("sample.png")
    img = add_text_to_image(BG, rank_num2string(rank_num), "C:\WINDOWS\Fonts\HGRSGU.TTC", 120, (255, 242, 158), 50, 30, 2000)
    height = h+25
    for title in titles:
        img = add_text_to_image(img, title, "C:\WINDOWS\Fonts\HGRPP1.TTC", 40, (255, 255, 255), height, 10, 2000)
        height += 65
    img = add_text_to_image(img, "１秒で", "C:\WINDOWS\Fonts\HGRPP1.TTC", 50, (255, 255, 255), 1080-85, 350, 2000)
    img = add_text_to_image(img, f"{speed} コメント！！", "C:\WINDOWS\Fonts\HGRPP1.TTC", 120, (255, 255, 20), 1080-130, 580, 2000)
    img.save(save_fname)


def go_make_TR(top10_fname):
    with open(top10_fname, 'r', encoding='utf-16') as f:
        lines = f.readlines()
    for i in range(min(10, len(lines))):
        if len(lines[i]) < 3:
            continue
        lc = lines[i].strip().split(',')
        make_transition(lc[2], i+1, lc[3], float(lc[1]), lc[2].replace('.webp', '.png'))


if __name__ == '__main__':
    # go_make_TR("20230617-20230623\Top10_RANK.tsv")
    go_make_TR("20230624-20230630\Top10_RANK.csv")

    # title = "【歌枠】誕生日カウントダウン🎤一緒に誕生日を迎えるでござる～～！🎉【風真いろは/ホロライブ】"
    # # title_list = bunsetsuWakachi(title)
    # titles = []
    # cnt = 0
    # while len(title)/38 > 0:
    #     titles.append(title[0:38])
    #     title = title[38:]

    # # titles = ["【歌枠】誕生日カウントダウン🎤一緒に", "誕生日を迎えるでござる～～！🎉【風真いろは/ホロライブ】"]
    # # titles = ["【歌枠】誕生日カウントダウン🎤一緒に誕生日を迎えるでござる～～！🎉【風真いろは/ホロライブ】"]

    # make_transition("20230617-20230623/thumbnails/1-CiVGCuVuvH8.webp", 1, titles, 21.4)
    # # make_transition("20230617-20230623/thumbnails/1-CiVGCuVuvH8.webp", "風真いろは",[title], 2.2)
