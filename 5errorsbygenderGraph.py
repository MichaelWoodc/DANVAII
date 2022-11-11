import os, sys
from PIL import Image, ImageDraw, ImageFont
import fillpdf
from fillpdf import fillpdfs

maleTotalErrors = 12
femaleTotalErrors = 12

# Let's define colors before creating images
happycolor = "#00FF00"
sadcolor = "#0000FF"
angrycolor = "#FF0000"
fearfulcolor = "#FFFF00"
skippedcolor = "#666666"
malecolor = "#0000FF"
femalecolor = "#FF0000"

widthgendererrors = 350
heightmisattributions = 18
errorsincrementgender = 350/24
gendererrorsincrement = widthgendererrors/24

malestartx = 0
maleendx = malestartx + (maleTotalErrors * errorsincrementgender) 
femalestartx = maleendx
femaleendx = femalestartx + (femaleTotalErrors * errorsincrementgender)

malerectangle = [(0, 0), (maleendx , heightmisattributions)]
femalerectangle = [(femalestartx,0),(femaleendx,heightmisattributions) ]



# creating new Image object
genderErrorsGraph = Image.new("RGB", (widthgendererrors, heightmisattributions),color = "#FFFFFF")

# create rectangle image for happy Errors
maleTotalErrorsrectangle = ImageDraw.Draw(genderErrorsGraph)
femaleTotalErrorsrectangle = ImageDraw.Draw(genderErrorsGraph)


maleTotalErrorsrectangle.rectangle(malerectangle, fill =malecolor, outline=None)
femaleTotalErrorsrectangle.rectangle(femalerectangle, fill =femalecolor, outline=None)



genderErrorsGraph.save("errorsbygender.jpg")
fillpdfs.place_image('errorsbygender.jpg',209, 691, '5errorsbygender.pdf', '5errorsbygendertest.pdf', 1, width=283.5, height=15)