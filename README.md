# TMMC_Challenge_Software

## This repositiory contains our team's code for the Toyota Motor Manufacturing Company (TMMC) Innovation Challenge.

## Our Approach
We took 800 photos of the various testing stations with the holes covered in various ways. We then used ROBOFLOW to annotate around 200 picutes which contain the 6 classes that the program will identify. We then trained the dataset on these images and relied on a hybrid approach to annotate the rest of the images. We let the model annotate the miages and checked them visually before adding them to the dataset that we would use to retrain the mode.

## Results
We had over a 98% accuracy identifying the holes across various background colors(red, white and aluminum). We did struggle with identifying the stickers on a black background which we plan to fix by comparing the hue of the sticker and the background.

## Installation and Dependencies
Ultralytics
