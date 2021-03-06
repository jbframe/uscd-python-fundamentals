#!/usr/bin/env python
# Assignment 5
# Final Project

# This final project is designed to incorporate all the tools learned throughout the course. You will need to create a class that handles image and audio processing methods. Follow the steps below to complete the project:

# 1. Name your class MMedia_Processing
# 2. You will be creating two methods. Name the first method ImgProc and the second AudProc
# 3. Method 1 will read the image file attached here download
# 4. Use the following libraries for your work import matplotlib.pyplot as plt and import matplotlib.image as mpimg
# 5. Use the mpimg imread method to read in the image file attached above
# 6. you can view the image by using plt.imshow(img) where img is the image read in
# 7. Color images are typically store as RGB files. So a color image is composed of three separate images concatenated; a Red component, and Green component and a Blue component. We will use the following to select the Red component - where 1 = R, 2 = G, 3 = B. So for img[:,  :, 1] this selects all the rows and all the columns of the first component. lum_img = img[:, :, 1]
# 8. View the new image and add a title using the imshow method
# 9. Plot a second image [your can use plt.figure(1) for the first plot, plt.figure(2) for the second and so on] that will show the histogram of the new image. Use the information below plt.hist(lum_img.ravel(), bins=256, range=(0.0, 255), fc='k', ec='k')
# 10. Add a grid, title, xlabel and ylabel to the plot.

# 11. Method 2 will read an audio file attached Alone-Sistar.wav download
# 12. Use the following libraries import matplotlib.pyplot as plt, import numpy as np and from scipy.io.wavfile import read, write
# 13 You will use the read method to read in the audio file as shown below where Fs stands for sampling rate and data is the data read in from the audio file. Fs, data = read('Alone-Sistar.wav')
# 14. Plot the data and title it Waveform of Test Audio. Label the Xaxis Sample Index and the Yaxis Amplitude
# 15. flip the entire data set around so that the track plays backwards. Save and write to a file using the write function.
# 16. To test out your code use any media player that supports wave files
# Submit your code, the plots, the image files and audio files for full credit. Have fun with this one.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy.io.wavfile import read, write

class MMedia_Processing():
  def ImgProc(self):
    img = mpimg.imread('BigDataImage-1.jpeg')
    plt.figure(1)
    plt.title('BigDataImage-1.jpeg')
    plt.imshow(img)
    # plt.show()
    lum_img = img[:,:,1]
    plt.figure(2)
    plt.title('Red component in BigDataImage-1.jpeg')
    plt.imshow(lum_img)
    plt.figure(3)
    plt.title('Histogram for red component in BigDataImage-1.jpeg')
    plt.ylabel('Number of Pixels')
    plt.xlabel('Intensity')
    plt.grid(True)
    plt.hist(lum_img.ravel(), bins=256, range=(0.0, 255), fc='k', ec='k')
    plt.show()

  def AudProc(self):
    samplerate, data = read('Alone-Sistar.wav')
    length = data.shape[0] / samplerate
    time = np.linspace(0., length, data.shape[0])
    plt.figure(4)
    plt.plot(time, data[:, 0], label="Left channel")
    plt.plot(time, data[:, 1], label="Right channel")
    plt.legend()
    plt.title('Waveform of Test Audio')
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    reverseData = np.flip(data,0)
    write('Alone-Sistar-reversed.wav', samplerate, reverseData)
    plt.figure(5)
    plt.plot(time, reverseData[:, 0], label="Left channel")
    plt.plot(time, reverseData[:, 1], label="Right channel")
    plt.legend()
    plt.title('Waveform of Test Audio Reversed')
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()


instanceOfMMedia_Processing = MMedia_Processing()
instanceOfMMedia_Processing.ImgProc()
instanceOfMMedia_Processing.AudProc()