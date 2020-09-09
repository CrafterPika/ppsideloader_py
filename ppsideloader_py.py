import os
from tkinter import ttk, Button, Label, Entry, Tk, Menu
import shutil
import zipfile
import wget
import urllib.request
import requests
import json

#json:
url = 'https://raw.githubusercontent.com/CrafterPika/ppsideloader_py/files/index.json'
req = urllib.request.Request(url)
r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))
counter = 0

print("*** PPSideloader By CrafterPika ***")
print("*** Twitter: @CrafterPika ***")
print("*** License: none ***")
print("*** Source Code: https://github.com/CrafterPika/ppsideloader_py ***")
print("")
print("Loading UI...")
print("")

#Commands:
def extract():
	print("*** PPSideloader By CrafterPika ***")
	print("*** Twitter: @CrafterPika ***")
	print("*** License: none ***")
	print("*** Source Code: https://github.com/CrafterPika/ppsideloader_py ***")
	print("")

	#creating directories
	print("Creating Directories!")
	os.mkdir("App")
	os.mkdir("App/Payload")
	os.mkdir("App/Payload/ppsideloader.app")
	os.mkdir("App/Payload/ppsideloader.app/Frameworks")
	os.mkdir("App/Payload/ppsideloader.app/libloader")
	print("Done!")

	#Extracting Files
	print("Extracting Importand Files!")
	with zipfile.ZipFile("deps/CydiaSubstrate.zip", 'r') as zip_ref:
		zip_ref.extractall("App/Payload/ppsideloader.app/Frameworks")

	with zipfile.ZipFile("deps/libloader.zip", 'r') as zip_ref:
		zip_ref.extractall("App/Payload/ppsideloader.app/")
	print("Done!")

	#moving Tweak
	print("Extracting Tweak!")
	with zipfile.ZipFile("Tweak.zip", 'r') as zip_ref:
		zip_ref.extractall("App/Payload/ppsideloader.app/libloader")
	print("Done!")

	#app
	print("Extracting App Zip.")
	with zipfile.ZipFile("app.zip", 'r') as zip_ref:
		zip_ref.extractall("App/Payload/ppsideloader.app/")
	print("Done!")

def hex_edit():
	print("*** PPSideloader By CrafterPika ***")
	print("*** Twitter: @CrafterPika ***")
	print("*** License: none ***")
	print("*** Source Code: https://github.com/CrafterPika/ppsideloader_py ***")
	print("")

	print("Creating Main Executeable Backup.")
	os.mkdir("tmp")
	shutil.copy("App/Payload/ppsideloader.app/"+exec_app.get(), "tmp")
	print("Done.")

	print("Generating HEX Dump (this may take a while).")
	fin = open("App/Payload/ppsideloader.app/"+exec_app.get(), "rb")
	fout = open("App/Payload/ppsideloader.app/output_exec", "wb")
	data = fin.read()
	print(data)
	fout.write(data.replace(b"\x2F\x75\x73\x72\x2F\x6C\x69\x62\x2F\x6C\x69\x62\x53\x79\x73\x74\x65\x6D\x2E\x42\x2E\x64\x79\x6C\x69\x62", b"\x40\x65\x78\x65\x63\x75\x74\x61\x62\x6C\x65\x5F\x70\x61\x74\x68\x2F\x53\x79\x73\x2E\x64\x79\x6C\x69\x62"))
	fin.close()
	fout.close()
	print("Done.")

	os.remove("App/Payload/ppsideloader.app/"+exec_app.get())
	shutil.move("App/Payload/ppsideloader.app/output_exec", "App/Payload/ppsideloader.app/"+exec_app.get())

	print("Hopefully Replaced '/usr/lib/libSystem.B.dylib' with '@executable_path/Sys.dylib' in"+exec_app.get())
	print("Note: if it did not work please do replace this string manually in a HEX editor")

def make_ipa():
	print("*** PPSideloader By CrafterPika ***")
	print("*** Twitter: @CrafterPika ***")
	print("*** License: none ***")
	print("*** Source Code: https://github.com/CrafterPika/ppsideloader_py ***")
	print("")

	print("Creating New ipa")
	# Creating Zip Archive
	shutil.make_archive("ppapp", 'zip', "App")

	#re-naming file to.ipa
	os.rename('ppapp.zip', 'ppapp.ipa')
	shutil.rmtree("App")
	shutil.rmtree("tmp")
	print("Done.!")

def exctract_framework():
	print("Extracting Framework(s)")
	with zipfile.ZipFile("Framework.zip", 'r') as zip_ref:
		zip_ref.extractall("App/Payload/ppsideloader.app/Frameworks")
	print("Done!")

#AppCake++
def make_appcake_pp():
	print("Creating AppCake++")
	#downloading Files
	print("Downloading ipa")
	wget.download(cont["appcake"], f'./appcake.zip')
	print("\nDone!")
	print("Downloading AppCake++!")
	wget.download(cont["appcake_pp"], f'./appcakepp.zip')
	print("\nDone!")

	#Extracting Files
	os.mkdir("App")

	print("Extracting AppCake Zip.")
	with zipfile.ZipFile("appcake.zip", 'r') as zip_ref:
		zip_ref.extractall("App")
	print("Done!")

	print("Extracting Importand Files!")
	with zipfile.ZipFile("deps/CydiaSubstrate.zip", 'r') as zip_ref:
		zip_ref.extractall("App/Payload/appcakej.app/Frameworks")

	with zipfile.ZipFile("deps/libloader.zip", 'r') as zip_ref:
		zip_ref.extractall("App/Payload/appcakej.app/")
	print("Done!")

	os.mkdir("App/Payload/appcakej.app/libloader")
	with zipfile.ZipFile("appcakepp.zip", 'r') as zip_ref:
		zip_ref.extractall("App/Payload/appcakej.app/libloader")
	print("Done!")

	#hex edit appcake
	print("Creating Main Executeable Backup.")
	os.mkdir("tmp")
	shutil.copy("App/Payload/appcakej.app/appcakej", "tmp")
	print("Done.")

	print("Generating HEX Dump (this may take a while).")
	fin = open("App/Payload/appcakej.app/appcakej", "rb")
	fout = open("App/Payload/appcakej.app/output_exec", "wb")
	data = fin.read()
	print(data)
	fout.write(data.replace(b"\x2F\x75\x73\x72\x2F\x6C\x69\x62\x2F\x6C\x69\x62\x53\x79\x73\x74\x65\x6D\x2E\x42\x2E\x64\x79\x6C\x69\x62", b"\x40\x65\x78\x65\x63\x75\x74\x61\x62\x6C\x65\x5F\x70\x61\x74\x68\x2F\x53\x79\x73\x2E\x64\x79\x6C\x69\x62"))
	fin.close()
	fout.close()
	print("Done.")

	os.remove("App/Payload/appcakej.app/appcakej")
	shutil.move("App/Payload/appcakej.app/output_exec", "App/Payload/appcakej.app/appcakej")

	# Creating Zip Archive
	print("Creating New ipa")
	shutil.make_archive("appcake++", 'zip', "App")

	#re-naming file to.ipa
	os.rename('appcake++.zip', 'appcake++.ipa')
	shutil.rmtree("App")
	shutil.rmtree("tmp")
	os.remove("appcakepp.zip")
	os.remove("appcake.zip")
	print("Done.!")






# UI
main = Tk()
main.title("ppsideloader")
main.geometry("500x350")
main.iconbitmap('icon.ico')

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

toolmenu=Menu()
tweaks=Menu()
tweaks.add_command(label='Creat AppCake++', command=make_appcake_pp)
utils=Menu()
utils.add_command(label='Extract External Framework(s)', command=exctract_framework)
toolmenu.add_cascade(label='Tweaks',menu=tweaks)
toolmenu.add_cascade(label='Utils',menu=utils)
main.config(menu=toolmenu)

main.mainloop()
