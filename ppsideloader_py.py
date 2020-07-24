import os
from tkinter import ttk, Button, Label, Entry, Tk
import shutil
import zipfile

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

# UI
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
