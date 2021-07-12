import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

root = tk.Tk()

canvas1 = tk.Canvas(root,width=550,height=550,bg="grey",relief="raised")
canvas1.pack()

label1 = tk.Label(root,text='Image conversion From JPG To png',bg="royalblue")
label1.config(font=('Bradley Hand ITC',20,'bold'))
canvas1.create_window(250,40,window=label1)


def getJPG():
    global  im1
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)

browseButton_JPG = tk.Button(text='   IMPORT JPG FILE    ',command=getJPG, bg ='royalblue', fg='white',
                             font=('',12,'bold'))
canvas1.create_window(250,200,window=browseButton_JPG)


def convertTOPNG():
    global im1

    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path)

saveasButton_PNG = tk.Button(text='COnvert JPG to PNG',command = convertTOPNG,bg = 'royalblue', fg='white',
                             font=('',12,'bold'))
canvas1.create_window(250,280,window=saveasButton_PNG)

root.mainloop()