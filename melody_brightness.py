# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



# This project is converting mel spectogram into clear readable for AI


# librosa
import matplotlib.pyplot as plt
import librosa
import librosa.display
import pylab

# image processing
import numpy as np
from keras.preprocessing.image import img_to_array, load_img

# file loading
import glob, os


def spectogram(filename):
    # to mel spectogram added to desktop
    y, sr = librosa.load('/Users/alex/desktop/Music/' + filename)
    save_path = '/Users/alex/desktop/spectogram/' + filename
    save_path = save_path[:-3]
    plt.figure(figsize=(16, 4))
    pylab.axis('off') # no axis
    pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[]) # Remove the white edge
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max, top_db=80.0)
    librosa.display.specshow(D, y_axis='mel')
    # if you want with decibel chart
    # plt.colorbar(format='%+3.0f dB')
    pylab.savefig(save_path, bbox_inches=None, pad_inches=None)
    pylab.close()
    return


def convert(filename):
    list_a = []
    image = load_img('/Users/alex/desktop/spectogram/' + filename)
    array_of_all_decibels = img_to_array(image)
    array_of_all_decibels_axis_2 = array_of_all_decibels[0:288,0:1152,0]
    upper_section = array_of_all_decibels_axis_2[0:288,0:1152]
    # delete all values under 100 in beats section
    for index in range(288):
        for newindex in range(1151):
            if upper_section[index, newindex] < 100:
                upper_section[index, newindex] = 0
            
    allvalues = np.sum(upper_section)
    # percentage appended to list (and printed)
    # values percentage of beats section
    for index in range(288):
        percent_from_top = np.sum(upper_section[index]) / allvalues
        percent_from_top = percent_from_top * 100
        percent_equation = round(percent_from_top, 10)
        list_a.append([percent_equation])
    list_answer = []
    for index2 in range(288):
        list_answer.append(-np.asarray(list_a[index2]))
    
    save_path = '/Users/alex/desktop/files_for_ANN/' + filename
    save_path = save_path[:-4]
    # Save to array
    np.save(save_path,np.asarray(list_answer))
    plt.figure(figsize=(16, 4))
    pylab.axis('off') # no axis
    pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
    plt.plot(list_answer)
    # Save to graph
    # plt.show()
    # plt.savefig(save_path, bbox_inches=None, pad_inches=None)
    return


# add all converted percentages into one single array and append brightness values
def single_file():
    os.chdir('/Users/alex/desktop/files_for_ANN/')
    for file in glob.glob("*.npy"):
        # 3 last letters of song name
        last_3 = file[-7:-4]
        last_3 = float(last_3)
        last_3 = np.array([[last_3]])
        # append 3 last letters to end of array
        temp = np.load('/Users/alex/desktop/files_for_ANN/' + file)
        temp_1 = np.append(temp, last_3, 0)
        save_path = '/Users/alex/desktop/added_brightness/' + file
        np.save(save_path, temp_1)
        # Convert all files in 'Files_for_ANN' to single array
        # add first value to array [0]
        # CHANGE THIS ARRAY TO 0 VALUES
        array = np.load("/Users/alex/desktop/added_brightness/Malumup - Navras_100.npy")
        array = np.swapaxes(array, 0, 1)
        # CHANGE THIS ARRAY TO 0 VALUES
        # append all songs to array
        os.chdir('/Users/alex/desktop/added_brightness/')
        for file in glob.glob("*.npy"):
            song = np.load("/Users/alex/desktop/added_brightness/" + file)
            swap = np.swapaxes(song, 0, 1)
            array = np.append(array, swap, 0)
    # delete first value of the array [0]
    array = array[1:288]
    save_path = '/Users/alex/desktop/ANN_dataset_for_brightness'
    np.save(save_path, array)
    return




# mp3 is taken from 'Music Folder' in desktop
# convert mp3 to spectogram, save to 'spectogram' folder
os.chdir("/Users/alex/desktop/Music/")
for file in glob.glob("*.mp3"):
    spectogram(file)

# convert spectogram to graph, save to 'files_for_ANN'
os.chdir("/Users/alex/desktop/spectogram/")
for file in glob.glob("*.png"):
    convert(file)

single_file()



