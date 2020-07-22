# ++sideloader_py
an python implementation of @eni9889's ppsideloader<br>
injecting/patching tweaks into apps by loading a library on the main app executable

# Requirements

- [Python v3.8.3](https://www.python.org/downloads/release/python-383/)

# How to use
1. Download [this repo](https://github.com/CrafterPika/ppsideloader_py/archive/master.zip)
2. Get an (decrypted) ipa from your app
3. Extract the .ipa and compress the content of "Payload/AppName.app/" (the inside of "AppName.app") to "app.zip"
4. Get your Tweak <code>.dylib</code> and compress to "Tweak.zip"
5. Extract the <code>ppsideloader_py-master.zip</a>
6. Copy both zips into the directory where all <code>.py</code>'s are
7. Open the "ppsiderloader_py.py"  with python
8. Click on "Extract Files", it will setup everything
9. Enter the App Exec name in the box and click on "Hex edit app"<br>
10. Click on "Creat IPA" and your ipa with the ++ tweak will be made.

# Credits
- <a href="https://github.com/eni9889">@eni9889</a> for <a href="https://github.com/eni9889/ppsideloader">The Original ppsideloader</a>
- <a href="https://github.com/julioverne/">@julioverne</a> for <a href="https://github.com/julioverne/libloader-sideloader">libloader</a>
- <a href="https://github.com/saurik/">@saurik</a> for CydiaSubstrate.framework
