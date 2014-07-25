from sklearn import svm
from ImageClipper.FileNameFeeder import FileNameFeeder
from HogFeatureExtractor.HogFeatureExtractor import HogFeatureExtractor




class Classifier:

    def getTrainingData(inputDir, classLabel, outputFileName):
        featureList = HogFeatureExtractor.getFeatureListFromDir(inputDir)
        labelList = [classLabel for i in xrange(len(featureList))]
        outputFile = open(outputFileName)
        for i in xrange(len(featureList)):
            currentFeature = featureList[i]
            for value in currentFeature:
                outputFile.write(value)
                outputFile.write(" ")
            outputFile.write(labelList[i])
        outputFile.close()


    



if __name__ == "__main__":
    classifier = Classifier()

    #prepare for data analysis
    negativeDir = "positive/"
    positiveDir = "negative/"

    positiveFeatureList, positiveLabelList = getTrainingData(positiveDir, 1, "positive.csv")
    negativeFeatureList, negativeLabelList = getTrainingData(negativeDir, 0, "negative.csv")













