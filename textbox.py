import os

class Features :
    def __init__(self) :
        self.pwd = os.getcwd()
        self.backgroundsDirectory = os.path.join(self.pwd, "assets/backgrounds")
        self.fontsDirectory = os.path.join(self.pwd, "assets/fonts")

    def listBackgrounds(self) :
        list = os.listdir(self.backgroundsDirectory)
        return self.removeFileExt(list)

    def listFonts(self) :
        list = os.listdir(self.fontsDirectory)
        return self.removeFileExt(list)

    def removeFileExt(self, files) :
        for i in range(0, len(files)) :
            item = files[i-1]
            splitUp = item.split(".")
            splitUp.pop()
            files[i-1] = (".".join(splitUp))
        return files