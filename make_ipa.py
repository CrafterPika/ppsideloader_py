import os
import shutil

print("*** PPSideloader By CrafterPika ***")
print("*** Twitter: @CrafterPika ***")
print("*** License: none ***")
print("*** Source Code: https://github.com/CrafterPika/ppsideloader_py ***")
print("")

print("Creating New ipa")
# Creating Zip Archive
shutil.make_archive("ppapp", 'zip', "App")
shutil.rmtree("App")

#re-naming file to.ipa
os.rename('ppapp.zip', 'ppapp.ipa')
print("Done.!")