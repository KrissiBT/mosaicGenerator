
import cv2
import numpy as np
import json
from tqdm import tqdm
import os
import random 
clear = lambda: os.system('clear')

import sys

#list of colors that have been found and one variable that doesnt ever trigger
preFoundColours = [[[1337,0,0], "fatChanse"],[[1337,0,0], "fatChanse"]]


#==========================================================================================
#create an function that concatenates a matrix of images
def concatenate(matrix,pixelSize):
    imi = np.zeros([1,(len(matrix[0])*pixelSize),3],dtype=np.uint8)
    for line in tqdm(matrix):        
        l = np.concatenate((line), axis=1)
        imi = np.concatenate((l, imi), axis=0)
    return imi

#=================== create an custom demensional matrix of images
def createRandomMatrix(xx,yy):
    map = json.loads(open("face.json").read())      
    pickist = []
    line = []
    for x in range(yy):
        line = []
        for y in range(xx):
            filename = picturePath + map[random.randint(0,len(map)-1)][3]
            f = cv2.imread(filename)
            #resize the image
            f = cv2.resize(f, (100,100))
            line.append(f)
        pickist.append(line)
    return pickist


#create a function that finds the most similar color in a map of colors
def findSimilarColor(color, map):
    #print(color)
    #check if the color is already in preFoundColours
    for i in preFoundColours:
        if str(color) == (str(i[0])):
            return i[1]
    #create a list of the differences between the color and each color in the map
    
    differences = []
    for x in map:
        differences.append(abs(x[0]-color[0]) + abs(x[1]-color[1]) + abs(x[2]-color[2]))
    #find the index of the smallest difference
    index = differences.index(min(differences))
    #return the color at that index
    preFoundColours.append(map[index][3])
    preFoundColours.append([color, map[index][3]])
    return map[index][3]


#create a function the returns the average color of an image
def avg_color(img):
    try:
        #get the colors of the image
        #colors = cv2.split(img)
        img = cv2.resize(img, (100,100))
        #get the average color of the image
        avg_color_per_row = np.average(img, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        #return the average color and filename in a list object
    except:
        avg_color = {[0,0,0]}
        print("failed processing image")
    return avg_color

#======================== take in a picture and return a list of the most similar colors per pixel
def findSimilarColors(img, map, pixelSize,picturePath):
    otp = []
    for line in tqdm(img):
        l = []
        for pixel in tqdm(line):
            m = cv2.imread(picturePath+findSimilarColor(pixel, map))
            m = cv2.resize(m, (pixelSize,pixelSize))
            l.append(m)
        otp.append(l)
        clear()
    return otp





def display(img, name):
    cv2.imshow(name, img)
    



clear()


#---------------------------------------- Program starts here ---------------------------------------------------


inputFile = "test.png"
colorMap = "pics.json"
pictureDirectory = "pictures/"
ps = 100# define the size of each pixel image

mynd  = cv2.imread(inputFile) #image to be used

map = json.loads(open(colorMap).read())#map of color images

otp = findSimilarColors(mynd,map,ps,pictureDirectory) #function that loops through each picture and asembles a np array of the most similar pictures
print("rendering image")
ut = concatenate(np.flip(otp,0),ps)# asembles the lines of the image togeather and flips the image so that the top is the bottom
display(ut, "normal")

# #resize the image to a reasonable size
#ut = cv2.resize(ut, (int(ut.shape[1]/5),int(ut.shape[0]/5)))

outPutFileName = inputFile.split(".")[0] + "_out."+inputFile.split(".")[1]
cv2.imwrite(outPutFileName, ut)
cv2.imshow("input",mynd)
cv2.waitKey(0)

