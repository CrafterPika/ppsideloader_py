#tkinter
from tkinter import ttk, Button, Label, Entry, Tk, Menu, filedialog, messagebox, OptionMenu
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
import time
import requests
import random
import json
import shlex
import subprocess

#Hotel Trivago
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "w", "x", "y", "z"]
cap_abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y", "Z"]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#Commands
def source_code():
	url = 'https://github.com/CrafterPika/ppsideloader_py'
	webbrowser.open_new(url)

def select_ipa():
    global ipa_file
    ipa_file = filedialog.askopenfilename(initialdir=f"{os.getcwd()}", filetypes=[('iOS Application Files', '*.ipa')])

def select_tweak():
    global tweak_file
    tweak_file = filedialog.askopenfilename(initialdir=f"{os.getcwd()}", filetypes=[('Dynamic Library Files', '*.dylib')])

def DO_IT():
    DO_IT1.config(text="1/4 Extracting", state='disabled')
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

    DO_IT1.config(text="2/4 Modifying", state='disabled')
    with open(f"{path}/Info.plist", 'rb') as fp:
        pl = plistlib.load(fp)
    data1 = pl["CFBundleExecutable"]
    print(f"{path}/{data1}")

    if(var3.get()==1):
        shutil.move(f"{tweak_file}", f"{path}/Twk.dylib")
    else:
        shutil.copy(f"{os.getcwd()}/assets/libloader.dylib", f"{path}/Sys.dylib")
        os.mkdir(f"{path}/libloader")

    try:
        os.mkdir(f"{path}/Frameworks")
    except:
        pass
    if(var4.get()==1):
        shutil.copy(f"{os.getcwd()}/assets/libsubstrate.dylib", f"{path}/Frameworks/libsubstrate.dylib")
    else:
        with zipfile.ZipFile(f"{os.getcwd()}/assets/CydiaSubstrate.zip", 'r') as zip_ref:
            zip_ref.extractall(f"{path}/Frameworks/")

    fin = open(f"{path}/{data1}", "rb")
    fout = open(f"{path}/output_exec", "wb")

    data = fin.read()
    if(var3.get()==1):
        fout.write(data.replace(b"\x2F\x75\x73\x72\x2F\x6C\x69\x62\x2F\x6C\x69\x62\x53\x79\x73\x74\x65\x6D\x2E\x42\x2E\x64\x79\x6C\x69\x62", b"\x40\x65\x78\x65\x63\x75\x74\x61\x62\x6c\x65\x5f\x70\x61\x74\x68\x2f\x54\x77\x6b\x2e\x64\x79\x6c\x69\x62"))
    else:
        fout.write(data.replace(b"\x2F\x75\x73\x72\x2F\x6C\x69\x62\x2F\x6C\x69\x62\x53\x79\x73\x74\x65\x6D\x2E\x42\x2E\x64\x79\x6C\x69\x62", b"\x40\x65\x78\x65\x63\x75\x74\x61\x62\x6C\x65\x5F\x70\x61\x74\x68\x2F\x53\x79\x73\x2E\x64\x79\x6C\x69\x62"))
    fin.close()
    fout.close()

    os.remove(f"{path}/{data1}")
    shutil.move(f"{path}/output_exec", f"{path}/{data1}")
    if(var3.get()==1):
        pass
    else:
        shutil.move(f"{tweak_file}", f"{path}/libloader")

    if(var1.get()==1):
        shutil.copy(f"./assets/addons/dlgmemor.dylib", f"{path}/libloader")
    else:
        pass

    if(var2.get()==1):
        shutil.copy(f"./assets/addons/FLEX_Jailed.dylib", f"{path}/libloader")
    else:
        pass

    time.sleep(5)

    DO_IT1.config(text="3/4 Compressing", state='disabled')
    shutil.make_archive(f"{data1}", "zip", "app")
    shutil.rmtree("app")
    os.rename(f"{data1}.zip", f"{data1}.ipa")
    DO_IT1.config(text="4/4 Done!", state='enabled')
    time.sleep(5)
    DO_IT1.config(text="Start!", state='enabled')

def t1():
    thread1 = threading.Thread(target=DO_IT)
    thread1.start()

def sign_app():
    # init
    certAPI1 = requests.get("https://api.crafterpika.ml/v1/cert.php")
    certAPI = certAPI1.json()
    certDB1 = requests.get("https://api.crafterpika.ml/public_certs/cert.json")
    certDB = certDB1.json()

    #Functions
    def zsign():
        random1 = random.choice(abc)
        random2 = random.choice(number)
        random3 = random.choice(abc)
        random4 = random.choice(number)
        random5 = random.choice(cap_abc)

        random6 = random.choice(abc)
        random7 = random.choice(number)
        random8 = random.choice(abc)
        random9 = random.choice(number)
        random10 = random.choice(cap_abc)
        bundle_id = f"com.{random1}{random2}{random3}{random4}{random5}.{random6}{random7}{random8}{random9}{random10}.{clicked.get()}.crafterpika"

        r = requests.get(f"{certDB[f'{clicked.get()}']['p12']}")
        with open(f'{os.getcwd()}/{clicked.get()}.p12', 'wb') as f:
            f.write(r.content)

        r = requests.get(f"{certDB[f'{clicked.get()}']['mobileprovision']}")
        with open(f'{os.getcwd()}/{clicked.get()}.mobileprovision', 'wb') as f:
            f.write(r.content)

        print(clicked.get())
        subprocess.run(shlex.split(f"zsign -k '{clicked.get()}.p12' -p {certDB[f'{clicked.get()}']['password']} -m '{clicked.get()}.mobileprovision' -b {bundle_id} -o '{os.getcwd()}/ipa_signed.ipa' -z 9 '{ipa_file1}'"))
        pass

    def sipa():
        global ipa_file1
        ipa_file1 = filedialog.askopenfilename(initialdir=f"{os.getcwd()}", filetypes=[('iOS Application Files', '*.ipa')])
        print(ipa_file1)

    signer = Tk()
    signer.title("Sign App")
    signer.iconbitmap('icon.ico')
    signer.geometry("370x150")

    #Title
    title = Label(signer, text="Sign App")
    title.pack()
    empty = Label(signer, text="")
    empty.pack()

    #Dropdown Menu for certs and ipa-select button
    bruh = Label(signer, text="Certificate & iPA")
    bruh.pack()
    clicked = StringVar()
    dropdown = ttk.OptionMenu(signer, clicked, *certAPI)
    dropdown.pack()
    select_ipa1 = ttk.Button(signer, text="Select iPA", command=sipa)
    select_ipa1.pack()

    #Sign :evil:
    empty = Label(signer, text="")
    empty.pack()
    sign = ttk.Button(signer, text="Sign iPA", command=zsign)
    sign.pack()

    signer.mainloop()

main = Tk()
main.title("ppsideloader")
main.geometry("400x390")
main.iconbitmap('icon.ico')

#global
global DO_IT1
global select_ipa1
global select_tweak1

title = Label(main, text="PPSideloader")
title.pack()

#frame
settings_frame = ttk.LabelFrame(main, text="Settings")
settings_frame.pack()
addons_frame = ttk.LabelFrame(main, text="Addons")
addons_frame.pack()

#addons
var1 = tkinter.IntVar()
dlgmemor = ttk.Checkbutton(addons_frame, text="Add DLGMemor Injected.          ", variable=var1, onvalue=1, offvalue=0)
dlgmemor.pack()
var2 = tkinter.IntVar()
FLEX = ttk.Checkbutton(addons_frame, text="Add FLEX.                                     ", variable=var2, onvalue=1, offvalue=0)
FLEX.pack()

#settings
var3 = tkinter.IntVar()
libloader = ttk.Checkbutton(settings_frame, text="Don't use libloader.                    ", variable=var3, onvalue=1, offvalue=0)
libloader.pack()
var4 = tkinter.IntVar()
libsubstrate = ttk.Checkbutton(settings_frame, text="Use libsubstrate.                         ", variable=var4, onvalue=1, offvalue=0)
libsubstrate.pack()

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
select_tweak1 = ttk.Button(main, text="Select Tweak", command=select_tweak)
select_tweak1.pack()

empty2 = Label(main, text="")
empty2.pack()
Step3 = Label(main, text="Step 3:")
Step3.pack()
DO_IT1 = ttk.Button(main, text="Start!", command=t1)
DO_IT1.pack()

empty3 = Label(main, text="")
empty3.pack()
copyright = Label(main, text="(c) 2020 CrafterPika")
copyright.pack()

#ToolBar
toolmenu=Menu()
options=Menu()
toolmenu.add_cascade(label='Options',menu=options)
options.add_command(label='Sign', command=sign_app)
toolmenu.add_command(label='Source Code', command=source_code)
main.config(menu=toolmenu)

main.mainloop()
