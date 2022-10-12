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

happyHighIntensityErrors = 0
happyLowIntensityErrors = 0
sadHighIntensityErrors = 0
sadLowIntensityErrors = 0
angryHighIntensityErrors = 0
angryLowIntensityErrors = 0
fearfulHighIntensityErrors = 0
fearfulLowIntensityErrors = 0

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
happyerrors = 2
saderrors = 2
angryerrors = 2
fearfulerrors = 2
w, h = 480, 30
totalerrorsincrement = widthmain/24

widthmisattribute = 300
heightmisattribute = 16
errorsincrementmisattribute = 300/18

shape = [(0, 0), (widthmain, heightmain)]

happystartx = 0
happyendx = totalerrorsincrement * happyerrors 
sadstartx = happyendx
sadendx = sadstartx + (saderrors*totalerrorsincrement)
angrystartx = sadendx
angryendx = angrystartx + (angryerrors*totalerrorsincrement)
fearfulstartx = angryendx
fearfulendx = fearfulstartx + (fearfulerrors*totalerrorsincrement)

happyrectangle = [(0, 0), (happyendx , heightmain)]
sadrectangle = [(sadstartx,0),(sadendx,heightmain) ]
angryrectangle = [(angrystartx,0), (angryendx, heightmain)]
fearfulrectangle = [(fearfulstartx,0), (fearfulendx,heightmain)]
  
# creating new Image object
totalerrorsgraph = Image.new("RGB", (widthmain, heightmain),color = "#FFFFFF")

happycolor = "#00FF00"
sadcolor = "#0000FF"
angrycolor = "#FF0000"
fearfulcolor = "#FFFF00"
skippedcolor = "#666666"


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


# img  = Image.new( mode = "RGB", size = (width, height),color = (255,255,255) )
# ImageDraw.rectangle((0,10),(100,100), fill= "#ffffff", outline=None, width=1)

happyErrors = 0
sadErrors = 0
angryErrors = 0
fearfulErrors = 0

emotions = ['happy','sad','angry','fearful']

maingraphwidth = 

startx = 0

def misattributionsfrom(emotions):
    for i in emotions:
    graphend = eval(emotions[i] + 'Errors') + startx
    
    startx = graphend = eval(emotions[i] + 'Errors')
    
    'happy' + str(i) = 2