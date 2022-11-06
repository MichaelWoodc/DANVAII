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

misattributedSadHappy = 1
misattributedSadAngry = 1
misattributedSadFearful = 1
misattributedAngryHappy = 1
misattributedAngrySad = 1
misattributedAngryFearful = 1
misattributedFearfulHappy = 1
misattributedFearfulSad = 1
misattributedFearfulAngry = 1
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
happyendx = (misattributedSadHappy * misattributionerrorsincrement) 
sadstartx = happyendx
sadendx = sadstartx # only since we're on the sad misattributions graph
angrystartx = sadendx
angryendx = angrystartx + (misattributedSadAngry * misattributionerrorsincrement)
fearfulstartx = angryendx
fearfulendx = fearfulstartx + (misattributedSadFearful*misattributionerrorsincrement)

happyrectangle = [(0, 0), (happyendx , heightmisattributions)]
angryrectangle = [(angrystartx,0), (angryendx, heightmisattributions)]
fearfulrectangle = [(fearfulstartx,0), (fearfulendx,heightmisattributions)]


  # creating new Image object
sadMisattributionsGraph = Image.new("RGB", (widthmisattributions, heightmisattributions),color = "#FFFFFF")

# create rectangle image for happy Errors
happyErrorsrectangle = ImageDraw.Draw(sadMisattributionsGraph)
angryErrorsrectangle = ImageDraw.Draw(sadMisattributionsGraph)
fearfulErrorsrectangle = ImageDraw.Draw(sadMisattributionsGraph)

happyErrorsrectangle.rectangle(happyrectangle, fill =happycolor, outline=None)
angryErrorsrectangle.rectangle(angryrectangle, fill =angrycolor, outline=None)
fearfulErrorsrectangle.rectangle(fearfulrectangle, fill =fearfulcolor, outline=None)

sadMisattributionsGraph.show()
sadMisattributionsGraph.save("sadMisattributions.jpg")