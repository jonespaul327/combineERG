import pandas as pd
import glob
import os


def main(path, savepath):

    all_files = glob.glob(path + "/*.csv")

    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)

    frame = pd.concat(li, axis=0, ignore_index=True)

    print(frame)

    frame.to_csv(savepath, index=False)

    os.startfile(savepath)
