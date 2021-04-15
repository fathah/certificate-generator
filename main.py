from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys

# File source for the empty certificate
in_file = "certificate.jpg"
# Folder to genrate certificates
out_file = "output/" 

# Add all participant names in the following list
users = [
"Participant 1",
"Participant 2",
"Participant 3",
"Participant 4",
"Participant 5",
"Participant 6",
"Participant 7",
]

# Run a for loop through the participants list

for i in users:
    # Opening Image
    img = Image.open(in_file)
    # Setting up image to over-draw
    draw = ImageDraw.Draw(img)
    # Font style for the text // 80 is the size of font
    font = ImageFont.truetype('font.ttf', 80)
    # Drwaing text over the image. x=1500, y=1250 // (83, 46,  17) is the rgb value for the color of text
    draw.text((1500, 1250), i.upper(), (83, 46, 17), font=font)
    # Finally save the image
    img.save(out_file+i.upper()+".jpg")

    
