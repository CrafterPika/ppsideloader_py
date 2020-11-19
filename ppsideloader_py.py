#tkinter
from tkinter import ttk, Button, Label, Entry, Tk, Menu, filedialog, messagebox
from tkinter import *
import tkinter
from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk

#modules
import webbrowser
import shutil
import zipfile
import os
import glob
import plistlib
import threading

#Commands
def select_ipa():
    global ipa_file
    ipa_file = filedialog.askopenfilename(initialdir=f"{os.getcwd()}", filetypes=[('iOS Application Files', '*.ipa')])

def select_tweak():
    global tweak_file
    tweak_file = filedialog.askopenfilename(initialdir=f"{os.getcwd()}", filetypes=[('Dynamic Library Files', '*.dylib')])

def DO_IT():
    DO_IT1.config(text="1/3 Extracting")
    os.rename(ipa_file, f"{os.getcwd()}/ipa.zip")
    os.mkdir("app")
    with zipfile.ZipFile(f"{os.getcwd()}/ipa.zip", 'r') as zip_ref:
        zip_ref.extractall(f"{os.getcwd()}/app/")
    os.remove("ipa.zip")
    orig = os.getcwd()
    os.chdir(f"{os.getcwd()}/app/Payload/")
    for file in glob.glob("*.app"):
        path = os.path.join(f"{orig}/app/Payload", file)
        print(path)
    os.chdir(orig)

    DO_IT1.config(text="2/3 Modifying")
    with open(f"{path}/Info.plist", 'rb') as fp:
        pl = plistlib.load(fp)
    data1 = pl["CFBundleExecutable"]
    print(f"{path}/{data1}")

    shutil.copy(f"{os.getcwd()}/assets/libloader.dylib", f"{path}/Sys.dylib")
    os.mkdir(f"{path}/libloader")
    try:
        os.mkdir(f"{path}/Frameworks")
    except:
        pass
    with zipfile.ZipFile(f"{os.getcwd()}/assets/CydiaSubstrate.zip", 'r') as zip_ref:
        zip_ref.extractall(f"{path}/Frameworks/")

    fin = open(f"{path}/{data1}", "rb")
    fout = open(f"{path}/output_exec", "wb")

    data = fin.read()
    fout.write(data.replace(b"\x2F\x75\x73\x72\x2F\x6C\x69\x62\x2F\x6C\x69\x62\x53\x79\x73\x74\x65\x6D\x2E\x42\x2E\x64\x79\x6C\x69\x62", b"\x40\x65\x78\x65\x63\x75\x74\x61\x62\x6C\x65\x5F\x70\x61\x74\x68\x2F\x53\x79\x73\x2E\x64\x79\x6C\x69\x62"))
    fin.close()
    fout.close()

    os.remove(f"{path}/{data1}")
    shutil.move(f"{path}/output_exec", f"{path}/{data1}")

    shutil.move(f"{tweak_file}", f"{path}/libloader")
    DO_IT1.config(text="3/3 Compressing")

    shutil.make_archive(f"{data1}", "zip", "app")
    shutil.rmtree("app")
    os.rename(f"{data1}.zip", f"{data1}.ipa")
    DO_IT1.config(text="Done!")

def t1():
    thread1 = threading.Thread(target=DO_IT)
    thread1.start()

main = Tk()
main.title("ppsideloader")
main.geometry("400x275")
main.iconbitmap('icon.ico')

title = Label(main, text="PPSideloader")
title.pack()

empty = Label(main, text="")
empty.pack()
Step1 = Label(main, text="Step 1:")
Step1.pack()
select_ipa1 = ttk.Button(main, text="Select iPA", command=select_ipa)
select_ipa1.pack()

empty1 = Label(main, text="")
empty1.pack()
Step2 = Label(main, text="Step 2:")
Step2.pack()
select_ipa1 = ttk.Button(main, text="Select Tweak", command=select_tweak)
select_ipa1.pack()

empty2 = Label(main, text="")
empty2.pack()
Step3 = Label(main, text="Step 3:")
Step3.pack()
global DO_IT1
DO_IT1 = ttk.Button(main, text="Do It!", command=t1)
DO_IT1.pack()

empty3 = Label(main, text="")
empty3.pack()
copyright = Label(main, text="(c) 2020 CrafterPika")
copyright.pack()


main.mainloop()
