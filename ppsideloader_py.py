import os
from tkinter import ttk, Button, Label, Entry, Tk, Menu
import tkinter
from tkinter.ttk import *
import shutil
import zipfile
import wget
import urllib.request
import requests
import json
import webbrowser

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

	print("Extracting content.")
	with zipfile.ZipFile("appcake.zip", 'r') as zip_ref:
		zip_ref.extractall("App")

	with zipfile.ZipFile("deps/CydiaSubstrate.zip", 'r') as zip_ref:
		zip_ref.extractall("App/Payload/appcakej.app/Frameworks")

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
	print("Done.!")

#Spotify++
def make_Spotify_pp():
	print("Creating Spotify++")
	#downloading Files
	print("Downloading ipa")
	wget.download(cont["spotify"], f'./spotify.zip')
	print("\nDone!")
	print("Downloading libSpotilife!")
	wget.download(cont["libSpotilife"], f'./libSpotilife.zip')
	print("\nDone!")

	#Extracting Files
	os.mkdir("App")

	print("Extracting Content.")
	with zipfile.ZipFile("spotify.zip", 'r') as zip_ref:
		zip_ref.extractall("App")

	os.mkdir("App/Payload/Spotify.app/Frameworks")
	print("Extracting Importand Files!")
	with zipfile.ZipFile("deps/CydiaSubstrate.zip", 'r') as zip_ref:
		zip_ref.extractall("App/Payload/Spotify.app/Frameworks")

	with zipfile.ZipFile("deps/libloader.zip", 'r') as zip_ref:
		zip_ref.extractall("App/Payload/Spotify.app/")

	os.mkdir("App/Payload/Spotify.app/libloader")
	with zipfile.ZipFile("libSpotilife.zip", 'r') as zip_ref:
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
	shutil.make_archive("Spotify++", 'zip', "App")

	#re-naming file to.ipa
	os.rename('Spotify++.zip', 'Spotify++.ipa')
	shutil.rmtree("App")
	shutil.rmtree("tmp")
	os.remove("spotify.zip")
	os.remove("libSpotilife.zip")
	print("Done.!")

#Spotify++ (w. Sposify)
def make_Spotify_w_spotilife_sposify():
	print("Creating Spotify++")
	#downloading Files
	print("Downloading ipa")
	wget.download(cont["spotify"], f'./spotify.zip')
	print("\nDone!")
	print("Downloading libSpotilife!")
	wget.download(cont["libSpotilife"], f'./libSpotilife.zip')
	print("\nDone!")
	print("Downloading libSposify!")
	wget.download(cont["libSposify"], f'./libSposify.zip')
	print("\nDone!")

	#Extracting Files
	os.mkdir("App")

	print("Extracting Content.")
	with zipfile.ZipFile("spotify.zip", 'r') as zip_ref:
		zip_ref.extractall("App")

	os.mkdir("App/Payload/Spotify.app/Frameworks")

	print("Extracting Importand Files!")
	with zipfile.ZipFile("deps/CydiaSubstrate.zip", 'r') as zip_ref:
		zip_ref.extractall("App/Payload/Spotify.app/Frameworks")

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
	print("Done.!")

def restore_app_exec_backup():

	def restore_backup2():
		print("Restoring Backup")
		os.remove("App/Payload/ppsideloader.app/"+exec_app2.get())
		shutil.copy("tmp/"+exec_app2.get(), "App/Payload/ppsideloader.app/"+exec_app2.get())
		print("Done!")


	def darkmode():
		restore.config(bg="#000000")
		title.config(background="#000000", foreground="#ffffff")
		empty.config(background="#000000", foreground="#ffffff")
		name.config(background="#000000", foreground="#ffffff")
		dark2.config(text="White Mode", command=whitemode)

	def whitemode():
		restore.config(bg="#ffffff")
		title.config(background="#ffffff", foreground="#000000")
		empty.config(background="#ffffff", foreground="#000000")
		name.config(background="#ffffff", foreground="#000000")
		dark2.config(text="Dark Mode", command=darkmode)

	restore = Tk()
	restore.title("Restore App Executeable")
	restore.config(bg="#ffffff")
	restore.geometry("370x150")
	restore.iconbitmap('icon.ico')
	title = Label(restore, text="Restore App Executeable")
	title.config(background="#ffffff", foreground="#000000")
	title.pack()
	#Dark/White Mode
	dark2 = ttk.Button(restore, text="Dark Mode", command=darkmode)
	dark2.pack()
	empty = Label(restore, text="")
	empty.config(background="#ffffff", foreground="#000000")
	empty.pack()
	name = Label(restore, text="App Exec Name")
	name.config(background="#ffffff", foreground="#000000")
	name.pack()
	exec_app2 = ttk.Entry(restore)
	exec_app2.pack()
	restore_backup = ttk.Button(restore, text="Restore Backup", command=restore_backup2)
	restore_backup.pack()

	restore.mainloop()


def dark_mode():
	main.config(bg="#000000")
	dark.config(text="White Mode", command=white_mode)
	title.config(background="#000000", foreground="#ffffff")
	empty.config(background="#000000", foreground="#ffffff")
	empty2.config(background="#000000", foreground="#ffffff")
	Step1.config(background="#000000", foreground="#ffffff")
	empty3.config(background="#000000", foreground="#ffffff")
	Step2.config(background="#000000", foreground="#ffffff")
	empty6.config(background="#000000", foreground="#ffffff")
	empty4.config(background="#000000", foreground="#ffffff")
	Step3.config(background="#000000", foreground="#ffffff")
	empty5.config(background="#000000", foreground="#ffffff")
	title2.config(background="#000000", foreground="#ffffff")
	exec_app_name.config(background="#000000", foreground="#ffffff")

def white_mode():
	main.config(bg="#ffffff")
	dark.config(text="Dark Mode", command=dark_mode)
	title.config(background="#ffffff", foreground="#000000")
	empty.config(background="#ffffff", foreground="#000000")
	empty2.config(background="#ffffff", foreground="#000000")
	Step1.config(background="#ffffff", foreground="#000000")
	empty3.config(background="#ffffff", foreground="#000000")
	Step2.config(background="#ffffff", foreground="#000000")
	empty6.config(background="#ffffff", foreground="#000000")
	empty4.config(background="#ffffff", foreground="#000000")
	Step3.config(background="#ffffff", foreground="#000000")
	empty5.config(background="#ffffff", foreground="#000000")
	title2.config(background="#ffffff", foreground="#000000")
	exec_app_name.config(background="#ffffff", foreground="#000000")




# UI
#Global
global title
global empty
global empty2
global Step1
global empty3
global Step2
global empty6
global empty4
global Step3
global empty5
global title2
global exec_app_name
global dark
global restore

main = Tk()
main.title("ppsideloader")
main.config(bg="#ffffff")
main.geometry("500x375")
main.iconbitmap('icon.ico')

title = Label(main, text="PPSideloader")
title.config(background="#ffffff", foreground="#000000")
title.pack()
#Dark/White Mode
dark = ttk.Button(main, text="Dark Mode", command=dark_mode)
dark.pack()

empty = Label(main, text="")
empty.config(background="#ffffff", foreground="#000000")
empty.pack()
empty2 = Label(main, text="")
empty2.config(background="#ffffff", foreground="#000000")
empty2.pack()

Step1 = Label(main, text="Step 1:")
Step1.config(background="#ffffff", foreground="#000000")
Step1.pack()
extract = ttk.Button(main, text="Extract Files", command=extract)
extract.pack()

empty3 = Label(main, text="")
empty3.config(background="#ffffff", foreground="#000000")
empty3.pack()

Step2 = Label(main, text="Step 2:")
Step2.config(background="#ffffff", foreground="#000000")
Step2.pack()
empty6 = Label(main, text="")
empty6.config(background="#ffffff", foreground="#000000")
empty6.pack()
exec_app_name = Label(main, text="Enter App Exec Name:")
exec_app_name.config(background="#ffffff", foreground="#000000")
exec_app_name.pack()
exec_app = ttk.Entry(main)
exec_app.pack()
hex_edit = ttk.Button(main, text="Hex Edit App", command=hex_edit)
hex_edit.pack()

empty4 = Label(main, text="")
empty4.config(background="#ffffff", foreground="#000000")
empty4.pack()

Step3 = Label(main, text="Step 3:")
Step3.config(background="#ffffff", foreground="#000000")
Step3.pack()
make_ipa = ttk.Button(main, text="Creat IPA", command=make_ipa)
make_ipa.pack()

empty5 = Label(main, text="")
empty5.config(background="#ffffff", foreground="#000000")
empty5.pack()
title2 = Label(main, text="Follow me on Twitter: @CrafterPika")
title2.config(background="#ffffff", foreground="#000000")
title2.pack()

toolmenu=Menu()
tweaks=Menu()
tweaks.add_command(label='AppCake++', command=make_appcake_pp)
tweaks.add_command(label='Spotify++', command=make_Spotify_pp)
tweaks.add_command(label='Spotify++ (w. Sposify)', command=make_Spotify_w_spotilife_sposify)
utils=Menu()
utils.add_command(label='Extract External Framework(s)', command=exctract_framework)
utils.add_command(label='Restore App Executable', command=restore_app_exec_backup)
toolmenu.add_cascade(label='Tweaks',menu=tweaks)
toolmenu.add_cascade(label='Utils',menu=utils)
toolmenu.add_command(label='Source Code', command=source_code)
main.config(menu=toolmenu)

main.mainloop()
