import cv2
import copy
import numpy as np
import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import filedialog as fd 

# ------------------
# -- FILTERS CODE --
# ------------------

# Basic Filters
# -------------
sharp = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
edges = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

def basic_filters(filter):
    global modifiable_image

    if filter == 'blur':
        modifiable_image = cv2.blur(modifiable_image,(5,5))
    else:
        modifiable_image  = cv2.filter2D(modifiable_image, -1, filter)

    canvas.image_tk = ImageTk.PhotoImage(image=Image.fromarray(cv2.resize(modifiable_image , maxsize)))
    # configure the canvas item to use this image
    canvas.itemconfigure(image_id, image=canvas.image_tk)


# Color Filters
# ------------   

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

def color_filter(filter):
    global modifiable_image
    filter_frame = np.full((modifiable_image.shape), filter, np.uint8)
    print(filter_frame) 
    filtered_image = cv2.add(modifiable_image, filter_frame)
    filtered_image = cv2.addWeighted(filtered_image, 0.8, filter_frame, 0.2, 0)

    canvas.image_tk = ImageTk.PhotoImage(image=Image.fromarray(cv2.resize(filtered_image , maxsize)))
    canvas.itemconfigure(image_id, image=canvas.image_tk)

# --------------
# -- GUI CODE --
# --------------

# Interface and Image Uploading
# -----------------------------

def upload_image():
    """
    Function called by the Browse button. It opens the file explorer and asks you to select a png or jpeg file 
    (actually, only this type of files are displayed on the file explorer). 
    After that, it reads the file and stores it in the image variable.
    """
    global image 
    global modifiable_image

    browse_text.set("Loading...") 
    filepath = fd.askopenfile(filetypes=(('image files', '.png'), ('image files', '.jpg'))) # filedialog function to open a file, it will only accept png or jpg images
    if filepath:
        instructions_text.set('Image Selected')
        browse_text.set('Select Image')
        print('image successfully loaded')
        image = cv2.imread(filepath.name)
        modifiable_image = copy.copy(image)

        # create the image object, and save it so that it
        # won't get deleted by the garbage collector
        canvas.image_tk = ImageTk.PhotoImage(image=Image.fromarray(cv2.resize(modifiable_image, maxsize)))

        # configure the canvas item to use this image
        canvas.itemconfigure(image_id, image=canvas.image_tk)

# interface
root = tk.Tk()
root.geometry('400x400')
root.title('Awesome Image Filters')

# canvas creation
canvas = tk.Canvas(root)
canvas.grid(column=0, row=0, columnspan=3)

# image variables
image = None
modifiable_image = None # copy of main image so it can be changed without altering the latter
maxsize = (350, 250)
image_id = canvas.create_image(20, 20, anchor='nw')

# instructions
instructions_text = tk.StringVar()
instructions = tk.Label(root, textvariable=instructions_text, font='Raleway')
instructions_text.set('Select a PNG or a JPEG file')
instructions.grid(column=0, row=2, columnspan=3)

# browse button and image loading
browse_text = tk.StringVar()
browse_image = tk.Button(root, width=12, height=1, command=upload_image, textvariable=browse_text, font='Raleway') # when the button is pressed, it opens the file explorer
browse_text.set('Select Image')
browse_image.grid(column=0, row=3)
root.grid_rowconfigure(1, minsize=10)

# save image button
save_button = tk.Button(root, width=10, height=1, text='Save Image', font='Raleway')
save_button.grid(column=1, row=3)

# exit button 
exit_button = tk.Button(root, command=lambda: exit(), text='Exit', font='Raleway')
exit_button.grid(column=2, row=3)


# Menu and filter application 
# ---------------------------

# main menu
menu = tk.Menu(root) 
root.config(menu=menu) 

# basic filters menu
basic_filters_menu = tk.Menu(menu)
menu.add_cascade(label='Basic Filters', menu=basic_filters_menu) 

basic_filters_menu.add_command(label='Sharpen', command=lambda:basic_filters(sharp)) 
basic_filters_menu.add_command(label='Blur', command=lambda:basic_filters('blur')) 
basic_filters_menu.add_command(label='Show edges', command=lambda:basic_filters(edges))

# color filters menu
color_filters_menu = tk.Menu(menu)
menu.add_cascade(label='Color Filters', menu=color_filters_menu) 
color_filters_menu.add_command(label='Red tint', command=lambda:color_filter(red))
color_filters_menu.add_command(label='Green tint', command=lambda:color_filter(green))
color_filters_menu.add_command(label='Blue tint', command=lambda:color_filter(blue))

root.mainloop() 

