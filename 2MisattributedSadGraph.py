import os, sys
from PIL import Image, ImageDraw, ImageFont
import fillpdf
from fillpdf import fillpdfs

misattributedSadHappy = 6
misattributedSadAngry = 6
misattributedSadFearful = 6

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

# sadMisattributionsGraph.show()
sadMisattributionsGraph.save("sadMisattributions.jpg")

fillpdfs.place_image('sadMisattributions.jpg', 209, 544, '1happymisattributions.pdf', '2sadmisattributionstest.pdf', 1, width=283.5, height=15)