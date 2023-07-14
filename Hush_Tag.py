c_names = [
    "@TokinoSora",
    "@Robocosan",
    "@AZKi",
    "@SakuraMiko",
    "@HoshimachiSuisei",
    "@YozoraMel",
    "@AkiRosenthal",
    "@AkaiHaato",
    "@ShirakamiFubuki",
    "@NatsuiroMatsuri",
    "@MinatoAqua",
    "@MurasakiShion",
    "@NakiriAyame",
    "@YuzukiChoco",
    "@OozoraSubaru",
    "@usadapekora",
    "@ShiranuiFlare",
    "@ShiroganeNoel",
    "@HoushouMarine",
    "@AmaneKanata",
    "@TsunomakiWatame",
    "@TokoyamiTowa",
    "@HimemoriLuna",
    "@YukihanaLamy",
    "@MomosuzuNene",
    "@ShishiroBotan",
    "@OmaruPolka",
    "@LaplusDarknesss",
    "@TakaneLui",
    "@HakuiKoyori",
    "@SakamataChloe",
    "@kazamairoha",
    "@OokamiMio",
    "@NekomataOkayu",
    "@InugamiKorone"
]

JP_names = [
    "ときのそら",
    "ロボ子さん",
    "AZKi",
    "さくらみこ",
    "星街すいせい",
    "夜空メル",
    "アキロゼ",
    "赤井はあと",
    "白上フブキ",
    "夏色まつり",
    "湊あくあ",
    "紫咲シオン",
    "百鬼あやめ",
    "癒月ちょこ",
    "大空スバル",
    "兎田ぺこら",
    "不知火フレア",
    "白銀ノエル",
    "宝鐘マリン",
    "天音かなた",
    "角巻わため",
    "常闇トワ",
    "姫森ルーナ",
    "雪花ラミィ",
    "桃鈴ねね",
    "獅白ぼたん",
    "尾丸ポルカ",
    "ラプラスダークネス",
    "鷹嶺ルイ",
    "博衣こより",
    "沙花叉クロヱ",
    "風真いろは",
    "大神ミオ",
    "猫又おかゆ",
    "戌神ころね"
]


def changeName(c_name):
    return JP_names[c_names.index(c_name)]


def mk_hushtag(c_names: list, fname: str):
    used = []
    top10_list = []
    hush_str = ''
    for cname in c_names:
        if cname in used:
            continue
        used.append(cname)
        JPname = changeName(cname)
        hush_str += f"#{JPname} "
        top10_list.append(f"{JPname}\n")

    with open(fname, "w", encoding="utf-16") as f:
        f.writelines(top10_list)

    print("Create ", fname)
    return hush_str.strip()


if __name__ == '__main__':
    print(len(c_names), len(JP_names))
