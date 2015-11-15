
from PIL import Image
import random
import randomImage

def get_seed(password):
    seed = 0
    for c in password:
        seed += ord(c)
    return seed


def num2rgba(num, rgba):
    i = lsb(num, rgba)
    return rgba[0:i] + (num,) + rgba[i + 1:3] + (rgba[3] - i,)


def rgba2num(rgb):
    i = 255 - rgb[3]
    print(i)
    return rgb[i]


def lsb(num, rgba):
    difference = [(x - num) ** 2 for x in rgba[0:3]]
    return difference.index(min(difference))


def get_length(pix, width, height):
    return pix[width - 1, height - 1][0]


def get_variables(image):
    return image.size[0], image.size[1], image.load()


def get_xy_loc(width, height, length):
    return random.sample(xrange(width - 2), length), random.sample(xrange(height - 2), length)


def encrypt(image, msg, password="123456789", output_name="encrypted.png"):
    random.seed(get_seed(password))
    if type(image) == str:
        image = Image.open(image).convert("RGB").convert("RGBA")

    width, height, pix = get_variables(image)
    length = len(msg)
    x_loc, y_loc = get_xy_loc(width, height, length)

    colors = [ord(c) for c in msg]

    for i in xrange(length):
        x, y, c = x_loc[i], y_loc[i], colors[i]
        pix[x, y] = num2rgba(c, pix[x, y])
    pix[width - 1, height - 1] = (length, length, length)
    image.save(output_name, "PNG")


def decrypt(image, password="123456789"):
    random.seed(get_seed(password))

    if type(image) == str:
        image = Image.open(image).convert("RGBA")

    width, height, pix = get_variables(image)
    length = get_length(pix, width, height)
    xLoc, yLoc = get_xy_loc(width, height, length)

    msg = ""
    for i in xrange(length):
        msg += chr(rgba2num(pix[xLoc[i], yLoc[i]]))
    return msg


