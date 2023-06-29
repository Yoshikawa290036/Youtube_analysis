import os
from liver_data_class import Liver_data, Conbined_Liver_data
import pickle
import sys
import io
from analysis_RANK import make_ranking

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def read_go():
    with open("go.bat", "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if "be=" in line:
            lc = line.strip().split()
            bestr = lc[1].replace("be=", "")
            break
    for line in lines:
        if "en=" in line:
            lc = line.strip().split()
            enstr = lc[1].replace("en=", "")
            break
    gens = []
    c_names = []
    for line in lines:
        if "main.py" not in line:
            continue
        lc = line.strip().split()
        main0 = lc.index("main.py")
        gens.append(lc[main0+3])
        c_names.append(lc[main0+4])

    # print(bestr, enstr)
    # print(gens, c_names)
    return [bestr, enstr, gens, c_names]


def read_Liver_data_class(be, en, gens, c_names):
    root = f"{be}-{en}"
    pickle_file = "Liver_data.pickle"
    livers = []
    for i in range(len(gens)):
        direc = f"{gens[i]}_{c_names[i]}"
        fname = os.path.join(root, direc, pickle_file)
        with open(fname, 'rb') as f:
            liver = pickle.load(f)
        livers.append(liver)
    return livers


def main():
    be, en, gens, c_names = read_go()
    livers_list = read_Liver_data_class(be, en, gens, c_names)
    livers = Conbined_Liver_data(be, en, livers_list)
    # livers.print_data()
    make_ranking(livers)


if __name__ == '__main__':
    main()
