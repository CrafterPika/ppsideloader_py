import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

required_packages = ['os', 'requests', 'tkinter', 'webbrowser', 'shutil', 'zipfile', 'glob', 'plistlib', 'threading', 'time']
excluded_packages = ['numpy']
executables_settings = [
    Executable(
        "ppsideloader_py.py",
        base=base,
        icon = 'icon.ico',
        #shortcutName='ppsideloader_py',
        #shortcutDir='DesktopFolder',
    )
]
build_options = {
    "build_exe": {
        'packages': required_packages,
        'excludes': excluded_packages,
        'include_files': ['icon.ico', 'zsign.exe'],
    },
    'bdist_msi': {
        'upgrade_code': "{f3a5eb20-7045-4937-aad2-61be50141b85}",
        'add_to_path': True,
        #'environment_variables': [
            #("E_MYAPP_VAR", "=-*MYAPP_VAR", "1", "TARGETDIR")
        #]
    }
}

setup(  name = "PPSideloaderPy",
        version = "2.1",
        description = "Tweak apps easily",
        options = build_options,
        executables = executables_settings
)
