import os
from getURL import getURL
from concurrent.futures import ThreadPoolExecutor


def make():
    with open('go.sh', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    sdates = lines[0].strip().split("=")[1]
    edates = lines[1].strip().split("=")[1]
    root = sdates+'-'+edates
    os.makedirs(root, exist_ok=True)


    with ThreadPoolExecutor() as executor:
        for i in range(40):
            lc = lines[i].strip().split()
            if len(lc) < 4:
                continue
            dirname = f"{root}/{lc[4]}_{lc[5]}"
            print(f"{lc[4]}\t{lc[5]}")
            os.makedirs(dirname, exist_ok=True)
            executor.submit(getURL, lc[5], dirname+'/URL_list')


if __name__ == '__main__':
    make()
