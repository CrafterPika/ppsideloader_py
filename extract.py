import os
import shutil
import zipfile

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