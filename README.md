# alien-invasion

Install PyInstaller from PyPI:
pip install pyinstaller

Python3 install
python3 -m pip install pyinstaller


To generate the bundle in a subdirectory called dist, go to your program’s directory and run:
pyinstaller yourprogram.py

Adding -F (or --onefile) parameter will pack everything into single "exe" without the need for any external package files/dependencies. Downside here is it would be hard for you program to act on certain files that are in specific external locations.
pyinstaller -F yourprogram.py

