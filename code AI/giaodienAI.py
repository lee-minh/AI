from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title('shin')
root.geometry("860x430") #set khung hình
root.iconbitmap('logo.ico') #set logo

# chèn background
load = Image.open('background.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root, image = render)
img.place(x=0, y=0)

name = Label(root, text="shin AI", fg="#000099", bd=0, bg="#06061E")
name.config(font = ("Transformers Movie.ttf",30))
name.pack(pady = 10)


root.mainloop()