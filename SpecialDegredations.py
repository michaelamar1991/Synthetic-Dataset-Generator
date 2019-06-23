import random, copy
from PIL import ImageChops


def dissconection_spot(image, strong, bg):

    strong = 100 - ((strong % 55) + 11)

    width, height = image.size
    blackPix = (0, 0, 0)
    whitePix = (255, 255, 255)
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
    p = strong  # (55-full cut, 10-half cut)

    for x in range(0, width):
        for y in range(0, height):
            if (pix[x, y] != 0):
                flag = False
                continue
            if (pix[x, y] == 0 and pix[x - 1, y] != 0 and flag == False and random.randint(0, p) == 0):
                i, j = x, y
                rand = random.randint(0, 1)
                while (pix[i, j] == 0):
                    pix[i, j] = 255
                    pix_tmp[i, j] = pix_bg[i, j]
                    if(random.randint(0,4) != 2 ):
                        pix_tmp[i, j - 1] = pix_bg[i, j - 1]
                    if (rand == 1):
                        c1 = random.randint(0, 7)
                        if(c1 == 0):
                            i += 1
                            j += random.randint(0, 1)
                        elif(c1 == 1):
                            j += 1
                            i += random.randint(0, 1)
                        else:
                            i += 1
                            j += 1
                    else:
                        c2 = random.randint(0, 7)
                        if(c2 == 0):
                            i += 1
                            j -= random.randint(0, 1)
                        elif(c2 == 1):
                            j -= 1
                            i += random.randint(0, 1)
                        else:
                            i += 1
                            j -= 1

                    # prevents index exception
                    if i >= width or j >= height:
                        flag = True
                        break

                    if (pix[i, j] == 255 and p <= 10):
                        pix[i, j] = 0
                        pix_tmp[i, j] = blackPix
                        flag = True
                        break
                    elif p <= 10:
                        pix[i, j] = 255
                        pix_tmp[i, j] = pix_bg[i, j]
                        if (random.randint(0, 4) != 2):
                            pix_tmp[i, j-1] = pix_bg[i, j-1]
                flag = True

    return img_tmp


def independent_spot(image, strong, bg):
    image1 = independent_spot2(image, strong, bg)
    return independent_spot1(image1, strong, bg)


def independent_spot1(image, strong, bg):

    strong = 100 - ((strong % 55) + 11)

    width, height = image.size
    blackPix = (0, 0, 0)
    whitePix = (255, 255, 255)
    img_bg = None
    spots_amount = random.randint(2,6)


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
    p = strong  # (55-full cut, 10-half cut)

    c=0 # count the amount of spots
    for x in range(0, width):
        for y in range(0, height):

            #disperse spots
            if(c == int(spots_amount/2) and x <= int(width/2)):
                continue

            # prevents index exception
            if x+1 >= width or y >= height:
               break

            if (pix[x, y] != 0):
                flag = False
                continue

            elif(pix[x, y] == 0 and pix[x + 1, y] != 0 and flag == False):
                i, j = x, y
                i += 1

                count = 0
                steps = 40

                # right searching.
                while(flag == False and count != steps):
                    if(count+i >= width):
                        break
                    if(pix[i+count, j] != 0):
                        count += 1
                    else:
                        if count >= 30:
                            count = 0
                            break
                        else:
                            flag = True
                            count = 0
                            break
                    if count+1 == steps:
                        flag = True

                # if right searching didn't success then break
                if flag == True:
                    flag = False
                    continue
                else: # if its limit of spots > return image
                    if(c<=spots_amount):
                        c+=1
                    else:
                        return img_tmp

                # make the spot
                count = 0
                j -= 1 # for independency
                while(count != 5):
                    rand1 = random.randint(4, 5)
                    rand2 = random.randint(9, 10)
                    for a in range(rand1, rand2):
                        if (pix[i + a, j] == 0 or pix[i+a-2 , j-2] == 0  or
                                pix[i+a+2, j-2] == 0 or pix[i+a+1, j] == 0 or
                                pix[i+a-1, j-1] == 0 or pix[i+a+1, j] == 0 or
                                pix[i+a-1, j] == 0 or pix[i+a-2, j] == 0 or
                                pix[i+rand1-2, j-1] == 0 or pix[i+rand2 +2, j-1] == 0):
                            break
                        pix[i + a, j] = 0
                        pix[i + a + 1, j] = 0
                        pix[i + a + 2, j] = 0
                        pix_tmp[i + a, j] = blackPix
                        pix_tmp[i + a + 1, j] = blackPix
                        pix_tmp[i + a + 2, j] = blackPix
                    j -= 1
                    count += 1

                # return img_tmp

    return img_tmp


def independent_spot2(image, strong, bg):

    spot_counter = 0

    strong += 60

    width, height = image.size
    blackPix = (0, 0, 0)
    whitePix = (255, 255, 255)
    img_bg = None

    # gets background
    if(bg is not None): #bg is antique image
        img_bg = copy.deepcopy(bg)
    else:  #bg is white
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
    p = strong  # (55-full cut, 10-half cut)

    for _ in range(0, strong):
        x = random.randint(10, width-10)
        y = random.randint(10, height-10)

        if (pix[x, y] != 0):
            flag = False
            continue

        for i in range (x, x+8):
            for j in range(y, y+8):
                if(pix[i,j] != 0):
                    flag = True
                    break

            if flag == True:
                break

        if flag == True:
            flag = False
            continue

        else: # make spot
            r1 = random.randint(x+1, x+3)
            r2 = random.randint(x+4, x+6)
            j = y+2
            n = y+6
            while(j != n):
                for i in range(r1, r2):
                    if(i>=width or j>=height): # prevent index out of range
                        break
                    pix[i,j] = 255
                    pix_tmp[i,j] = pix_bg[i, j]
                    if(random.randint(0,1) == 0):
                        pix_tmp[i, j-1] = pix_bg[i, j-1]
                j += 1
            spot_counter += 1
    return img_tmp


def overlapping_spot(image, strong, bg):

    strong = 100 - ((strong % 55) + 11)

    width, height = image.size
    blackPix = (0, 0, 0)
    whitePix = (255, 255, 255)
    img_bg = None
    spots_amount = random.randint(2, 6)

    # gets background
    if (bg is not None):  # bg is antique image
        img_bg = copy.deepcopy(bg)
    else:  # bg is white
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
    p = strong  # (55-full cut, 10-half cut)

    c = 0  # count the amount of spots
    for x in range(0, width):
        for y in range(0, height):

            #disperse spots
            if(c == int(spots_amount/2) and x <= int(width/2)):
                continue

            # prevents index exception
            if x + 1 >= width or y >= height:
                break

            if (pix[x, y] != 0):
                flag = False
                continue

            elif (pix[x, y] == 0 and pix[x + 1, y] != 0 and flag == False):
                i, j = x, y
                i += 1

                count = 0
                steps = 40

                # right searching.
                while (flag == False and count != steps):
                    if (count + i >= width):
                        break
                    if (pix[i + count, j] != 0):
                        count += 1
                    else:
                        if count >= 30:
                            count = 0
                            break
                        else:
                            flag = True
                            count = 0
                            break
                    if count + 1 == steps:
                        flag = True

                # if right searching didn't success then break
                if flag == True:
                    flag = False
                    continue
                else:  # if its limit of spots > return image
                    if (c <= spots_amount):
                        c += 1
                    else:
                        return img_tmp

                # make the spots
                count = 0
                j -= 0  # for independency
                while (count != 5):
                    rand2 = random.randint(5, 6)
                    for a in range(0, rand2):
                        pix[i + a, j] = 0
                        pix_tmp[i + a, j] = blackPix
                    j -= 1
                    count += 1


    return img_tmp

