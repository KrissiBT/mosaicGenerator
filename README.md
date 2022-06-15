# mosaic Generator
program that generates pictures out of pictures

# Requirements
numpy
opencv_python
tqdm

# Workflow
if the picture you are working with you might want to start off by scaling it down
```sh
python3 scaleImage.py shroom.png
```
that should return 
```sh
image saved as scaled.png
```
now that you have a smaller image you can use that with the generator program
i have generated a picture map with an online picture set of anime faces [Link to that here](https://www.kaggle.com/datasets/splcher/animefacedataset)
the map file is called anime.json and the pictures are in a folder called anime
so in order to generate the mosaic you simply run:
```sh
python3 generator.py scaled.png anime.json anime/ 100 
```
the 100 here refferances to the fact that i want each picture in the mosaic to be 100x100 px 
# Warning
this program is very stupid and has no trouble generating image files that are many Gb's in size
when opencv tries to display such large files YOUR COMPUTER WILL CRASH

# Result
this 
![plot](shroom.png)
Turned to this
![plot](output/scaled_out.png)
