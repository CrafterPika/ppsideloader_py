import os
from tkinter import ttk, Button, Label, Entry, Tk, Menu, filedialog, messagebox
from tkinter import *
import tkinter
from tkinter.ttk import *
import shutil
import zipfile
import wget
import urllib.request
import requests
import json
import ssl
import webbrowser

#other
ssl._create_default_https_context = ssl._create_unverified_context


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
def source_code():
	url = 'https://github.com/CrafterPika/ppsideloader_py'
	webbrowser.open_new(url)

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
	if(var.get()==1):
		shutil.copy("deps/libsubstrate.dylib", "App/Payload/ppsideloader.app/Frameworks")
	else:
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
	messagebox.showinfo("Info", "Please provide a directory where you want to save the IPA!")
	folder_selected = filedialog.askdirectory()
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
	shutil.move("ppapp.ipa", folder_selected)
	print("Done.!")

def exctract_framework():
	print("Extracting Framework(s)")
	with zipfile.ZipFile("Framework.zip", 'r') as zip_ref:
		zip_ref.extractall("App/Payload/ppsideloader.app/Frameworks")
	print("Done!")

#AppCake++
def AppCake():
	messagebox.showinfo("Info", "Please provide a directory where you want to save the IPA!")
	folder_selected = filedialog.askdirectory()
	print("Creating AppCake++")
	#downloading Files
	print("Downloading ipa")
	wget.download(cont["AppCake"]["IPA"], f'./appcake.zip')
	print("\nDone!")
	print("Downloading AppCake++!")
	wget.download(cont["AppCake"]["Tweak"], f'./appcakepp.zip')
	print("\nDone!")

	#Extracting Files
	os.mkdir("App")

	print("Extracting content.")
	with zipfile.ZipFile("appcake.zip", 'r') as zip_ref:
		zip_ref.extractall("App")

	try:
		os.mkdir("App/Payload/ZipAppLite.app/Frameworks")
	except:
		pass

	if(var.get()==1):
		shutil.copy("deps/libsubstrate.dylib", "App/Payload/ppsideloader.app/Frameworks")
	else:
		with zipfile.ZipFile("deps/CydiaSubstrate.zip", 'r') as zip_ref:
			zip_ref.extractall("App/Payload/ppsideloader.app/Frameworks")

	with zipfile.ZipFile("deps/libloader.zip", 'r') as zip_ref:
		zip_ref.extractall("App/Payload/appcakej.app/")

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
	shutil.move("appcake++.ipa", folder_selected)
	print("Done.!")

#Spotify++ (w. Sposify)
def Spotify():
	messagebox.showinfo("info", "Please provide a directory where you want to save the IPA!")
	folder_selected = filedialog.askdirectory()
	print("Creating Spotify++")
	#downloading Files
	print("Downloading ipa")
	wget.download(cont["Spotify"]["IPA"], f'./spotify.zip')
	print("\nDone!")
	print("Downloading libSpotilife!")
	wget.download(cont["Spotify"]["Spotilife"], f'./libSpotilife.zip')
	print("\nDone!")
	print("Downloading libSposify!")
	wget.download(cont["Spotify"]["Sposify"], f'./libSposify.zip')
	print("\nDone!")

	#Extracting Files
	os.mkdir("App")

	print("Extracting Content.")
	with zipfile.ZipFile("spotify.zip", 'r') as zip_ref:
		zip_ref.extractall("App")

	try:
		os.mkdir("App/Payload/ZipAppLite.app/Frameworks")
	except:
		pass

	if(var.get()==1):
		shutil.copy("deps/libsubstrate.dylib", "App/Payload/ppsideloader.app/Frameworks")
	else:
		with zipfile.ZipFile("deps/CydiaSubstrate.zip", 'r') as zip_ref:
			zip_ref.extractall("App/Payload/ppsideloader.app/Frameworks")

	with zipfile.ZipFile("deps/libloader.zip", 'r') as zip_ref:
		zip_ref.extractall("App/Payload/Spotify.app/")

	os.mkdir("App/Payload/Spotify.app/libloader")

	with zipfile.ZipFile("libSpotilife.zip", 'r') as zip_ref:
		zip_ref.extractall("App/Payload/Spotify.app/libloader")

	with zipfile.ZipFile("libSposify.zip", 'r') as zip_ref:
		zip_ref.extractall("App/Payload/Spotify.app/libloader")
	print("Done!")

	#hex edit appcake
	print("Creating Main Executeable Backup.")
	os.mkdir("tmp")
	shutil.copy("App/Payload/Spotify.app/Spotify", "tmp")
	print("Done.")

	print("Generating HEX Dump (this may take a while).")
	fin = open("App/Payload/Spotify.app/Spotify", "rb")
	fout = open("App/Payload/Spotify.app/output_exec", "wb")
	data = fin.read()
	print(data)
	fout.write(data.replace(b"\x2F\x75\x73\x72\x2F\x6C\x69\x62\x2F\x6C\x69\x62\x53\x79\x73\x74\x65\x6D\x2E\x42\x2E\x64\x79\x6C\x69\x62", b"\x40\x65\x78\x65\x63\x75\x74\x61\x62\x6C\x65\x5F\x70\x61\x74\x68\x2F\x53\x79\x73\x2E\x64\x79\x6C\x69\x62"))
	fin.close()
	fout.close()
	print("Done.")

	os.remove("App/Payload/Spotify.app/Spotify")
	shutil.move("App/Payload/Spotify.app/output_exec", "App/Payload/Spotify.app/Spotify")

	# Creating Zip Archive
	print("Creating New ipa")
	shutil.make_archive("Spotify++_w.Sposify", 'zip', "App")

	#re-naming file to.ipa
	os.rename('Spotify++_w.Sposify.zip', 'Spotify++_w.Sposify.ipa')
	shutil.rmtree("App")
	shutil.rmtree("tmp")
	os.remove("spotify.zip")
	os.remove("libSpotilife.zip")
	os.remove("libSposify.zip")
	shutil.move("Spotify++_w.Sposify.ipa", folder_selected)
	print("Done.!")

#ZipAppLite++
def ZipAppLite():
	messagebox.showinfo("Info", "Please provide a directory where you want to save the IPA!")
	folder_selected = filedialog.askdirectory()
	print("Creating ZipAppLite++")
	#downloading Files
	print("Downloading ipa")
	wget.download(cont["ZipAppLite"]["IPA"], f'./ZipAppLite.zip')
	print("\nDone!")
	print("Downloading libZipAppLite!")
	wget.download(cont["ZipAppLite"]["Tweak"], f'./libZipAppLite.zip')
	print("\nDone!")

	#Extracting Files
	os.mkdir("App")

	print("Extracting Content.")
	with zipfile.ZipFile("ZipAppLite.zip", 'r') as zip_ref:
		zip_ref.extractall("App")

	try:
		os.mkdir("App/Payload/ZipAppLite.app/Frameworks")
	except:
		pass

	if(var.get()==1):
		shutil.copy("deps/libsubstrate.dylib", "App/Payload/ppsideloader.app/Frameworks")
	else:
		with zipfile.ZipFile("deps/CydiaSubstrate.zip", 'r') as zip_ref:
			zip_ref.extractall("App/Payload/ppsideloader.app/Frameworks")

	with zipfile.ZipFile("deps/libloader.zip", 'r') as zip_ref:
		zip_ref.extractall("App/Payload/ZipAppLite.app/")

	os.mkdir("App/Payload/ZipAppLite.app/libloader")
	with zipfile.ZipFile("libZipAppLite.zip", 'r') as zip_ref:
		zip_ref.extractall("App/Payload/ZipAppLite.app/libloader")
	print("Done!")

	#hex edit appcake
	print("Creating Main Executeable Backup.")
	os.mkdir("tmp")
	shutil.copy("App/Payload/ZipAppLite.app/ZipAppLite", "tmp")
	print("Done.")

	print("Generating HEX Dump (this may take a while).")
	fin = open("App/Payload/ZipAppLite.app/ZipAppLite", "rb")
	fout = open("App/Payload/ZipAppLite.app/output_exec", "wb")
	data = fin.read()
	print(data)
	fout.write(data.replace(b"\x2F\x75\x73\x72\x2F\x6C\x69\x62\x2F\x6C\x69\x62\x53\x79\x73\x74\x65\x6D\x2E\x42\x2E\x64\x79\x6C\x69\x62", b"\x40\x65\x78\x65\x63\x75\x74\x61\x62\x6C\x65\x5F\x70\x61\x74\x68\x2F\x53\x79\x73\x2E\x64\x79\x6C\x69\x62"))
	fin.close()
	fout.close()
	print("Done.")

	os.remove("App/Payload/ZipAppLite.app/ZipAppLite")
	shutil.move("App/Payload/ZipAppLite.app/output_exec", "App/Payload/ZipAppLite.app/ZipAppLite")

	# Creating Zip Archive
	print("Creating New ipa")
	shutil.make_archive("ZipAppLite++", 'zip', "App")

	#re-naming file to.ipa
	os.rename('ZipAppLite++.zip', 'ZipAppLite++.ipa')
	shutil.rmtree("App")
	shutil.rmtree("tmp")
	os.remove("ZipAppLite.zip")
	os.remove("libZipAppLite.zip")
	shutil.move("ZipAppLite++.ipa", folder_selected)
	print("Done.!")

def restore_app_exec_backup():

	def restore_backup2():
		print("Restoring Backup")
		os.remove("App/Payload/ppsideloader.app/"+exec_app2.get())
		shutil.copy("tmp/"+exec_app2.get(), "App/Payload/ppsideloader.app/"+exec_app2.get())
		print("Done!")

	restore = Tk()
	restore.title("Restore App Executeable")
	restore.geometry("370x150")
	restore.iconbitmap('icon.ico')
	title = Label(restore, text="Restore App Executeable")
	title.pack()

	empty = Label(restore, text="")
	empty.pack()
	name = Label(restore, text="App Exec Name")
	name.pack()
	exec_app2 = ttk.Entry(restore)
	exec_app2.pack()
	restore_backup = ttk.Button(restore, text="Restore Backup", command=restore_backup2)
	restore_backup.pack()

	restore.mainloop()


main = Tk()
main.title("ppsideloader")
main.geometry("500x375")
main.iconbitmap('icon.ico')

title = Label(main, text="PPSideloader")
title.pack()

var = tkinter.IntVar()
libsubstrate = ttk.Checkbutton(main, text="Use libsubstrate.dylib.", variable=var, onvalue=1, offvalue=0)
libsubstrate.pack()

empty = Label(main, text="")
empty.pack()
empty2 = Label(main, text="")
empty2.pack()

Step1 = Label(main, text="Step 1:")
Step1.pack()
extract = ttk.Button(main, text="Extract Files", command=extract)
extract.pack()

empty3 = Label(main, text="")
empty3.pack()

Step2 = Label(main, text="Step 2:")
Step2.pack()
empty6 = Label(main, text="")
empty6.pack()
exec_app_name = Label(main, text="Enter App Exec Name:")
exec_app_name.pack()
exec_app = ttk.Entry(main)
exec_app.pack()
hex_edit = ttk.Button(main, text="Hex Edit App", command=hex_edit)
hex_edit.pack()

empty4 = Label(main, text="")
empty4.pack()

Step3 = Label(main, text="Step 3:")
Step3.pack()
make_ipa = ttk.Button(main, text="Creat IPA", command=make_ipa)
make_ipa.pack()

empty5 = Label(main, text="")
empty5.pack()
title2 = Label(main, text="Follow me on Twitter: @CrafterPika")
title2.pack()

toolmenu=Menu()
tweaks=Menu()
tweaks.add_command(label='AppCake++', command=AppCake)
tweaks.add_command(label='Spotify++', command=Spotify)
tweaks.add_command(label='ZipAppLite++', command=ZipAppLite)
utils=Menu()
utils.add_command(label='Extract External Framework(s)', command=exctract_framework)
utils.add_command(label='Restore App Executable', command=restore_app_exec_backup)
toolmenu.add_cascade(label='Tweaks',menu=tweaks)
toolmenu.add_cascade(label='Utils',menu=utils)
toolmenu.add_command(label='Source Code', command=source_code)
main.config(menu=toolmenu)

main.mainloop()
