import cv2
import sys

#createa a function that takes in an image file and shows it downscaled
def showImage(img,scale):
    #scale the image down to a reasonable size
    img = cv2.resize(img, (int(img.shape[1]/scale),int(img.shape[0]/scale)))
    cv2.imshow("image"+str(img.shape), img)
    cv2.imwrite("scaled.png",img)
    cv2.waitKey(0)


#if no sysarg are given, display instructions
if len(sys.argv) < 3:
    print("Usage: python3 showImage.py <image file> <scale>")
    print("scale refers to a fraction of the original image size")
    sys.exit()

#load in image
#get system arguments
mynd = cv2.imread(sys.argv[1])
scale = sys.argv[2]
showImage(mynd,int(scale))
print("image saved as scaled.png")
