import os
from PIL import Image, ImageFont, ImageDraw

class Features :
    font = None
    background = None

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

    def setBackground(self, choice) :
        if choice not in self.listBackgrounds() :
            raise NameError("Background does not exist")
        
        self.background = os.path.join(self.backgroundsDirectory, choice + ".png")

    def setFont(self, choice) :
        if choice not in self.listFonts() :
            raise NameError("Font does not exist")
        
        self.font = os.path.join(self.fontsDirectory, choice + ".ttf")

class Generate :
    def __init__(self, features) :
        if features.font == None or features.background == None :
            raise ValueError("Either font or background is not set on features")
        
        self.features = features

    def make(self, text, outputPath) :
        img = Image.open(self.features.background)
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype(self.features.font, 32)
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((180, 15),text,(255,255,255),font=font)
        img.save(outputPath)

    def bulkMake(self, lines, outputFolder) :
        boxNumber = 1
        for each in lines :
            print(each)
            self.make(each, os.path.join(outputFolder, str(boxNumber) + ".png"))
            boxNumber += 1

def wrapFunction(text, length) :
    # If you pass text to the function which is to long it will break the function,
    # this function allows you to check if the text is too long and put new lines 
    # in between each line
    pass # yeah do this, i just dont want vs code to whine