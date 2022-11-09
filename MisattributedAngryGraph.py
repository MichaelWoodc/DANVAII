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


happyErrors = 0
sadErrors = 0
angryErrors = 0
fearfulErrors = 0

misattributedHappySad = 3
misattributedHappyAngry = 3
misattributedHappyFearful = 3
misattributedHappySkipped = 6

misattributedSadHappy = 0
misattributedSadAngry = 0
misattributedSadFearful = 0
misattributedAngryHappy = 3
misattributedAngrySad = 3
misattributedAngryFearful = 4
misattributedFearfulHappy = 4
misattributedFearfulSad = 3
misattributedFearfulAngry = 2
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

widthmain = 480
heightmain = 30
widthmisattributions = 300
heightmisattributions = 18
totalerrorsincrement = widthmain/24

widthmisattributions = 300
heightmisattributions = 18
errorsincrementmisattribute = 300/18
misattributionerrorsincrement = widthmisattributions/18

shape = [(0, 0), (widthmain, heightmain)]

happystartx = 0
happyendx = (happyErrors * totalerrorsincrement)
sadstartx = happyendx
sadendx = sadstartx + (sadErrors * totalerrorsincrement)
angrystartx = sadendx
angryendx = angrystartx + (angryErrors * totalerrorsincrement)
fearfulstartx = angryendx
fearfulendx = fearfulstartx + (fearfulErrors * totalerrorsincrement)

happyrectangle = [(0, 0), (happyendx , heightmain)]
sadrectangle = [(sadstartx,0),(sadendx,heightmain) ]
angryrectangle = [(angrystartx,0), (angryendx, heightmain)]
fearfulrectangle = [(fearfulstartx,0), (fearfulendx,heightmain)]
  
# creating new Image object
totalerrorsgraph = Image.new("RGB", (widthmain, heightmain),color = "#FFFFFF")




# create rectangle image for happy errors
happyerrorsrectangle = ImageDraw.Draw(totalerrorsgraph)
saderrorsrectangle = ImageDraw.Draw(totalerrorsgraph)
angryerrorsrectangle = ImageDraw.Draw(totalerrorsgraph)
fearfulerrorsrectangle = ImageDraw.Draw(totalerrorsgraph)

happyerrorsrectangle.rectangle(happyrectangle, fill =happycolor, outline=None)
saderrorsrectangle.rectangle(sadrectangle, fill =sadcolor, outline=None)
angryerrorsrectangle.rectangle(angryrectangle, fill =angrycolor, outline=None)
fearfulerrorsrectangle.rectangle(fearfulrectangle, fill =fearfulcolor, outline=None)

totalerrorsgraph.show()
totalerrorsgraph.save("totalerrorgraph.jpg")


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

angryMisattributionsGraph.show()
angryMisattributionsGraph.save("angryMisattributions.jpg")

fillpdfs.place_image('fearfulMisattributions.jpg', 100, -18, 'completed3.pdf', 'completed4.pdf', 2, width=500, height=50) 
# os.startfile('completed4.pdf')

fillpdfs.write_fillable_pdf('completed4.pdf', 'completed5.pdf', data_dict, flatten=False)
os.startfile('completed5.pdf')