from sklearn import svm
from ImageClipper.FileNameFeeder import FileNameFeeder
from HogFeatureExtractor.HogFeatureExtractor import HogFeatureExtractor




class Classifier:

    @staticmethod
    def getTrainingData(inputDir, classLabel, outputFileName):
        featureList = HogFeatureExtractor.getFeatureListFromDir(inputDir)
        labelList = [classLabel for i in xrange(len(featureList))]
        outputFile = open(outputFileName, "w")
        if len(featureList) > 0:
            length = len(featureList[0])
            for i in xrange(length - 1):
                outputFile.write(str(i))
                outputFile.write(" ")
            outputFile.write("label\r\n")
        for i in xrange(len(featureList)):
            currentFeature = featureList[i]
            for value in currentFeature:
                outputFile.write(str(value))
                outputFile.write(" ")
            outputFile.write(str(labelList[i]))
            outputFile.write("\r\n")
        outputFile.close()
        print "finished extracting features"


    



if __name__ == "__main__":
    classifier = Classifier()

    #prepare for data analysis
    negativeDir = "negative/"
    positiveDir = "positive/"

    Classifier.getTrainingData(positiveDir, 1, "positive.csv")

    Classifier.getTrainingData(negativeDir, 0, "negative.csv")













