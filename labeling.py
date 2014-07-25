import cv2
import numpy as np
import cv
import os
import sys
from ImageClipper.FileNameFeeder import FileNameFeeder
from HogFeatureExtractor.HogFeatureExtractor import HogFeatureExtractor
import matplotlib.pyplot as plt

fixed_start_x = 0
fixed_start_y = 0
fixed_end_x = 0
fixed_end_y = 0

start_x = 0
start_y = 0
end_x = 0
end_y = 0
hasPressed = False
inputImage = np.zeros((512, 512, 3), np.uint8)
image_output_count = 0
def draw_circle(event, x, y, flags, param):
    global start_x
    global start_y
    global end_x
    global end_y
    global hasPressed
    global inputImage
    global fixed_start_x
    global fixed_start_y
    global fixed_end_x
    global fixed_end_y
    global image_output_count
    if event == cv2.EVENT_LBUTTONDOWN:
        hasPressed = True
        start_x = x
        start_y = y
    elif event == cv2.EVENT_LBUTTONUP:
        end_x = x
        end_y = y
        fixed_start_x = start_x
        fixed_start_y = start_y
        fixed_end_x = end_x
        fixed_end_y = end_y
        hasPressed = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if hasPressed:
            end_x = x
            end_y = y
            tempImage = np.copy(inputImage)
            cv2.rectangle(tempImage, (start_x, start_y), (end_x, end_y), (255, 255, 255), 1)
            cv2.imshow('image', tempImage)
            print start_x, start_y, end_x, end_y

def makedir(path):
    try:
        os.stat(path)
    except:
        os.mkdir(path)


def showHogImage(inputImage):
    features = HogFeatureExtractor.getHogFeature(inputImage);
    #print features
    #plt.bar(np.arange(len(features)), features, 1.0, color='r')
    #plt.show()
    #plt.close()
    #print len(features)





if __name__ == "__main__":
    cv2.namedWindow('image')
    cv2.namedWindow('hog')
    cv2.setMouseCallback('image', draw_circle)
    feeder = FileNameFeeder()
    inputDir = "images/"
    outputDir = "output/"
    makedir(outputDir)

    imageFileNames = feeder.getImageFiles(inputDir)
    for fileName in imageFileNames:
        image_output_count = 0
        inputImage = cv2.imread(inputDir + fileName)
        cv2.imshow("image", inputImage)
        while True:
            keyValue = cv2.waitKey() & 0xFF
            if keyValue == ord('q'):
                sys.exit(0)
            elif keyValue == ' ':
                resultImage = inputImage[fixed_start_y : fixed_end_y, fixed_start_x : fixed_end_x, :]
                dot_index = fileName.find(".")
                outputFileName = outputDir + fileName[0:dot_index] + "_" + str(image_output_count) + fileName[dot_index:]
                cv2.imwrite( outputFileName , resultImage)
                image_output_count += 1
                cv2.imshow('image', inputImage)
                showHogImage(inputImage)
            elif keyValue == 13:
                break


    cv2.destroyAllWindows()
