import cv2
import numpy as np
import os
import json
#create a function that returns the average color of an image
def avg_colors(img):
    try:
    #get the colors of the image
        #colors = cv2.split(img)
        #scale the image to 100x100 to see the avg color when it is squared
        img = cv2.resize(img, (100,100))
        #get the average color of the image
        avg_color_per_row = np.average(img, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        #return the average color and filename in a list object
    except:
        avg_color = {[0,0,0]}
        print("failed processing image")
    return avg_color

map = []
#convert list to json string
def list_to_json(list):
    return json.dumps(list)

def processImage(path):
    picks = os.listdir(path)
    for pick in picks:
        print(pick)
        #open the image
        imga = cv2.imread(path + pick)
        data = avg_colors(imga)
        map.append([data[0],data[1],data[2],pick])




#---------------------------------------- Program starts here ---------------------------------------------------

pathToPictures = "pictures/"
outputFileName = "pics.json"

processImage(pathToPictures)
open(outputFileName, "w").write(list_to_json(map))
#ist_to_json(map)
