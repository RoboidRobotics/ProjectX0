# REFRENCED CODE:
#   https://www.datacamp.com/community/tutorials/face-detection-python-opencv
#
# DATE: October 12th, 2021
# DESCRIPTION: This program is meant to provide facial-recognition capabilities to the rest of the project.
#
# DEPENDENCIES:
#   OpenCV | pip install opencv-python \\For computer vision
#   matplotlib | pip install -U matplotlib \\For testing
#   numpy | pip install numpy \\For matrix manipulation


__opencv_version__ = r'4.1.1'

import sys
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

print(cv.__file__)
if(__opencv_version__ != cv.__version__):
    print('WARNING: The OpenCV version being used ({}) is different from the OpenCV version this module was written in! ({})'.format(cv.__version__, __opencv_version__))

__training_xml__ = cv.data.haarcascades + 'haarcascade_frontalface_default.xml'
__cascade__ = cv.CascadeClassifier(__training_xml__) #load the already-trained facial-recongition model


#specify which detection model to use
def use_model(cascade):
    __cascade__ = cascade

#given an image and a scale factor, find faces in an image and return that image with rectangles around the faces
def detect_faces(image):
    image_gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY) #create a grayscale copy of the image (used for face detection)

    #find the faces.
    #** scaleFactor is a parameter specifying how much the image size is reduced at each image scale.
    #** minNeighbors is a parameter specifying how many neighbors each candidate rectangle should have to retain it.
    faces_rects = __cascade__.detectMultiScale(image_gray, scaleFactor = 1.3, minNeighbors = 6)

    #print how many faces were found
    print('Faces found: {}'.format(len(faces_rects)))

    #creates variables needed to check for largest box
    size = 0
    xf = 0
    yf = 0
    wf = 0
    hf = 0

    #loops through each recorded face
    for (x,y,w,h) in faces_rects:

        #if data is largest, store in variables
        if size < (w*h):
            size = (w*h)
            xf = x
            yf = y
            wf = w
            hf = h

        #draws a red rectangle with a thickness of 2
    cv.rectangle(image, (xf, yf), (xf + wf, yf + hf), (0, 0, 255), 2)
    return image

username = "dickless dennis"

# Using camera
cap = cv.VideoCapture(0) # The Parameter is the index of the camera
while 1:
    ret, image = cap.read()  # Read each frame as an image
    # test_image = cv.imread(image)
    result_image = detect_faces(image)  # detect the faces

    # #show the image and waits for a key press before exiting
    cv.imshow('Detected Faces', result_image)
    key = cv.waitKey(1) #waits for 2 milliseconds for a key press on a OpenCV window
    if key == 113: # it breaks when q is pressed
        break

    elif key == 32:

        stringname = f"{username}_facerecog.jpg"
        cv.imwrite(stringname, image)
        print("Picture recorded, verification in process")
        break


cap.release()
cv.destroyAllWindows()


# FOR TESTING (code is run only when called from command line)
# if __name__ == '__main__':
#     import sys
#     test_image = cv.imread(sys.argv[1])  #load the image from the file specified from the command line
#     result_image = detect_faces(test_image)  #detect the faces
#     # #show the image and waits for a key press before exiting
#     cv.imshow('Detected Faces', result_image)
#     cv.waitKey(0)
#     cv.destroyAllWindows()

# For testing from code
# image = r'/Users/rediettadesse/Documents/GitHub/ProjectX0/image2.jpeg' #image full path
# test_image =  cv.imread(image) #load the image from the file specified from the command line
# result_image = detect_faces(test_image)  #detect the faces
# #show the image and waits for a key press before exiting

# cv.imshow('Detected Faces', result_image)
# # print(cv.waitKey(0))
# cv.waitKey(0)
# cv.destroyAllWindows()
