import io, os
from PIL import Image, ImageDraw, ImageFont

font_path = os.path.join(os.path.dirname(__file__) , "fonts", "OpenSans-Regular.ttf")

font = ImageFont.truetype(font_path, 12)
label = "Kilroy was here!"


# Use getbbox to get the bounding box of the text
bbox = font.getbbox(label)
w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]

print(f"Width: {w}, Height: {h}")


print (label)
