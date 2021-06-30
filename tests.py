# A script to test the textbox generator

import textbox

features = textbox.Features()

fonts = features.listFonts()
backgrounds = features.listBackgrounds()

testLines = [
    "Test line one",
    "Test line two",
    "A slightly longer test line",
    "A test line that that is much longer than the last one",
    "a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9"
]

longLine = "This is a very long line that the code will have to split into multiple textboxes to make it work and fit all the text in"

outputFolder = "/tmp/"

for background in backgrounds :
    for font in fonts :
        print("background : " + background + "\nfont : " + font)
        features.setBackground(background)
        features.setFont(font)
        generator = textbox.Generate(features)
        generator.bulkMake(testLines, outputFolder)
        input("Array generating done, check " + outputFolder)
        generator.bulkMake(longLine, outputFolder)
        input("String generating done, check " + outputFolder)