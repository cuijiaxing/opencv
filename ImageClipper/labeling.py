import cv2
import numpy as np
import cv
import os
from FileNameFeeder import FileNameFeeder

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



if __name__ == "__main__":
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)
    feeder = FileNameFeeder()
    inputDir = "images/"
    outputDir = "output/"
    makedir(outputDir)

    imageFileNames = feeder.getImageFiles(inputDir)
    for fileName in imageFileNames:
        inputImage = cv2.imread(inputDir + fileName)
        cv2.imshow("image", inputImage)
        #cv2.imshow('image', inputImage)
        keyValue = cv2.waitKey() & 0xFF
        if keyValue == ord('q'):
            break
        elif keyValue == 13:
            resultImage = inputImage[fixed_start_y : fixed_end_y, fixed_start_x : fixed_end_x, :]
            cv2.imwrite(outputDir + fileName, resultImage)
            break

    cv2.destroyAllWindows()
