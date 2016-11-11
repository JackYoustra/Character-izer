import PIL
import re
from PIL import Image, ImageFont, ImageDraw, ImageChops
from string import ascii_lowercase
import matplotlib.font_manager


def imageToWeights(image):
    weightlist = []
    width, height = image.size
    for x in range(width):
        for y in range(height):
            weight = image.getpixel((x, y))
            weightlist.append(weight)
    return weightlist

def trim(im, borderColor=255.0):
    bg = Image.new(im.mode, im.size, (255))
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

def imageFromPath(letter, fontPath):
    m = re.search("\\\\[^\\\\]*\\.", fontPath)
    fontName = m.group(0)[2:-1]
    #print(fontName)
    font = ImageFont.truetype(fontPath, 48)
    img = Image.new("L", (48, 56), 255) # 8 bit greyscale
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), letter, font=font)
    draw = ImageDraw.Draw(img) #this is off-center, not sure if this is a problem. EDIT: It is
    img = trim(img)
    #img.save(fontName + "_" + letter + ".png")
    if img == None:
        return None
    img.thumbnail((5, 7), PIL.Image.ANTIALIAS)
    normSizeImage = Image.new("L", (5,7))
    normSizeImage.paste(img, (0, 0, img.width, img.height))
    assert normSizeImage.width == 5 and normSizeImage.height == 7
    #img.save("thumb_" + fontName + "_" + letter + ".png")
    return normSizeImage


# try 5x7
# returns map between letter and image
def load():
    fontPaths = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
    letterImage = {}
    for letter in ascii_lowercase:
        fontImages = []
        for fontPath in fontPaths:
            img = imageFromPath(letter, fontPath)
            if img == None:
                continue
            fontImages.append(img)
            #img.save(fontName + "_ " + letter + ".png")
        letterImage[letter] = fontImages
    return letterImage
        
#if __name__ == "__main__":
 #   load()