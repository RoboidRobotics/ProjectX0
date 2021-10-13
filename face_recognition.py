# AUTHOR: Nicholas Thor Page
# REFRENCED CODE:
#   https://www.datacamp.com/community/tutorials/face-detection-python-opencv
# CONTACT:
#   thor@thepages.net
#   npage2@gmu.edu
#   +1-434-218-8241 (text preferred)
#
# DATE: October 12th, 2021
# DESCRIPTION: This program is meant to provide facial-recognition capabilities to the rest of the project.
#
# DEPENDENCIES:
#   OpenCV | pip install opencv-python


__opencv_version__ = r'4.1.1'


import cv2 as cv
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
    image_copy = image.copy() #create a copy of the image so we can draw on it
    image_gray = cv.cvtColor(image_copy, cv.COLOR_RGB2GRAY) #create a grayscale copy of the image (used for face detection)

    #find the faces.
    #TODO: NOTE: Not entirely sure how 'scaleFactor' and 'minNeighbors' affect this operation.
    faces_rects = __cascade__.detectMultiScale(image_gray, scaleFactor = 1.2, minNeighbors = 5)

    #print how many faces were found
    #print('Faces found: {}'.format(len(faces_rects)))

    #draw rectangles around the bounds of the detected faces
    for (x,y,w,h) in faces_rects:
        #draws a red rectangle with a thickness of 2
        cv.rectangle(image_copy, (x,y), (x+w, y+h), (0, 0, 255), 2)

    #show the image with rectangles around the detected faces
    #cv.imshow('Detected Faces', image_copy)
    #cv.waitKey(0)
    return image_copy













# FOR TESTEING (code is run only when called from command line)
if __name__ == '__main__':
    import sys


    test_image = cv.imread(sys.argv[1]) #load the image from the file specified from the command line
    result_image = detect_faces(test_image) #detect the faces

    #show the image and waits for a key press before exiting
    cv.imshow('Detected Faces', result_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
