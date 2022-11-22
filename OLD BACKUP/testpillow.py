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
happyErrors = 3
sadErrors = 2
angryErrors = 1
fearfulErrors = 4
skippedErrors = 3

misattributedHappySad = 0
misattributedHappyAngry = 0
misattributedHappyFearful = 0
misattributedSadHappy = 0
misattributedSadAngry = 0
misattributedSadFearful = 0
misattributedAngryHappy = 0
misattributedAngrySad = 0
misattributedAngryFearful = 0
misattributedFearfulHappy = 0
misattributedFearfulSad = 0
misattributedFearfulAngry = 0

total = 24

widthmain = 480
heightmain = 30
widthmisattributions = 300
heightmisattributions = 18

w, h = 480, 30
totalErrorsincrement = widthmain/24

widthmisattributions = 300
heightmisattributions = 18
Errorsincrementmisattribute = 300/18

shape = [(0, 0), (widthmain, heightmain)]

happystartx = 0
happyendx = (totalErrorsincrement * happyErrors) 
sadstartx = happyendx
sadendx = sadstartx + (sadErrors*totalErrorsincrement)
angrystartx = sadendx
angryendx = angrystartx + (angryErrors*totalErrorsincrement)
fearfulstartx = angryendx
fearfulendx = fearfulstartx + (fearfulErrors*totalErrorsincrement)
skippedstartx = fearfulendx
skippedendx = skippedstartx + (skippedErrors*totalErrorsincrement)

happyrectangle = [(0, 0), (happyendx , heightmain)]
sadrectangle = [(sadstartx,0),(sadendx,heightmain) ]
angryrectangle = [(angrystartx,0), (angryendx, heightmain)]
fearfulrectangle = [(fearfulstartx,0), (fearfulendx,heightmain)]
skippedrectangle = [(skippedstartx,0), (skippedendx,heightmain)]

# Let's define colors before creating images
happycolor = "#00FF00"
sadcolor = "#0000FF"
angrycolor = "#FF0000"
fearfulcolor = "#FFFF00"
skippedcolor = "#666666"
  
# creating new Image object
totalErrorsgraph = Image.new("RGB", (widthmain, heightmain),color = "#FFFFFF")

# create rectangle image for happy Errors
happyErrorsrectangle = ImageDraw.Draw(totalErrorsgraph)
sadErrorsrectangle = ImageDraw.Draw(totalErrorsgraph)
angryErrorsrectangle = ImageDraw.Draw(totalErrorsgraph)
fearfulErrorsrectangle = ImageDraw.Draw(totalErrorsgraph)
skippedErrorsrectangle = ImageDraw.Draw(totalErrorsgraph)

happyErrorsrectangle.rectangle(happyrectangle, fill =happycolor, outline=None)
sadErrorsrectangle.rectangle(sadrectangle, fill =sadcolor, outline=None)
angryErrorsrectangle.rectangle(angryrectangle, fill =angrycolor, outline=None)
fearfulErrorsrectangle.rectangle(fearfulrectangle, fill =fearfulcolor, outline=None)
skippedErrorsrectangle.rectangle(skippedrectangle, fill =skippedcolor, outline=None)

totalErrorsgraph.show()


# img  = Image.new( mode = "RGB", size = (width, height),color = (255,255,255) )
# ImageDraw.rectangle((0,10),(100,100), fill= "#ffffff", outline=None, width=1)
