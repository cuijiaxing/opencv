from os import listdir
from os.path import isfile, join

class FileNameFeeder:
    def getFiles(self, inputDir):
        onlyfiles = [f for f in listdir(inputDir) if isfile(join(inputDir, f))]
        return onlyfiles

    def getImageFiles(self, inputDir):
        fileNameList = self.getFiles(inputDir)
        extensionList = ["png", "bmp", "jpg", "jpeg"]
        fileNameList = [f for f in fileNameList if f[f.find(".") + 1:] in extensionList]
        return fileNameList

'''
if __name__ == "__main__":
    feeder = FileNameFeeder()
    print feeder.getImageFiles(".")
'''
