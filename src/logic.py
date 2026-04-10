import json
import hashlib
import pathlib, zipfile
import crossfiledialog as cfd

class Logic():
    def __init__(self):
        pass

    def open_file(self):
        filename = cfd.open_file()
        if filename:
            print(f"Selected: {filename}")

    
