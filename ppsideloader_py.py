import os
from tkinter import ttk, Button, Label, Entry, Tk

print("*** PPSideloader By CrafterPika ***")
print("*** Twitter: @CrafterPika ***")
print("*** License: none ***")
print("*** Source Code: https://github.com/CrafterPika/ppsideloader_py ***")
print("")
print("Loading UI...")
print("")

#Commands:
def extract():
	os.system('py -3 ./extract.py')

def hex_edit():
	print("*** PPSideloader By CrafterPika ***")
	print("*** Twitter: @CrafterPika ***")
	print("*** License: none ***")
	print("*** Source Code: https://github.com/CrafterPika/ppsideloader_py ***")
	print("")
	print("WIP. Not Finished yet. hopefully s0n. ETA WEN?!?!")
	print("")
	print("Instrcustion to hex app manually:")
	print("1. Open '/App/Payload/ppsideloader.app/[NameOfAppYouWanttoTweak]' in a hex editor")
	print("2. Replace the following String '/usr/lib/libSystem.B.dylib' with '@executable_path/Sys.dylib'")
	print("3. Save and then press 'Creat IPA' on the UI windows.")

def make_ipa():
	os.system('py -3 ./make_ipa.py')

main = Tk()
main.title("ppsideloader")
main.geometry("500x350")

title = ttk.Label(main, text="PPSideloader")
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
empty6 = ttk.Label(main, text="")
empty6.pack()
exec_app_name = ttk.Label(main, text="Enter App Exec Name:")
exec_app_name.pack()
exec_app = ttk.Entry(main)
exec_app.pack()
hex_edit = ttk.Button(main, text="Hex Edit App", command=hex_edit)
hex_edit.pack()

empty4 = ttk.Label(main, text="")
empty4.pack()

Step3 = ttk.Label(main, text="Step 3:")
Step3.pack()
make_ipa = ttk.Button(main, text="Creat IPA", command=make_ipa)
make_ipa.pack()

empty5 = ttk.Label(main, text="")
empty5.pack()
title = ttk.Label(main, text="Follow me on Twitter: @CrafterPika")
title.pack()

main.mainloop()