
# Project: predicting tone / mood of songs with artificial neural network

## Since mel spectograms tend to have an incredible number of different values coinciding it didnt seem like the best option for using for an ANN or CNN, much of information is hard to percieve. So i decided to convert spectogram into an array of percent of pitch dividing 22.000hz into 16 sections and counting sum of occurances in spectogram (sum of each section / total sum)

## Mel Spectogram
![Ivan Torrent - THE BOUNDS OF THE UNIVERSE_200](https://user-images.githubusercontent.com/59181775/80721741-dd754d80-8afe-11ea-81c1-1f8cd566c35e.png) <img width="9" alt="Screenshot 2020-05-09 at 11 50 08" src="https://user-images.githubusercontent.com/59181775/81470610-dda2d680-91eb-11ea-94ce-6e3c90c79fb5.png">


## Percentage decibel graph of array (22000hz on x axis, % on y axis)
![Malumup - Navras_100](https://user-images.githubusercontent.com/59181775/80723968-8f157e00-8b01-11ea-9cd7-7f7f27274296.png)

## Percentage decibel graph of array (22000hz on x axis, % on y axis)
![Nightcore - Day after day_400](https://user-images.githubusercontent.com/59181775/80723726-465dc500-8b01-11ea-81b0-7e13d75c1e5a.png)

## Single array of 42 mp3 files with 16 pitch sections of song
<img width="1300" alt="Screenshot 2020-05-07 at 10 57 03" src="https://user-images.githubusercontent.com/59181775/81276342-27a48480-9053-11ea-81d6-f249e1bbb542.png">

# Neural Network Statistic
## Accuracy on training (42 objects)
Epoch 1000/1000
42/42 [==============================] - 0s 163us/step - loss: 0.3876 - accuracy: 0.8274

## Accuracy on test set (12 objects)
<img width="403" alt="Screenshot 2020-05-07 at 13 22 11" src="https://user-images.githubusercontent.com/59181775/81289125-27fa4b00-9066-11ea-8e4e-22bb5d772ed4.png"> decoded: <img width="101" alt="Screenshot 2020-05-07 at 13 26 49" src="https://user-images.githubusercontent.com/59181775/81289399-a5be5680-9066-11ea-90d0-7a478cd32a91.png"> actual values: <img width="99" alt="Screenshot 2020-05-07 at 13 44 15" src="https://user-images.githubusercontent.com/59181775/81290825-051d6600-9069-11ea-9be4-d1242d4e7caa.png"> 

# Result
50% accuracy

# Improvements: more accurate and bigger dataset, power/db and number of values(calm songs)


