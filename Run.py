import os
from SpecialDegredations import *
from SimpleDegredations import *

def run(txt, fontname, font_sizes, angles, degredations, revFlag, savePath):
    if revFlag == 1:
        path = savePath + 'Processed images - OUTPUT/' + txt[::-1]
    else:
        path = savePath + 'Processed images - OUTPUT/' + txt

    if not os.path.exists(path):
        os.makedirs(path)

    frame_w = 800
    frame_h = 800

    for size in font_sizes:
        for angle in angles:


            if fontname == "":
                font = ImageFont.truetype("Fonts/Arial.ttf", size)
            else:
                font = ImageFont.truetype("Fonts/" + fontname, size)
            w, h = font.getsize(txt)

            frame_w = w + h
            frame_h = h + w

            bg = Image.new('RGBA', (frame_w, frame_h), 'white')
            img = Image.new('RGBA', (frame_w, frame_h), 'white')

            yel_w, yel_h = img.size

            yel_bg = None #declare yal_bg
            if degredations[5] > 0:
                img = yellow(img, degredations[5], yel_w, yel_h)
                yel_bg = img
                yel_bg = yel_bg.convert('RGBA')

            draw = ImageDraw.Draw(img)
            draw.text(((frame_w - w) / 2, (frame_h - h) / 2), txt[::-1], font=font, fill="black", )

            im = img.rotate(angle)
            im = im.convert('RGBA')
            if degredations[5] > 0:
                im = Image.alpha_composite(yel_bg, im)
            else:
                im = Image.alpha_composite(img, im)


            if degredations[0] > 0:
                im = dissconection_spot(im, degredations[0], yel_bg)

            if degredations[1] > 0:
                im = overlapping_spot(im, degredations[1], yel_bg)

            if degredations[2] > 0:
                im = independent_spot(im, degredations[2], yel_bg)

            if degredations[3] > 0:
                im = noise(im, degredations[3], yel_bg)

            if degredations[4] > 0:
                im = blur(im, degredations[4])

            bg.paste(im, box=(0, 0))

            if revFlag == 1:
                bg.save(path + '/' + txt[::-1] + '_' + angle.__str__() + '_' + size.__str__() + '.png')
            else:
                bg.save(path + '/' + txt + '_' + angle.__str__() + '_' + size.__str__() + '.png')



