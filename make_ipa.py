import os
import shutil

print("Creating New ipa")
# Creating Zip Archive
shutil.make_archive("ppapp", 'zip', "App")

#re-naming file to.ipa
os.rename('ppapp.zip', 'ppapp.ipa')
shutil.rmtree("App")
print("Done.!")