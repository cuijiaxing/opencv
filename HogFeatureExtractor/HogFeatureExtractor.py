import matplotlib.pyplot as plt
import cv2

from skimage.feature import hog
from skimage import data, color, exposure
from ImageClipper.FileNameFeeder import FileNameFeeder

class HogFeatureExtractor:

    @staticmethod
    def getHogFeature(inputImage):
        image = color.rgb2gray(inputImage)
        width, height = image.shape[:2]
        fd, hog_image = hog(image, orientations = 18, pixels_per_cell=(height, width),
                            cells_per_block = (1, 1), visualise=True)
        return fd


    @staticmethod
    def getFeatureListFromDir(inputDir):
        feeder = FileNameFeeder()
        fileNameList = feeder.getImageFiles(inputDir)
        return HogFeatureExtractor.getFeatureList(inputDir, fileNameList)


    @staticmethod
    def getFeatureList(inputDir, fileNameList):
        featureList = []
        for fileName in fileNameList:
            print inputDir + fileName
            image = cv2.imread(inputDir + fileName)
            feature = HogFeatureExtractor.getHogFeature(image)
            featureList.append(feature)
        return featureList




