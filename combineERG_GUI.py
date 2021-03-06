import os
import pandas as pd
import glob
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import subprocess

# subprocess.call('python combineERG_GUI.py', shell=True)

def main(path, savepath):
    print(savepath)
    all_files = glob.glob(path + "/*.csv")

    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)

    frame = pd.concat(li, axis=0, ignore_index=True)

    print(frame)

    frame.to_csv(savepath, index=False)

    os.startfile(savepath)


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def select_path():
    global path
    curr_directory = os.getcwd()
    filename = filedialog.askdirectory(initialdir=curr_directory, title="Select Folder")
    path.set(filename)


def default_path():
    curr_directory = os.getcwd()
    curr_directory = os.path.join(curr_directory, "Output.csv")
    savePath.set(curr_directory)


def save_path():
    curr_directory = os.getcwd()
    filename = filedialog.askdirectory(initialdir=curr_directory, title="Select Folder")
    curr_directory = os.path.join(filename, "Output.csv")
    savePath.set(curr_directory)


def completed_popup():
    messagebox.showinfo(title="Completed", message="Finished",)


def Loading():
    entry3 = tk.Entry(root, width=15, text=loading)
    entry3.place(x=100, y=125)


def dummy1():
    main(path.get(), savePath.get())
    completed_popup()


root = Tk()
root.title('Efficiency')
root.geometry('280x150')
image1 = PhotoImage(file=resource_path("images.png"))

path = StringVar()
savePath = StringVar()
loading = StringVar()
loading.set("Processing...")

label = tk.Label(root, text="Folder Path:")
label.place(x=0, y=5)
label2 = tk.Label(root, text="Save Path:")
label2.place(x=0, y=30)

entry = tk.Entry(root, width=20, text=path)
entry.place(x=67, y=7)
entry2 = tk.Entry(root, width=20, text=savePath)
entry2.place(x=67, y=32)

button1 = tk.Button(root, image=image1, width=20, height=20,  command=select_path)
button1.place(x=190, y=3)
button2 = tk.Button(root, image=image1, width=20, height=20,  command=save_path)
button2.place(x=190, y=28)
button2 = tk.Button(root, text="Default", command=default_path)
button2.place(x=218, y=29)

button1 = tk.Button(root, text="Combine",  command=dummy1)
button1.place(x=100, y=65)

root.mainloop()

