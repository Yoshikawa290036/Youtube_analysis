import os
import time
import sys
import analysis

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', buffering=1)
sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', buffering=1)
sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', buffering=1)

def wait_pickle_exist(files: list):
    bet = 10
    not_yet = "not yet"
    status = [not_yet] * len(files)
    for i in range(2000):
        print("----------------------")
        time_str = f"{str(i*bet//3600).zfill(2)} : {str(i*bet//60).zfill(2)} : {str(i*bet%60).zfill(2)}"
        print(f"time  {time_str}")
        flag = True
        for j in range(len(files)):
            if not os.path.exists(files[j]):
                print(f"{files[j]}\t\twas not yet")
                flag = False
            else:
                if status[j] == not_yet:
                    status[j] = time_str
        if flag:
            break
        print(f"wating {bet} s")
        # print()
        time.sleep(bet)
    
    print("All pickle files were CREATED !!")
    print("----------------------")
    for i in range(len(files)):
        print(f"{status[i]}\t\t{files[i]}")
    print("----------------------")


def main():
    be, en, gens, c_names = analysis.read_go()
    files = []
    for i in range(len(gens)):
        files.append(os.path.join(f"{be}-{en}", f"{gens[i]}_{c_names[i]}", "Liver_data.pickle"))
    wait_pickle_exist(files)
    print("Starting Analysis ....")
    analysis.main()


if __name__ == '__main__':
    main()
