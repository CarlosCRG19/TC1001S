from tkinter import *
import cv2
import numpy as np
from tkinter.filedialog import *
from PIL import Image, ImageTk

def sharp_filter():
    arr_new = cv2.filter2D(arr,-1,np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]))
    canvas.image2 = Image.fromarray(cv2.cvtColor(arr_new,cv2.COLOR_BGR2RGB))
    img_new = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(arr_new,cv2.COLOR_BGR2RGB)))
    canvas.itemconfigure(img_on_canvas, image=img_new)
    canvas.image = img_new

def detect_edges():
    arr_new = cv2.filter2D(arr,-1,np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]))
    canvas.image2 = Image.fromarray(cv2.cvtColor(arr_new,cv2.COLOR_BGR2RGB))
    img_new = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(arr_new,cv2.COLOR_BGR2RGB)))
    canvas.itemconfigure(img_on_canvas, image=img_new)
    canvas.image = img_new
    

def blur():
    arr_new = cv2.blur(arr,(5,5))
    canvas.image2 = Image.fromarray(cv2.cvtColor(arr_new,cv2.COLOR_BGR2RGB))
    img_new = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(arr_new,cv2.COLOR_BGR2RGB)))
    canvas.itemconfigure(img_on_canvas, image=img_new)
    canvas.image = img_new

def UploadAction(event=None):
    filename = askopenfilename()
    img = cv2.imread(filename)
    return img 

def save():
    canvas.image2.save('final.png')

root = Tk() 
arr = UploadAction()
img = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(arr,cv2.COLOR_BGR2RGB)))
canvas = Canvas(root,width=img.width(),height=img.height())
canvas.grid(row=0, column=0)
img_on_canvas = canvas.create_image(20,20, anchor="nw", image=img)
root.geometry(f"{img.width()+30}x{img.height()+60}")
menu = Menu(root) 
root.config(menu=menu) 
root.title('Image Lab') 
basicFilterMenu = Menu(menu)
menu.add_cascade(label='Basic Filters', menu=basicFilterMenu) 
basicFilterMenu.add_command(label='Sharpen',command=sharp_filter) 
basicFilterMenu.add_command(label='Blur', command=blur) 
basicFilterMenu.add_command(label='Show edges', command=detect_edges)
colorFilterMenu = Menu(menu)
menu.add_cascade(label='Color Filters', menu=colorFilterMenu) 
colorFilterMenu.add_command(label='Red tint')
colorFilterMenu.add_command(label='Green tint')
colorFilterMenu.add_command(label='Blue tint')
colorFilterMenu.add_command(label='Custom tint...')
button = Button(root, text='Save image', width=25, command=save) 
button.grid(row=1,column=0)
root.mainloop() 

