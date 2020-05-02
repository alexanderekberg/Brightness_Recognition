# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""






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

# saved

class functions:
    # convert mp3 to spectogram
    def spectogram(filename, FolderForSpectogram):
        # to mel spectogram added to desktop
        y, sr = librosa.load('/Users/alex/desktop/Music/' + filename)
        save_path =  FolderForSpectogram + filename
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





    # convert 
    def convert(filename, Type):
        list_a = []
        image = load_img('/Users/alex/desktop/spectogram/' + filename)
        array_of_all_decibels = img_to_array(image)
        array_of_all_decibels_axis_2 = array_of_all_decibels[0:288,0:1152,0]
        upper_section = array_of_all_decibels_axis_2[0:288,0:1152]
    
        # delete all values under 100
        for index in range(288):
            for newindex in range(1151):
                if upper_section[index, newindex] < 100:
                    upper_section[index, newindex] = 0
            
            allvalues = np.sum(upper_section)
    
        # percentage appended to list
        # values percentage of beats section
        for index in range(288):
            percent_from_top = np.sum(upper_section[index]) / allvalues
            percent_from_top = percent_from_top * 100
            percent_equation = round(percent_from_top, 10)
            
            
            # List_a = 288 sections
            list_a.append([percent_equation])
        
        # if CNN then 288 sections - fix
        # 16 sections instead of 288
        # append first 16 values 18 times
        number1 = 0
        list_b = []
        for number in range(18):
            number1 = number1 + 16
            sum_of_16 = np.sum(list_a[number1:number1 + 16])
            list_b.append(sum_of_16)
            list_b = list_b[0:17]
        
        list_answer = []
            
        # add '-' values and convert to array
        for index2 in range(17):
            list_answer.append(-np.asarray(list_b[index2]))
    
        save_path = '/Users/alex/desktop/files_for_ANN/' + filename
        save_path = save_path[:-4]
    
    
        
    # Here fix memory of bunch of plots being saved to ram
        if Type == 'CNN':
            plt.figure(figsize=(16, 4))
            pylab.axis('off') # no axis
            pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
            plt.plot(list_answer)
            plt.savefig(save_path, bbox_inches=None, pad_inches=None)
        else:
            np.save(save_path,np.asarray(list_answer))
        return



    # add all converted percentages into one single array for ANN (make array smaller 0-10 maybe instead of 0-288)
    def single_file():
        os.chdir('/Users/alex/desktop/files_for_ANN/')
    
        # appending last 3 digits ex "100" to array
        for file in glob.glob("*.npy"):
        
            # last digits "400" etc
            last_3 = file[-7:-4]
            last_3 = float(last_3)
    
            # last 3 digits in name
            last_3 = np.array([last_3])
        
            # appending last 3 numbers into value and saving to "added_brightness"
            temp = np.load('/Users/alex/desktop/files_for_ANN/' + file)
            temp_1 = np.append(temp, last_3, 0)
            save_path = '/Users/alex/desktop/added_brightness/' + file
            np.save(save_path, temp_1)
        
            #   Load first file to use as first array value and appending last 3 to value
            array = np.load('/Users/alex/desktop/files_for_ANN/Nightcore - Day after day_400.npy')
            number = float(400)
            number = np.array([number])
            array = np.append(array, number, 0)
            array = np.array([array])
        

        # append all songs to the array above
        os.chdir('/Users/alex/desktop/files_for_ANN/')
        for file in glob.glob("*.npy"):
            song = np.load('/Users/alex/desktop/added_brightness/' + file)
            song = np.array([song])
            array = np.append(array, song, 0) 
    
        # delete first value of the array [0]
        # array = array[1:288]
        save_path = '/Users/alex/desktop/ANN_dataset_for_brightness'
        np.save(save_path, array)
        return




# Task
# Delete all files after usage (spectogram, .npy files etc.)

class AI:
    
    def Spectogram(FolderOfMusic, FolderForSpectogram):
        os.chdir(FolderOfMusic)
        for file in glob.glob("*.mp3"):
            functions.spectogram(file, FolderForSpectogram)
    def Type(FolderOfSpectogram, Type):
        os.chdir(FolderOfSpectogram)
        for file in glob.glob("*.png"):
            functions.convert(file, Type)
        
        if Type == 'ANN':
            functions.single_file()
        else:
            return


# making CNN or ANN files, grade mp3 with last 3 digits being a numbers 100-400
# type in functions from other class




# Runfile after typing in here

# ex ('/Users/alex/desktop/Music/', '/Users/alex/desktop/spectogram/')
AI.Spectogram('/Users/alex/desktop/Music/', '/Users/alex/desktop/spectogram/')

# ex ('/Users/alex/desktop/spectogram/','CNN')
AI.Type('/Users/alex/desktop/spectogram/','ANN')















