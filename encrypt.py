import random
from PIL import Image


def encrypt(msg, picture, password="123456789", outputName="encrypted.png"):
    # basic encryption mech
    seed = 0;
    for c in password: seed += ord(c)
    random.seed(seed)
    image = Image.open(picture)
    width, height = image.size
    pix = image.load()

    length = len(msg)

    xLocations = random.sample(xrange(width - 1), length)
    yLocations = random.sample(xrange(height - 1), length)
    colors = []

    for c in msg:
        colors.append(ord(c))
    for i in xrange(length):
        x = xLocations[i]
        y = yLocations[i]
        c = colors[i]
        pix[x, y] = (c, c*x%255, c*y%255)

    pix[width-1,height-1] = (length,length,length)
    image.save(outputName,"PNG")

def decrypt(picture, password):
    msg = ""
    seed = 0;
    for c in password: seed += ord(c)
    random.seed(seed)

    image = Image.open(picture)
    width, height = image.size
    pix = image.load()

    length = pix[width-1,height-1][0]

    xLocations = random.sample(xrange(width -1), length)
    yLocations = random.sample(xrange(height -1), length)

    for i in xrange(length):
        msg += chr(pix[xLocations[i], yLocations[i]][0])
        print(xLocations[i],yLocations[i],pix[xLocations[i],yLocations[i]][0])
    print(msg)
