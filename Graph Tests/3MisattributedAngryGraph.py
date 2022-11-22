import os, sys
from PIL import Image, ImageDraw, ImageFont
import fillpdf
from fillpdf import fillpdfs

misattributedAngryHappy = 6
misattributedAngrySad = 6
misattributedAngryFearful = 6

# Let's define colors before creating images
happycolor = "#00FF00"
sadcolor = "#0000FF"
angrycolor = "#FF0000"
fearfulcolor = "#FFFF00"
skippedcolor = "#666666"

widthmisattributions = 350
heightmisattributions = 15
misattributionerrorsincrement = widthmisattributions/18
shape = [(0, 0), (widthmisattributions, heightmisattributions)]

widthmisattributions = 350
heightmisattributions = 18
misattributionerrorsincrement = widthmisattributions/18

happystartx = 0
happyendx = happystartx + (misattributedAngryHappy * misattributionerrorsincrement) 
sadstartx = happyendx
sadendx = sadstartx + (misattributedAngrySad * misattributionerrorsincrement)
angrystartx = sadendx
angryendx = angrystartx # only since we're on the Angry misattributions graph
fearfulstartx = angryendx
fearfulendx = fearfulstartx + (misattributedAngryFearful * misattributionerrorsincrement)

happyrectangle = [(0, 0), (happyendx , heightmisattributions)]
sadrectangle = [(sadstartx,0),(sadendx,heightmisattributions) ]
fearfulrectangle = [(fearfulstartx,0), (fearfulendx,heightmisattributions)]


# creating new Image object
angryMisattributionsGraph = Image.new("RGB", (widthmisattributions, heightmisattributions),color = "#FFFFFF")

# create rectangle image for happy Errors
happyErrorsrectangle = ImageDraw.Draw(angryMisattributionsGraph)
sadErrorsrectangle = ImageDraw.Draw(angryMisattributionsGraph)
fearfulErrorsrectangle = ImageDraw.Draw(angryMisattributionsGraph)

happyErrorsrectangle.rectangle(happyrectangle, fill =happycolor, outline=None)
sadErrorsrectangle.rectangle(sadrectangle, fill =sadcolor, outline=None)
fearfulErrorsrectangle.rectangle(fearfulrectangle, fill =fearfulcolor, outline=None)

angryMisattributionsGraph.save("angryMisattributions.jpg")
fillpdfs.place_image('angryMisattributions.jpg',-2, 646, 'blankDocument.pdf', '3angrymisattributionstest.pdf', 2, width=283.5, height=15)