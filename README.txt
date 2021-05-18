This CNN model aims to classify audio files (.wav format) of digits 0-9.

It is a pre-loaded model with a few sample inputs (10) to test it on, as the complete dataset was too big to upload.
The pre-loaded model is stored in "model.h5" and loaded in "savedModel.py".

The purpose of "createSpectro.py" was just to convert the .wav files to .png files so that they could be fed into the model for training/ testing.

It is trained in the file "CNN.py" which should not be run now as the original training and testing folders have not been 
uploaded due to size issues. It stored the trained model in "model.h5".
The dataset used was taken from "https://github.com/Jakobovski/free-spoken-digit-dataset", it provides 3000 files, out of which,
2400 files (with ending index 0-39) were used to train it and the remaining 600 files (with index 40-49) were 
used to test it, yielding these results:	"loss: 0.2425 - accuracy: 0.9354 - val_loss: 0.7589 - val_accuracy: 0.7900"


Out of the 600 files, 1 random file of each digit is included in "SmallWav/" and a .png of the corresponding spectrogram is stored
in "SmallTest/". Running "savedModel.py" uses these files to predict and prints the percentage of files correctly predicted at the end.


(The original dataset had .wav files in a folder called "Train/" and and the corresponding .png files were stored in "Trainimg/". Similarly, for "Test/".)


"Extra/" contains a program, "sort.py" that wasn't directly related to the model but was useful nonetheless,
and a program, "spectro.py" that makes a spectrogram of a file, a .wav file, and it's spectrogram.


Some links I referred to:

https://www.coursera.org/learn/introduction-tensorflow/home/welcome
https://pythontic.com/visualization/signals/spectrogram
https://machinelearningmastery.com/save-load-keras-deep-learning-models/
tensorflow and keras documentation,
and stackexchange and google in general