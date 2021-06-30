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

outputFolder = "/tmp/"

for background in backgrounds :
    for font in fonts :
        features.setBackground(background)
        features.setFont(font)
        generator = textbox.Generate(features)
        generator.bulkMake(testLines, outputFolder)
        input("Generating done, check " + outputFolder)