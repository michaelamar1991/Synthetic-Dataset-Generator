from tkinter import *
from img_test import *

root = Tk()

# Frames
topFrame = Frame(root)
topFrame.pack()

runFrame = Frame(root)
runFrame.pack(side=BOTTOM)

anglesFrame = Frame(root)
anglesFrame.pack(side=BOTTOM)

fontsizeFrame = Frame(root)
fontsizeFrame.pack(side=BOTTOM)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# Entry's
textEntry = Entry(topFrame)

fontsizeMinEntry = Entry(fontsizeFrame, width=3)
fontsizeMaxEntry = Entry(fontsizeFrame, width=3)
fontjumpsEntry = Entry(fontsizeFrame, width=3)

angleMinEntry = Entry(anglesFrame, width=3)
angleMaxEntry = Entry(anglesFrame, width=3)
anglejumpsEntry = Entry(anglesFrame, width=3)

# ListBox
fontlistBox = Listbox(bottomFrame)
for item in ["Dana Yad Alef Alef Alef Normal.ttf", "Ellinia CLM Light Italic.ttf", "GYADBR.TTF", "GYADL.TTF", "GYADXL.TTF", "Motek.ttf", "Yoav Cursive.ttf"]:
    fontlistBox.insert(END, item)

# for item in ["Brush Script.ttf", "Bradley Hand Bold.ttf", "Herculanum.ttf", "MarkerFelt.ttc"]:
#    fontlistBox.insert(END, item)

# Labels
titleLabel = Label(topFrame, text="Image Processing Test", bg="Light Blue", fg="Blue")

textLabel = Label(topFrame, text="Text: ")

fontLabel = Label(bottomFrame, text="Font: ")

fontsizeLabel = Label(fontsizeFrame, text="Font Sizes: ")
fsizeToLabel = Label(fontsizeFrame, text="To ")
fjumpsLabel = Label(fontsizeFrame, text="Jumps of: ")

anglesLabel = Label(anglesFrame, text="Angles: ")
anglesToLabel = Label(anglesFrame, text="To ")
ajumpsLabel = Label(anglesFrame, text="Jumps of: ")


def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


def prepare():
    text = textEntry.get()
    print(text)
    txt = reverse(text)

    fontname = fontlistBox.get(fontlistBox.curselection())
    print(fontname)

    fontsizes = [int(fontsizeMinEntry.get())]
    tmp = int(fontsizeMinEntry.get())
    while tmp < (int(fontsizeMaxEntry.get()) - int(fontjumpsEntry.get())):
        tmp += int(fontjumpsEntry.get())
        fontsizes.append(tmp)
    print(fontsizes)

    angles = [int(angleMinEntry.get())]
    tmp = int(angleMinEntry.get())
    while tmp < (int(angleMaxEntry.get()) - int(anglejumpsEntry.get())):
        tmp += int(anglejumpsEntry.get())
        angles.append(tmp)
    print(angles)
    run(text, fontname, fontsizes, angles)


# Buttons
runBtn = Button(runFrame, text="RUN", fg="blue", bg="yellow", command=prepare)

# Pack Everything
titleLabel.pack(side=TOP)
textLabel.pack(side=LEFT)
textEntry.pack(side=LEFT)
fontLabel.pack(side=LEFT)
runBtn.pack(side=BOTTOM)
fontsizeLabel.pack(side=LEFT)
fontsizeMinEntry.pack(side=LEFT)
fsizeToLabel.pack(side=LEFT)
fontsizeMaxEntry.pack(side=LEFT)
fjumpsLabel.pack(side=LEFT)
fontjumpsEntry.pack(side=LEFT)

anglesLabel.pack(side=LEFT)
angleMinEntry.pack(side=LEFT)
anglesToLabel.pack(side=LEFT)
angleMaxEntry.pack(side=LEFT)
ajumpsLabel.pack(side=LEFT)
anglejumpsEntry.pack(side=LEFT)

fontlistBox.pack(side=BOTTOM)

root.mainloop()



