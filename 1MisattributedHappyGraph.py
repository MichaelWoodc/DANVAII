import os, sys
from PIL import Image, ImageDraw, ImageFont
import fillpdf
from fillpdf import fillpdfs


# Draws a rounded rectangle.

# PARAMETERS:
# xy – Two points to define the bounding box. Sequence of either [(x0, y0), (x1, y1)] or [x0, y0, x1, y1]. The second point is just outside the drawn rectangle.

# radius – Radius of the corners.

# outline – Color to use for the outline.

# fill – Color to use for the fill.

# width – The line width, in pixels.

# This is a begin experiment comment in the code section of the readymessage section

misattributedHappySad = 6
misattributedHappyAngry = 6
misattributedHappyFearful = 6
misattributedHappySkipped = 6

misattributedSadHappy = 6
misattributedSadAngry = 6
misattributedSadFearful = 6
misattributedAngryHappy = 6
misattributedAngrySad = 6
misattributedAngryFearful = 6
misattributedFearfulHappy = 6
misattributedFearfulSad = 6
misattributedFearfulAngry = 6
total = 24

# Let's define colors before creating images
happycolor = "#00FF00"
sadcolor = "#0000FF"
angrycolor = "#FF0000"
fearfulcolor = "#FFFF00"

widthmisattributions = 350
heightmisattributions = 16

misattributionerrorsincrement = widthmisattributions/18

shape = [(0, 0), (widthmisattributions, heightmisattributions)]

happystartx = 0
happyendx = (0) # only since we're on the happy misattributions graph
sadstartx = happyendx
sadendx = sadstartx + (misattributedHappySad*misattributionerrorsincrement)
angrystartx = sadendx
angryendx = angrystartx + (misattributedHappyAngry*misattributionerrorsincrement)
fearfulstartx = angryendx
fearfulendx = fearfulstartx + (misattributedHappyFearful*misattributionerrorsincrement)

happyrectangle = [(0, 0), (happyendx , heightmisattributions)]
sadrectangle = [(sadstartx,0),(sadendx,heightmisattributions) ]
angryrectangle = [(angrystartx,0), (angryendx, heightmisattributions)]
fearfulrectangle = [(fearfulstartx,0), (fearfulendx,heightmisattributions)]


  # creating new Image object
happyMisattributionsGraph = Image.new("RGB", (widthmisattributions, heightmisattributions),color = "#FFFFFF")

# create rectangle image for happy Errors
happyErrorsrectangle = ImageDraw.Draw(happyMisattributionsGraph)
sadErrorsrectangle = ImageDraw.Draw(happyMisattributionsGraph)
angryErrorsrectangle = ImageDraw.Draw(happyMisattributionsGraph)
fearfulErrorsrectangle = ImageDraw.Draw(happyMisattributionsGraph)

sadErrorsrectangle.rectangle(sadrectangle, fill =sadcolor, outline=None)
angryErrorsrectangle.rectangle(angryrectangle, fill =angrycolor, outline=None)
fearfulErrorsrectangle.rectangle(fearfulrectangle, fill =fearfulcolor, outline=None)

# happyMisattributionsGraph.show()
happyMisattributionsGraph.save("happyMisattributions.jpg")



fillpdfs.place_image('happyMisattributions.jpg', 209, 512.8, '1happymisattributions.pdf', '1happymisattributionstest.pdf', 1, width=283.5, height=15)