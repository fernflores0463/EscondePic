from PIL import Image
import random


def getSeed(password):
    seed = 0;
    for c in password:
        seed += ord(c)
    return seed;


def num2RGB(num, initalRGBA):
    i = lsb(num,initalRGBA)
    return initalRGBA[0:i] + (num,) + initalRGBA[i+1:3] + (initalRGBA[3]-i,)


def RGB2num(rgb):
    i = 255-rgb[3]
    return (rgb[i])

def lsb(num, RGBA):
    difference = [(x-num)**2 for x in RGBA[0:3]]
    return difference.index(min(difference))

def getLength(pix, width, height):
    return pix[width - 1, height - 1][0]


def getVariables(picture):
    image = Image.open(picture).convert("RGBA")
    return image, image.size[0], image.size[1], image.load()


def getXYLocs(width, height, length):
    return random.sample(xrange(width - 2), length), random.sample(xrange(height - 2), length)


def encrypt(picture, msg, password="123456789", outputName="encrypted.png"):
    random.seed(getSeed(password))

    image, width, height, pix = getVariables(picture)
    length = len(msg)
    xLoc, yLoc = getXYLocs(width, height, length)

    colors = [ord(c) for c in msg]

    for i in xrange(length):
        x, y, c = xLoc[i], yLoc[i], colors[i]
        pix[x, y] = num2RGB(c, pix[x, y])
    pix[width - 1, height - 1] = (length, length, length)
    image.save(outputName, "PNG")


def decrypt(picture, password="123456789"):
    random.seed(getSeed(password))

    image, width, height, pix = getVariables(picture)
    length = getLength(pix, width, height)
    xLoc, yLoc = getXYLocs(width, height, length)

    msg = ""
    for i in xrange(length):
        msg += chr(RGB2num(pix[xLoc[i], yLoc[i]]))
    return msg


## test

encrypt("cat.jpg", "a" * 255, outputName="regular.png")

print (decrypt("regular.png"))
