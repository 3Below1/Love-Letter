from distutils.core import setup
import py2exe
from PIL import Image

Image = Image.open("icon.png")
Image.save("icon.ico")

setup(
    console=[
        {
            "script": "Love.py", 
            "icon_resources": [(0, "icon.ico")]
        }
    ],
    zipfile = None,
)