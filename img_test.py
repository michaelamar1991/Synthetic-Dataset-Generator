import os
from PIL import Image, ImageFont, ImageDraw


def run(txt, fontname, font_sizes, angles):
    path = '/Users/michaelamar/Desktop/img_processing/' + txt
    if not os.path.exists(path):
        os.makedirs(path)

    frame_w = 400
    frame_h = 200

    for size in font_sizes:
        for angle in angles:
            bg = Image.new('RGBA', (frame_w, frame_h), 'white')
            img = Image.new('RGBA', (frame_w, frame_h), 'white')

            # font = ImageFont.truetype("/Library/Fonts/"+fontname, size)
            font = ImageFont.truetype("/Users/michaelamar/Downloads/re/" + fontname, size)
            w, h = font.getsize(txt)

            draw = ImageDraw.Draw(img)
            draw.text(((frame_w - w) / 2, (frame_h - h) / 2), txt, font=font, fill="black", )

            im = img.rotate(angle, fillcolor='white')

            bg.paste(im, box=(0, 0))
            bg.save(path + '/' + txt + '_' + angle.__str__() + '_' + size.__str__() + '.png')



