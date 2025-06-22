import os
import json

os.chdir("c:\\Users\\elchr\\Desktop\\chrabz.github.io\\music")

musiclist = os.listdir()


os.chdir("c:\\Users\\elchr\\Desktop\\chrabz.github.io")

with open("musiclist.js", 'w', encoding='utf-8') as f:
    f.write("const musicFiles = ")
    f.write(json.dumps(musiclist, indent=4))
    f.write(";")