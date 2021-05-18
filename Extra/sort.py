import os
import shutil

""" This program was used to move the .wav files from the 
    downloaded file to different Train and Test folders"""

for i in range(0,10):
    path = "Trainimg/"+ str(i) + "/"
    moveto = "Testimg/"
    files = os.listdir(path)
    files.sort()
    for f in files:
        for i in range(0,5):
            s="4"+str(i)
            if s in f:
                src = path+f
                dst = moveto+str(f[0])+"/"
                shutil.move(src, dst)