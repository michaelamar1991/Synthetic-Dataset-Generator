import sys
from Run import *
from tkinter import filedialog
from PIL import Image

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Project_support

txtFlag = 0
fileFlag = 0
revFlag = 0
filePath = ""
dirPath = ""

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    Project_support.set_Tk_var()
    top = DatasetGenerator (root)
    Project_support.init(root, top)
    root.mainloop()

w = None
def create_DatasetGenerator(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    Project_support.set_Tk_var()
    top = DatasetGenerator (w)
    Project_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_DatasetGenerator():
    global w
    w.destroy()
    w = None

class DatasetGenerator:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("714x493+251+71")
        top.title("Synthetic Data Set Generator")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.MainFrame = tk.Frame(top)
        self.MainFrame.place(relx=0.014, rely=0.152, relheight=0.822
                , relwidth=0.973)
        self.MainFrame.configure(relief='groove')
        self.MainFrame.configure(borderwidth="2")
        self.MainFrame.configure(relief="groove")
        self.MainFrame.configure(background="#d9d9d9")
        self.MainFrame.configure(highlightbackground="#d9d9d9")
        self.MainFrame.configure(highlightcolor="black")
        self.MainFrame.configure(width=695)

        self.TextInputCheck = tk.Checkbutton(self.MainFrame, command=txtFlagChange)
        self.TextInputCheck.place(relx=0.014, rely=0.025, relheight=0.054
                , relwidth=0.128)
        self.TextInputCheck.configure(activebackground="#ececec")
        self.TextInputCheck.configure(activeforeground="#000000")
        self.TextInputCheck.configure(background="#d9d9d9")
        self.TextInputCheck.configure(foreground="#000000")
        self.TextInputCheck.configure(highlightbackground="#d9d9d9")
        self.TextInputCheck.configure(highlightcolor="black")
        self.TextInputCheck.configure(justify='left')
        self.TextInputCheck.configure(text='''Text Input''')

        self.FileInputCheck = tk.Checkbutton(self.MainFrame, command=fileFlagChange)
        self.FileInputCheck.place(relx=0.014, rely=0.099, relheight=0.054
                , relwidth=0.127)
        self.FileInputCheck.configure(activebackground="#ececec")
        self.FileInputCheck.configure(activeforeground="#000000")
        self.FileInputCheck.configure(background="#d9d9d9")
        self.FileInputCheck.configure(foreground="#000000")
        self.FileInputCheck.configure(highlightbackground="#d9d9d9")
        self.FileInputCheck.configure(highlightcolor="black")
        self.FileInputCheck.configure(justify='left')
        self.FileInputCheck.configure(text='''File Input''')

        self.TSeparator1 = ttk.Separator(self.MainFrame)
        self.TSeparator1.place(relx=0.151, rely=0.025, relheight=0.123)
        self.TSeparator1.configure(orient="vertical")

        self.textEntry = tk.Entry(self.MainFrame)
        self.textEntry.place(relx=0.173, rely=0.025,height=27, relwidth=0.291)
        self.textEntry.configure(background="white")
        self.textEntry.configure(font="TkFixedFont")
        self.textEntry.configure(foreground="#000000")
        self.textEntry.configure(highlightbackground="#d9d9d9")
        self.textEntry.configure(highlightcolor="black")
        self.textEntry.configure(insertbackground="black")
        self.textEntry.configure(selectbackground="#c4c4c4")
        self.textEntry.configure(selectforeground="black")

        self.OpenFileBtn = tk.Button(self.MainFrame, command=openFile)
        self.OpenFileBtn.place(relx=0.165, rely=0.099, height=22, width=51)
        self.OpenFileBtn.configure(activebackground="#ececec")
        self.OpenFileBtn.configure(activeforeground="#000000")
        self.OpenFileBtn.configure(background="#d9d9d9")
        self.OpenFileBtn.configure(foreground="#000000")
        self.OpenFileBtn.configure(highlightbackground="#d9d9d9")
        self.OpenFileBtn.configure(highlightcolor="black")
        self.OpenFileBtn.configure(text='''Open''')

        self.FontLabel = tk.Label(self.MainFrame)
        self.FontLabel.place(relx=0.014, rely=0.173, height=24, width=39)
        self.FontLabel.configure(activebackground="#f9f9f9")
        self.FontLabel.configure(activeforeground="black")
        self.FontLabel.configure(background="#d9d9d9")
        self.FontLabel.configure(foreground="#000000")
        self.FontLabel.configure(highlightbackground="#d9d9d9")
        self.FontLabel.configure(highlightcolor="black")
        self.FontLabel.configure(text='''Font :''')

        self.FontListbox = tk.Listbox(self.MainFrame)
        for item in ["Dana Yad Alef Alef Alef Normal.ttf", "Ellinia CLM Light Italic.ttf", "GYADBR.TTF", "GYADL.TTF",
                     "GYADXL.TTF", "Motek.ttf", "Yoav Cursive.ttf", "GveretLevinAlefAlefAlef-Regular.otf",
                     "keteryg-medium-webfont.ttf", "keteryg-mediumoblique-webfont.ttf", "KtavYadCLM-MediumItalic.otf",
                     "KtavYadCLM-BoldItalic.otf", "MakabiYG.ttf", "ShmulikCLM.ttf", "stamashkenazclm-webfont.ttf",
                     "stamsefaradclm-webfont.ttf", "TsMatka-Regular.ttf", "YiddishkeitAlefAlefAlef-Bold.otf", "shmuel.ttf",
                     "Miriwin.ttf", "BENGURIO.TTF"]:
            x = 1
            self.FontListbox.insert(x, item)
            x += 1

        self.FontListbox.place(relx=0.086, rely=0.173, relheight=0.385
                , relwidth=0.377)
        self.FontListbox.configure(background="white")
        self.FontListbox.configure(font="TkFixedFont")
        self.FontListbox.configure(foreground="#000000")
        self.FontListbox.configure(highlightbackground="#d9d9d9")
        self.FontListbox.configure(highlightcolor="black")
        self.FontListbox.configure(selectbackground="#c4c4c4")
        self.FontListbox.configure(selectforeground="black")
        self.FontListbox.configure(width=262)

        self.FontSizesLabel = tk.Label(self.MainFrame)
        self.FontSizesLabel.place(relx=0.0, rely=0.593, height=24, width=86)
        self.FontSizesLabel.configure(activebackground="#f9f9f9")
        self.FontSizesLabel.configure(activeforeground="black")
        self.FontSizesLabel.configure(background="#d9d9d9")
        self.FontSizesLabel.configure(foreground="#000000")
        self.FontSizesLabel.configure(highlightbackground="#d9d9d9")
        self.FontSizesLabel.configure(highlightcolor="black")
        self.FontSizesLabel.configure(text='''Font Sizes :''')

        self.fontsizeMinEntry = tk.Entry(self.MainFrame)
        self.fontsizeMinEntry.place(relx=0.122, rely=0.593, height=27
                , relwidth=0.06)
        self.fontsizeMinEntry.configure(background="white")
        self.fontsizeMinEntry.configure(font="TkFixedFont")
        self.fontsizeMinEntry.configure(foreground="#000000")
        self.fontsizeMinEntry.configure(highlightbackground="#d9d9d9")
        self.fontsizeMinEntry.configure(highlightcolor="black")
        self.fontsizeMinEntry.configure(insertbackground="black")
        self.fontsizeMinEntry.configure(selectbackground="#c4c4c4")
        self.fontsizeMinEntry.configure(selectforeground="black")

        self.fsizeToLabel = tk.Label(self.MainFrame)
        self.fsizeToLabel.place(relx=0.187, rely=0.593, height=24, width=26)
        self.fsizeToLabel.configure(activebackground="#f9f9f9")
        self.fsizeToLabel.configure(activeforeground="black")
        self.fsizeToLabel.configure(background="#d9d9d9")
        self.fsizeToLabel.configure(foreground="#000000")
        self.fsizeToLabel.configure(highlightbackground="#d9d9d9")
        self.fsizeToLabel.configure(highlightcolor="black")
        self.fsizeToLabel.configure(text='''To''')

        self.fontsizeMaxEntry = tk.Entry(self.MainFrame)
        self.fontsizeMaxEntry.place(relx=0.223, rely=0.593, height=27
                , relwidth=0.06)
        self.fontsizeMaxEntry.configure(background="white")
        self.fontsizeMaxEntry.configure(font="TkFixedFont")
        self.fontsizeMaxEntry.configure(foreground="#000000")
        self.fontsizeMaxEntry.configure(highlightbackground="#d9d9d9")
        self.fontsizeMaxEntry.configure(highlightcolor="black")
        self.fontsizeMaxEntry.configure(insertbackground="black")
        self.fontsizeMaxEntry.configure(selectbackground="#c4c4c4")
        self.fontsizeMaxEntry.configure(selectforeground="black")

        self.fjumpsLabel = tk.Label(self.MainFrame)
        self.fjumpsLabel.place(relx=0.288, rely=0.593, height=24, width=72)
        self.fjumpsLabel.configure(activebackground="#f9f9f9")
        self.fjumpsLabel.configure(activeforeground="black")
        self.fjumpsLabel.configure(background="#d9d9d9")
        self.fjumpsLabel.configure(foreground="#000000")
        self.fjumpsLabel.configure(highlightbackground="#d9d9d9")
        self.fjumpsLabel.configure(highlightcolor="black")
        self.fjumpsLabel.configure(text='''Jumps Of :''')

        self.fontJumpsEntry = tk.Entry(self.MainFrame)
        self.fontJumpsEntry.place(relx=0.396, rely=0.593, height=27
                , relwidth=0.06)
        self.fontJumpsEntry.configure(background="white")
        self.fontJumpsEntry.configure(font="TkFixedFont")
        self.fontJumpsEntry.configure(foreground="#000000")
        self.fontJumpsEntry.configure(highlightbackground="#d9d9d9")
        self.fontJumpsEntry.configure(highlightcolor="black")
        self.fontJumpsEntry.configure(insertbackground="black")
        self.fontJumpsEntry.configure(selectbackground="#c4c4c4")
        self.fontJumpsEntry.configure(selectforeground="black")

        self.anglesLabel = tk.Label(self.MainFrame)
        self.anglesLabel.place(relx=0.0, rely=0.691, height=24, width=62)
        self.anglesLabel.configure(activebackground="#f9f9f9")
        self.anglesLabel.configure(activeforeground="black")
        self.anglesLabel.configure(background="#d9d9d9")
        self.anglesLabel.configure(foreground="#000000")
        self.anglesLabel.configure(highlightbackground="#d9d9d9")
        self.anglesLabel.configure(highlightcolor="black")
        self.anglesLabel.configure(text='''Angles :''')

        self.angleMinEntry = tk.Entry(self.MainFrame)
        self.angleMinEntry.place(relx=0.122, rely=0.691, height=27
                , relwidth=0.06)
        self.angleMinEntry.configure(background="white")
        self.angleMinEntry.configure(font="TkFixedFont")
        self.angleMinEntry.configure(foreground="#000000")
        self.angleMinEntry.configure(highlightbackground="#d9d9d9")
        self.angleMinEntry.configure(highlightcolor="black")
        self.angleMinEntry.configure(insertbackground="black")
        self.angleMinEntry.configure(selectbackground="#c4c4c4")
        self.angleMinEntry.configure(selectforeground="black")

        self.anglesToLabel = tk.Label(self.MainFrame)
        self.anglesToLabel.place(relx=0.187, rely=0.704, height=24, width=26)
        self.anglesToLabel.configure(activebackground="#f9f9f9")
        self.anglesToLabel.configure(activeforeground="black")
        self.anglesToLabel.configure(background="#d9d9d9")
        self.anglesToLabel.configure(foreground="#000000")
        self.anglesToLabel.configure(highlightbackground="#d9d9d9")
        self.anglesToLabel.configure(highlightcolor="black")
        self.anglesToLabel.configure(text='''To''')

        self.angleMaxEntry = tk.Entry(self.MainFrame)
        self.angleMaxEntry.place(relx=0.223, rely=0.691, height=27
                , relwidth=0.06)
        self.angleMaxEntry.configure(background="white")
        self.angleMaxEntry.configure(font="TkFixedFont")
        self.angleMaxEntry.configure(foreground="#000000")
        self.angleMaxEntry.configure(highlightbackground="#d9d9d9")
        self.angleMaxEntry.configure(highlightcolor="black")
        self.angleMaxEntry.configure(insertbackground="black")
        self.angleMaxEntry.configure(selectbackground="#c4c4c4")
        self.angleMaxEntry.configure(selectforeground="black")

        self.ajumpsLabel = tk.Label(self.MainFrame)
        self.ajumpsLabel.place(relx=0.288, rely=0.691, height=24, width=80)
        self.ajumpsLabel.configure(activebackground="#f9f9f9")
        self.ajumpsLabel.configure(activeforeground="black")
        self.ajumpsLabel.configure(background="#d9d9d9")
        self.ajumpsLabel.configure(foreground="#000000")
        self.ajumpsLabel.configure(highlightbackground="#d9d9d9")
        self.ajumpsLabel.configure(highlightcolor="black")
        self.ajumpsLabel.configure(text='''Jumps Of :''')

        self.angleJumpsEntry = tk.Entry(self.MainFrame)
        self.angleJumpsEntry.place(relx=0.403, rely=0.691, height=27
                , relwidth=0.06)
        self.angleJumpsEntry.configure(background="white")
        self.angleJumpsEntry.configure(font="TkFixedFont")
        self.angleJumpsEntry.configure(foreground="#000000")
        self.angleJumpsEntry.configure(highlightbackground="#d9d9d9")
        self.angleJumpsEntry.configure(highlightcolor="black")
        self.angleJumpsEntry.configure(insertbackground="black")
        self.angleJumpsEntry.configure(selectbackground="#c4c4c4")
        self.angleJumpsEntry.configure(selectforeground="black")

        self.DegredationsFrame = tk.Frame(self.MainFrame)
        self.DegredationsFrame.place(relx=0.468, rely=0.025, relheight=0.753
                , relwidth=0.525)
        self.DegredationsFrame.configure(relief='groove')
        self.DegredationsFrame.configure(borderwidth="2")
        self.DegredationsFrame.configure(relief="groove")
        self.DegredationsFrame.configure(background="#d9d9d9")
        self.DegredationsFrame.configure(highlightbackground="#d9d9d9")
        self.DegredationsFrame.configure(highlightcolor="black")
        self.DegredationsFrame.configure(width=365)

        self.DegredationsTitle = tk.Label(self.DegredationsFrame)
        self.DegredationsTitle.place(relx=0.356, rely=0.0, height=24, width=97)
        self.DegredationsTitle.configure(activebackground="#f9f9f9")
        self.DegredationsTitle.configure(activeforeground="black")
        self.DegredationsTitle.configure(background="#d9d9d9")
        self.DegredationsTitle.configure(foreground="#000000")
        self.DegredationsTitle.configure(highlightbackground="#d9d9d9")
        self.DegredationsTitle.configure(highlightcolor="black")
        self.DegredationsTitle.configure(text='''Degredations''')

        self.DisconnectionScale = tk.Scale(self.DegredationsFrame, from_=0.0, to=100.0)
        self.DisconnectionScale.place(relx=0.466, rely=0.082, relwidth=0.504
                , relheight=0.0, height=39, bordermode='ignore')
        self.DisconnectionScale.configure(activebackground="#ececec")
        self.DisconnectionScale.configure(background="#d9d9d9")
        self.DisconnectionScale.configure(font="TkTextFont")
        self.DisconnectionScale.configure(foreground="#000000")
        self.DisconnectionScale.configure(highlightbackground="#d9d9d9")
        self.DisconnectionScale.configure(highlightcolor="black")
        self.DisconnectionScale.configure(orient="horizontal")
        self.DisconnectionScale.configure(troughcolor="#d9d9d9")

        self.OverlappingScale = tk.Scale(self.DegredationsFrame, from_=0.0, to=100.0)
        self.OverlappingScale.place(relx=0.466, rely=0.23, relwidth=0.504
                , relheight=0.0, height=39, bordermode='ignore')
        self.OverlappingScale.configure(activebackground="#ececec")
        self.OverlappingScale.configure(background="#d9d9d9")
        self.OverlappingScale.configure(font="TkTextFont")
        self.OverlappingScale.configure(foreground="#000000")
        self.OverlappingScale.configure(highlightbackground="#d9d9d9")
        self.OverlappingScale.configure(highlightcolor="black")
        self.OverlappingScale.configure(orient="horizontal")
        self.OverlappingScale.configure(troughcolor="#d9d9d9")

        self.IndependentScale = tk.Scale(self.DegredationsFrame, from_=0.0, to=100.0)
        self.IndependentScale.place(relx=0.466, rely=0.361, relwidth=0.504
                , relheight=0.0, height=39, bordermode='ignore')
        self.IndependentScale.configure(activebackground="#ececec")
        self.IndependentScale.configure(background="#d9d9d9")
        self.IndependentScale.configure(font="TkTextFont")
        self.IndependentScale.configure(foreground="#000000")
        self.IndependentScale.configure(highlightbackground="#d9d9d9")
        self.IndependentScale.configure(highlightcolor="black")
        self.IndependentScale.configure(orient="horizontal")
        self.IndependentScale.configure(troughcolor="#d9d9d9")

        self.NoiseScale = tk.Scale(self.DegredationsFrame, from_=0.0, to=100.0)
        self.NoiseScale.place(relx=0.466, rely=0.525, relwidth=0.504
                , relheight=0.0, height=39, bordermode='ignore')
        self.NoiseScale.configure(activebackground="#ececec")
        self.NoiseScale.configure(background="#d9d9d9")
        self.NoiseScale.configure(font="TkTextFont")
        self.NoiseScale.configure(foreground="#000000")
        self.NoiseScale.configure(highlightbackground="#d9d9d9")
        self.NoiseScale.configure(highlightcolor="black")
        self.NoiseScale.configure(orient="horizontal")
        self.NoiseScale.configure(troughcolor="#d9d9d9")

        self.BlurScale = tk.Scale(self.DegredationsFrame, from_=0.0, to=100.0)
        self.BlurScale.place(relx=0.466, rely=0.656, relwidth=0.504
                , relheight=0.0, height=39, bordermode='ignore')
        self.BlurScale.configure(activebackground="#ececec")
        self.BlurScale.configure(background="#d9d9d9")
        self.BlurScale.configure(font="TkTextFont")
        self.BlurScale.configure(foreground="#000000")
        self.BlurScale.configure(highlightbackground="#d9d9d9")
        self.BlurScale.configure(highlightcolor="black")
        self.BlurScale.configure(orient="horizontal")
        self.BlurScale.configure(troughcolor="#d9d9d9")

        self.YellowScale = tk.Scale(self.DegredationsFrame, from_=0.0, to=100.0)
        self.YellowScale.place(relx=0.466, rely=0.82, relwidth=0.504
                , relheight=0.0, height=39, bordermode='ignore')
        self.YellowScale.configure(activebackground="#ececec")
        self.YellowScale.configure(background="#d9d9d9")
        self.YellowScale.configure(font="TkTextFont")
        self.YellowScale.configure(foreground="#000000")
        self.YellowScale.configure(highlightbackground="#d9d9d9")
        self.YellowScale.configure(highlightcolor="black")
        self.YellowScale.configure(orient="horizontal")
        self.YellowScale.configure(troughcolor="#d9d9d9")

        self.DissconectionLabel = tk.Label(self.DegredationsFrame)
        self.DissconectionLabel.place(relx=0.014, rely=0.131, height=24
                , width=146)
        self.DissconectionLabel.configure(background="#d9d9d9")
        self.DissconectionLabel.configure(foreground="#000000")
        self.DissconectionLabel.configure(text='''Disconnection Spot :''')
        self.DissconectionLabel.configure(width=146)

        self.OverlappingLabel = tk.Label(self.DegredationsFrame)
        self.OverlappingLabel.place(relx=0.027, rely=0.295, height=24, width=130)

        self.OverlappingLabel.configure(background="#d9d9d9")
        self.OverlappingLabel.configure(foreground="#000000")
        self.OverlappingLabel.configure(text='''Overlapping Spot :''')

        self.IndependentLabel = tk.Label(self.DegredationsFrame)
        self.IndependentLabel.place(relx=0.014, rely=0.426, height=24, width=143)

        self.IndependentLabel.configure(background="#d9d9d9")
        self.IndependentLabel.configure(foreground="#000000")
        self.IndependentLabel.configure(text='''Independent Spot :''')
        self.IndependentLabel.configure(width=143)

        self.NoiseLabel = tk.Label(self.DegredationsFrame)
        self.NoiseLabel.place(relx=0.014, rely=0.574, height=24, width=65)
        self.NoiseLabel.configure(background="#d9d9d9")
        self.NoiseLabel.configure(foreground="#000000")
        self.NoiseLabel.configure(text='''Noise :''')
        self.NoiseLabel.configure(width=65)

        self.BlurLabel = tk.Label(self.DegredationsFrame)
        self.BlurLabel.place(relx=0.0, rely=0.721, height=24, width=64)
        self.BlurLabel.configure(background="#d9d9d9")
        self.BlurLabel.configure(foreground="#000000")
        self.BlurLabel.configure(text='''Blur :''')
        self.BlurLabel.configure(width=64)

        self.YellowLabel = tk.Label(self.DegredationsFrame)
        self.YellowLabel.place(relx=0.014, rely=0.869, height=24, width=70)
        self.YellowLabel.configure(background="#d9d9d9")
        self.YellowLabel.configure(foreground="#000000")
        self.YellowLabel.configure(text='''Yellow :''')
        self.YellowLabel.configure(width=70)

        self.InfoBtn = tk.Button(self.MainFrame, command=readme)
        self.InfoBtn.place(relx=0.029, rely=0.889, height=32, width=63)
        self.InfoBtn.configure(activebackground="#ececec")
        self.InfoBtn.configure(activeforeground="#000000")
        self.InfoBtn.configure(background="#d9d9d9")
        self.InfoBtn.configure(foreground="#000000")
        self.InfoBtn.configure(highlightbackground="#d9d9d9")
        self.InfoBtn.configure(highlightcolor="black")
        self.InfoBtn.configure(text='''Info''')

        self.SaveToBtn = tk.Button(self.MainFrame, command=openDir)
        self.SaveToBtn.place(relx=0.144, rely=0.889, height=32, width=69)
        self.SaveToBtn.configure(activebackground="#ececec")
        self.SaveToBtn.configure(activeforeground="#000000")
        self.SaveToBtn.configure(background="#d9d9d9")
        self.SaveToBtn.configure(foreground="#000000")
        self.SaveToBtn.configure(highlightbackground="#d9d9d9")
        self.SaveToBtn.configure(highlightcolor="black")
        self.SaveToBtn.configure(text='''Save To''')

        self.RunBtn = tk.Button(self.MainFrame, command=prepare)
        self.RunBtn.place(relx=0.878, rely=0.889, height=32, width=63)
        self.RunBtn.configure(activebackground="#ececec")
        self.RunBtn.configure(activeforeground="#000000")
        self.RunBtn.configure(background="#d9d9d9")
        self.RunBtn.configure(foreground="#000000")
        self.RunBtn.configure(highlightbackground="#d9d9d9")
        self.RunBtn.configure(highlightcolor="black")
        self.RunBtn.configure(text='''Run''')

        self.TitleLabel = tk.Label(top)
        self.TitleLabel.place(relx=0.322, rely=0.02, height=24, width=255)
        self.TitleLabel.configure(activebackground="#f9f9f9")
        self.TitleLabel.configure(activeforeground="black")
        self.TitleLabel.configure(background="#d9d9d9")
        self.TitleLabel.configure(foreground="#000000")
        self.TitleLabel.configure(highlightbackground="#d9d9d9")
        self.TitleLabel.configure(highlightcolor="black")
        self.TitleLabel.configure(text='''Synthetic Data Set Generator''')


def readme():
    image = Image.open('Readme.png')
    image.show()

def openDir():
    global dirPath
    root.directory = filedialog.askdirectory()
    dirPath = root.directory + "/"

def openFile():
    global filePath
    global fileFlag
    if fileFlag == 1:
        root.fileName = filedialog.askopenfilename(filetypes=(("txt File", "*.txt"), ("All files", "*.*")))
        filePath = root.fileName

def txtFlagChange():
    global txtFlag
    if txtFlag == 0:
        txtFlag = 1
    else:
        txtFlag = 0

def fileFlagChange():
    global fileFlag
    if fileFlag == 0:
        fileFlag = 1
    else:
        fileFlag = 0


def prepare():
        global fileFlag, fileFlag, txtFlag, revFlag, dirPath
        text = top.textEntry.get()
        textList = ["Synthetic Data Set Generator"]

        if txtFlag == 0 & fileFlag == 0:
            textList[0] = textList[0][::-1]
            revFlag = 1

        if txtFlag == 1:
            revFlag = 0
            textList[0] = text

        if fileFlag == 1:
            revFlag = 0
            file = open(filePath, 'r')
            textList = file.read().splitlines()

        if txtFlag == 1 & fileFlag == 1:
            revFlag = 0
            textList.append(text)

        if top.FontListbox.curselection():
            fontname = top.FontListbox.get(top.FontListbox.curselection())
        else:
            fontname = ""

        fontsizes = [int(top.fontsizeMinEntry.get())]
        tmp = int(top.fontsizeMinEntry.get())
        while tmp < (int(top.fontsizeMaxEntry.get()) - int(top.fontJumpsEntry.get())):
            tmp += int(top.fontJumpsEntry.get())
            fontsizes.append(tmp)

        angles = [int(top.angleMinEntry.get())]
        tmp = int(top.angleMinEntry.get())
        while tmp < (int(top.angleMaxEntry.get()) - int(top.angleJumpsEntry.get())):
            tmp += int(top.angleJumpsEntry.get())
            angles.append(tmp)

        dissconection = top.DisconnectionScale.get()
        overlapping = top.OverlappingScale.get()
        independent = top.IndependentScale.get()
        noise = top.NoiseScale.get()
        blur = top.BlurScale.get()
        yellow = top.YellowScale.get()
        degredations = [dissconection, overlapping, independent, noise, blur, yellow]

        savePath = dirPath

        for txt in textList:
            run(txt, fontname, fontsizes, angles, degredations, revFlag, savePath)


if __name__ == '__main__':
    root = tk.Tk()
    Project_support.set_Tk_var()
    top = DatasetGenerator(root)
    Project_support.init(root, top)
    root.mainloop()