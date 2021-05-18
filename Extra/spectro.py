import os
import matplotlib.pyplot as plot
from scipy.io import wavfile

wavPath = "5_george_15.wav"
pngPath = "5_george_15"
    
samplingFrequency, signalData = wavfile.read(wavPath)

plot.subplot(211)
plot.title('Spectrogram of a wav file with piano music')
plot.plot(signalData)
plot.xlabel('Sample')
plot.ylabel('Amplitude')

plot.subplot(212)
plot.specgram(signalData,Fs=samplingFrequency)
plot.xlabel('Time')
plot.ylabel('Frequency')

plot.savefig(pngPath, dpi=4000, bbox_inches='tight', pad_inches=0)
plot.show()