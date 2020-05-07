
# Project: converting mel spectogram to "clearer info" to be passed to Artificial Neural Network
## Mel Spectogram
![Ivan Torrent - THE BOUNDS OF THE UNIVERSE_200](https://user-images.githubusercontent.com/59181775/80721741-dd754d80-8afe-11ea-81c1-1f8cd566c35e.png)

## Percentage decibel array (left graph being high pitch and right being low pitch)
![Malumup - Navras_100](https://user-images.githubusercontent.com/59181775/80723968-8f157e00-8b01-11ea-9cd7-7f7f27274296.png)

## Comparing to high pitch (brightness)
![Nightcore - Day after day_400](https://user-images.githubusercontent.com/59181775/80723726-465dc500-8b01-11ea-81b0-7e13d75c1e5a.png)

## Single array of 42 mp3 files
<img width="1300" alt="Screenshot 2020-05-07 at 10 57 03" src="https://user-images.githubusercontent.com/59181775/81276342-27a48480-9053-11ea-81d6-f249e1bbb542.png">


# Neural Network Statistic
## Accuracy on training (42 objects)
Epoch 1000/1000
42/42 [==============================] - 0s 163us/step - loss: 0.3876 - accuracy: 0.8274

## Accuracy on test set (12 objects)
## hotencoded array with index 0-3 being 100-400
<img width="403" alt="Screenshot 2020-05-07 at 13 22 11" src="https://user-images.githubusercontent.com/59181775/81289125-27fa4b00-9066-11ea-8e4e-22bb5d772ed4.png"> <img width="101" alt="Screenshot 2020-05-07 at 13 26 49" src="https://user-images.githubusercontent.com/59181775/81289399-a5be5680-9066-11ea-90d0-7a478cd32a91.png">

## Highest percent guess 1-4 being 100-400


# Result
50% accuracy

# Improvements: more accurate and bigger dataset, better analysis of what makes humans percieve as brightness since db(power) might be included and more factors like number of values in a song


