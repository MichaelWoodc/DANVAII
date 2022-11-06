import os, sys
from PIL import Image, ImageDraw, ImageFont



# Draws a rounded rectangle.
# PARAMETERS:
# xy – Two points to define the bounding box. Sequence of either [(x0, y0), (x1, y1)] or [x0, y0, x1, y1]. The second point is just outside the drawn rectangle.
# radius – Radius of the corners.

# outline – Color to use for the outline.

# fill – Color to use for the fill.

# width – The line width, in pixels.

# This is a begin experiment comment in the code section of the readymessage section

misattributedHappySad = 3
misattributedHappyAngry = 3
misattributedHappyFearful = 3
misattributedHappySkipped = 6

misattributedSadHappy = 0
misattributedSadAngry = 0
misattributedSadFearful = 0
misattributedSadSkipped = 0

misattributedAngryHappy = 0
misattributedAngrySad = 0
misattributedAngryFearful = 0
misattributedAngrySkipped = 0

misattributedFearfulHappy = 1
misattributedFearfulSad = 1
misattributedFearfulAngry = 1
misattributedFearfulSkipped = 1
total = 24

# Let's define colors before creating images
happycolor = "#00FF00"
sadcolor = "#0000FF"
angrycolor = "#FF0000"
fearfulcolor = "#FFFF00"
skippedcolor = "#666666"

widthmisattributions = 350
heightmisattributions = 16
misattributionerrorsincrement = widthmisattributions/18
shape = [(0, 0), (widthmisattributions, heightmisattributions)]

happystartx = 0
happyendx = (misattributedFearfulHappy * misattributionerrorsincrement) 
sadstartx = happyendx
sadendx = sadstartx + (misattributedFearfulSad*misattributionerrorsincrement)
angrystartx = sadendx
angryendx = angrystartx + (misattributedFearfulAngry*misattributionerrorsincrement)
fearfulstartx = angryendx
fearfulendx = fearfulstartx # because we are making the fearful graph


happyrectangle = [(0, 0), (happyendx , heightmisattributions)]
sadrectangle = [(sadstartx,0),(sadendx,heightmisattributions) ]
angryrectangle = [(angrystartx,0), (angryendx, heightmisattributions)]
fearfulrectangle = [(fearfulstartx,0), (fearfulendx,heightmisattributions)]


  # creating new Image object
fearfulMisattributionsGraph = Image.new("RGB", (widthmisattributions, heightmisattributions),color = "#FFFFFF")

# create rectangle image for happy Errors
happyErrorsrectangle = ImageDraw.Draw(fearfulMisattributionsGraph)
sadErrorsrectangle = ImageDraw.Draw(fearfulMisattributionsGraph)
angryErrorsrectangle = ImageDraw.Draw(fearfulMisattributionsGraph)

happyErrorsrectangle.rectangle(happyrectangle, fill =happycolor, outline=None)
sadErrorsrectangle.rectangle(sadrectangle, fill =sadcolor, outline=None)
angryErrorsrectangle.rectangle(angryrectangle, fill =angrycolor, outline=None)

fearfulMisattributionsGraph.show()
fearfulMisattributionsGraph.save("fearfulMisattributions.jpg")