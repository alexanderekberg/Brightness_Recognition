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




# Pitch and decibel make up a song
# Pitch percent makes a song brightness
# Number of values make a song fast
# Decibel count makes a song power





class functions:
    
    def spectogram(folderOfMusic, FolderForSpectogram):
        os.chdir(folderOfMusic)
        for file in glob.glob("*.mp3"):
            y, sr = librosa.load(folderOfMusic + file)
            save_path =  FolderForSpectogram + file
            save_path = save_path[:-3]
            plt.figure(figsize=(16, 4))
            pylab.axis('off')
            pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
            D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max, top_db=80.0)
            librosa.display.specshow(D, y_axis='mel')
            pylab.savefig(save_path, bbox_inches=None, pad_inches=None)
            pylab.close()
        return



    def append_value(folderOfSpectogram, folderOfDataset, dataset_name, has_grade):
        os.chdir(folderOfSpectogram)
        
        # make empty array with 18 sections
        array = np.array([[]])
        array = np.resize(array,(0,18))
        
        
        for file in glob.glob("*.npy"):
            # updating .npy file to have a grade (only on true)
            if has_grade == 'true':
                last_3 = float(file[-7:-4])
                last_3 = np.array([last_3])
                temp = np.load(folderOfSpectogram + file)
                temp_1 = np.append(temp, last_3, 0)
                save_path = folderOfSpectogram + file
                np.save(save_path, temp_1)
            
            # updating dataset to have name (only on false)
            elif has_grade == 'false':
                name = np.asarray([file[:-4]])
                temporary = np.load(folderOfSpectogram + file)
                temporary_1 = np.append(temporary, name, 0)
                save_path_1 = folderOfSpectogram + file
                np.save(save_path_1, temporary_1)
                
            # append everything to array
            song = np.load(folderOfSpectogram + file)
            song = np.array([song])
            array = np.append(array, song, 0)
                
        # add (hasValue) or (noValue) to name
        name = dataset_name
        if has_grade == 'true':
            name = name + '(hasValue)'
        elif has_grade == 'false':
            name = name + '(noValue)'
            
            
        # save array(dataset) to folderOfDataset
        save_path = folderOfDataset + name
        np.save(save_path, array[:])
        return



    def pitch_percent(folderOfMusic, folderOfSpectogram, folderOfDataset, dataset_name, has_grade):
        
        functions.spectogram(folderOfMusic, folderOfSpectogram)
        
        # arrays of image and removing any irrelevant info
        os.chdir(folderOfSpectogram)
        for file in glob.glob("*.png"):
            list_a = []
            image = load_img(folderOfSpectogram + file)
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
            for index in range(288):
                percent_from_top = np.sum(upper_section[index]) / allvalues
                percent_from_top = percent_from_top * 100
                percent_equation = round(percent_from_top, 10)
                list_a.append([percent_equation])
        
        
            # converting array of 288 columns to 16 columns
            # faster fix: make spectogram 16 pixel height
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
    
            save_path = folderOfSpectogram + file
            save_path = save_path[:-4]
            
            np.save(save_path,np.asarray(list_answer))
            
        functions.append_value(folderOfSpectogram, folderOfDataset, dataset_name, has_grade)
        
        # Fix
        # delete everything in spectogram folder after dataset has been created
        # for files in glob.glob('/Users/alex/desktop/spectogram/'):
            # os.remove(files)
        return






# true = training or evaluating dataset
# false = real dataset


# returns dataset with names(noValue) or grades(hasValue) from music chosen                                         # Dataset name    # Has_Value
functions.pitch_percent('/Users/alex/desktop/Music/','/Users/alex/desktop/spectogram/','/Users/alex/desktop/dataset/','evaluating_dataset','true')















