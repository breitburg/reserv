'''
On Windows:
python setup.py build

On macOS:
python3 setup.py py2app
'''
import platform
from main import __version__ as VERSION

if platform.system() == "Windows":
    import sys
    from cx_Freeze import setup, Executable

    base = None
    if sys.platform == 'win32' : base = 'Win32GUI'

    opts = {'include_files' : ['resources/logo.png', 'resources/banner/ru.png', 'resources/done.png', 'resources/lang.py', 'resources/banner/en.png'], 'includes' : ['PyQt5', 'sip', 'requests', 'wget', 'zipfile', 'os']}

    setup(
    name = 'Reserv',
    version=VERSION,
    author = 'Upbits',
    options = {'build_exe' : opts},
    executables = [Executable('main.py', base = base, icon="win_icon.ico")]
    )
elif platform.system() == "Darwin":
    from setuptools import setup

    APP = ['main.py']
    DATA_FILES = ['resources/logo.png', 'resources/banner/ru.png', 'resources/done.png', 'resources/lang.py', 'resources/banner/en.png']
    OPTIONS = {'argv_emulation': True,
     'iconfile': 'mac_icon.icns',
     'includes': ['sip', 'PyQt5', 'wget', 'os', 'zipfile'],
     'packages': ['requests']
    }

    setup(
    name='Reserv',
    version=VERSION,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    )
else:
    print("Your system is not supported.")
