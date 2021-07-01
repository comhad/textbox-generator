import os
import inspect
from typing import NewType
from PIL import Image, ImageFont, ImageDraw

class Features :
    font = None
    background = None
    avatar = None

    def __init__(self) :
        pwd = inspect.getfile(self.__class__) # this gets the full file path
        path = pwd.split("/") # assume linux
        path.pop() # remove file name
        self.pwd = "/".join(path) # this is just the folder path
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

    def setAvatar(self, choice) : # this is the file path
        if not os.path.isfile(choice) :
            raise FileNotFoundError("That avatar could not be found")
        self.avatar = choice

    def setFont(self, choice) :
        if choice not in self.listFonts() :
            raise NameError("Font does not exist")
        
        self.font = os.path.join(self.fontsDirectory, choice + ".ttf")

class Generate :
    wrapAt = 18 # the character limit per line
    fontSize = 40
    drawPos = (180, 15) # the pixels on the image to start drawing the text at
    textColor = (255, 255, 255) # the color of the text
    maxBoxSize = 60 # the max characters that can be fit into a box, need to know so we can seperate them
    avatarAt = (15, 5) # the pos to draw the avatar at
    avatarSize = (130, 130) # avatar size in x and y

    def __init__(self, features) :
        if features.font == None or features.background == None :
            raise ValueError("Either font or background is not set on features")
        
        self.features = features

    def make(self, text, outputPath) :
        text = wrapText(text, self.wrapAt)
        img = Image.open(self.features.background)
        if self.features.avatar :
            avatar = Image.open(self.features.avatar)
            avatar = avatar.resize(self.avatarSize)
            img.paste(avatar, self.avatarAt)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(self.features.font, self.fontSize)
        draw.text(self.drawPos, text, self.textColor, font=font)
        img.save(outputPath)

    def bulkMake(self, lines, outputFolder) :
        if isinstance(lines, str) : # if the argument is a string we want to split it (if we need to)
            splitLines = wrapText(lines, self.maxBoxSize)
            lines = splitLines.split("\n")
            # its a dirty reuse, but it works
        boxNumber = 1
        for each in lines :
            self.make(each, os.path.join(outputFolder, str(boxNumber) + ".png"))
            boxNumber += 1

def wrapText(text, length) :
    # If you pass text to the function which is to long it will break the function,
    # this function allows you to check if the text is too long and put new lines 
    # in between each line
    splitText = text.split(" ")
    wrappedLines = [""]
    lineNumber = 0
    while len(splitText) > 0 :
        word = splitText.pop(0) # remove the word from the text and add it to the list
        wrappedLines[lineNumber] += word + " "
        if len(wrappedLines[lineNumber]) > length : # if the line is too long, remove the last word
            wrappedLines[lineNumber] = wrappedLines[lineNumber][0:len(wrappedLines[lineNumber])-len(word)-1]
            lineNumber += 1
            wrappedLines.append(word + " ")
    
    newText = ("\n".join(wrappedLines))
    return newText