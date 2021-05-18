import os
import matplotlib.pyplot as plot
from scipy.io import wavfile

#This file converts the .wav files in Test and Train folders to .png files

def createSpec(num):

    #num= The digit which we are converting from .wav to .png
    wavPath = "Train/" + str(num) + "/"
    pngPath = "Trainimg/" + str(num) + "/"
    
    for f in os.listdir(wavPath):
        samplingFrequency, signalData = wavfile.read(wavPath+f)
        plot.subplot(212)
        plot.specgram(signalData,Fs=samplingFrequency)
        plot.xlabel('Time')
        plot.ylabel('Frequency')
        plot.savefig(pngPath+f[:-4], dpi=50, bbox_inches='tight', pad_inches=0)

        #plot.show() #shows the spectrograms

for i in range(0, 10):
    
    print("Start", i) #Just to track the progress, since it took a lot of time
    createSpec(i)
    print("Finish", i)