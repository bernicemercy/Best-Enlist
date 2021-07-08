import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
canvas = tk.Canvas(root,width=300,height = 300,bg='white')
canvas.pack()

label = tk.Label(root,text='JPG to PNG converter',bg='white',fg ='#c91733',font=('helvetica', 12, 'bold'))
label.config()
canvas.create_window(150,30,window=label)

def getJPG():
    global img
    import_file_path = filedialog.askopenfilename()
    img = Image.open(import_file_path)

browse_jpg = tk.Button(text="Select JPG",command = getJPG,bg='#030133',fg = 'white',font=('helvetica', 12, 'bold'))
canvas.create_window(150,100,window=browse_jpg)

def convert():
    global img
    export_file_path = filedialog.asksaveasfilename(defaultextension = '.png')
    img.save(export_file_path)

saveasbutton = tk.Button(text="Convert JPG to PNG", command=convert, bg='#030133', fg='white', font=('helvetica', 12, 'bold'))
canvas.create_window(150, 150, window=saveasbutton)
root.mainloop()
