import glob
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random, copy

bg_list = []
for filename in glob.glob('AntiquePaper/*.jpg'):
    im = Image.open(filename)
    bg_list.append(im)

def blur(image, val):
    im = image
    img = im.convert('RGBA')

    radius = val/10
    im2 = img.filter(ImageFilter.GaussianBlur(radius))

    return im2

def yellow(image, val, yel_w, yel_h):
    yel = random.choice(bg_list)
    yel = yel.resize((yel_w, yel_h), Image.ANTIALIAS)
    yel2 = yel.convert('RGBA')
    im = image.convert('RGBA')
    val = val / 100
    if val >= 0.9:
        val = 0.9

    ret = Image.blend(im, yel2, val)

    return ret

def noise(image, strong, bg):

    if strong >= 0 and strong <= 30:
        strong = 40

    elif strong >= 31 and strong <=50:
        strong = 30

    elif strong >= 51 and strong <= 60:
        strong = 20

    elif strong >= 61 and strong <= 70:
        strong = 15
    elif strong >= 71 and strong <=89:
        strong = 8
    else:
        strong = 5

    width, height = image.size
    blackPix = (0, 0, 0)
    whitePix = (255, 255, 255)
    grayPix = (128, 128, 128)

    img_bg = None

    # gets background
    if(bg is not None): #bg is antique image
        img_bg = copy.deepcopy(bg)
    else:               #bg is white
        img_bg = copy.deepcopy(image)
        pix_img_bg = img_bg.load()
        for x in range(0, width):
            for y in range(0, height):
                if pix_img_bg[x, y] != whitePix:
                    pix_img_bg[x, y] = whitePix

    pix_bg = img_bg.load()
    img_tmp = image
    pix_tmp = img_tmp.load()


    # convert image to binary
    thresh = 100
    fn = lambda x: 255 if x > thresh else 0
    image = image.convert('L').point(fn, mode='1')

    pix = image.load()
    flag = False

    for x in range(0, width):
        for y in range(0, height):
            if pix[x,y] != 0:
                rand = random.randint(0,103-strong)
                if rand == 0:
                    pix[x, y] = 0
                    pix_tmp[x, y] = blackPix
                elif rand == 1:
                    pix_tmp[x, y] = grayPix
                else:
                    pix_tmp[x,y] = pix_bg[x, y]
            else:
                rand2 = random.randint(0,103-strong)
                if rand2 == 0:
                    pix_tmp[x, y] = pix_bg[x, y]

    return img_tmp