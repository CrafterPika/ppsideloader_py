import os
from tkinter import ttk, Button, Label, Tk

#Commands:
def extract():
	os.system('py -3 ./extract.py')

def hex_edit():
	os.system('py -3 ./hex_edit.py')

def make_ipa():
	os.system('py -3 ./make_ipa.py')

main = Tk()
main.title("ppsideloader py")
main.geometry("500x250")

title = ttk.Label(main, text="PPSideloader, Python Implenention")
title.pack()

empty = ttk.Label(main, text="")
empty.pack()
empty2 = ttk.Label(main, text="")
empty2.pack()

Step1 = ttk.Label(main, text="Step 1:")
Step1.pack()
extract = ttk.Button(main, text="Extract Files", command=extract)
extract.pack()

empty3 = ttk.Label(main, text="")
empty3.pack()

Step2 = ttk.Label(main, text="Step 2:")
Step2.pack()
hex_edit = ttk.Button(main, text="Hex Edit App", command=hex_edit)
hex_edit.pack()

empty4 = ttk.Label(main, text="")
empty4.pack()

Step3 = ttk.Label(main, text="Step 3:")
Step3.pack()
make_ipa = ttk.Button(main, text="Creat IPA", command=make_ipa)
make_ipa.pack()

main.mainloop()