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

    display_image(modifiable_image)


# Color Filters
# ------------   

def color_filter(r_slider, g_slider, b_slider, saturation):
    global modifiable_image

    rgb = (r_slider, g_slider, b_slider)
    beta = saturation / 100.0
    alpha = 1 - beta

    filter_frame = np.full((modifiable_image.shape), rgb, np.uint8)
    filtered_image = cv2.addWeighted(modifiable_image, alpha, filter_frame, beta, 0)

    display_image(filtered_image)

# ---------------------
# -- IMAGE FUNCTIONS --
# ---------------------

def display_image(displayable):
    # create the image object, and save it so that it
    # won't get deleted by the garbage collector
    canvas.image_tk = ImageTk.PhotoImage(image=Image.fromarray(cv2.resize(displayable, maxsize)))

    # configure the canvas item to use this image
    canvas.itemconfigure(image_id, image=canvas.image_tk)


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
        browse_text.set('Select')
        print('image successfully loaded')
        image = cv2.imread(filepath.name)
        modifiable_image = copy.copy(image)

        display_image(modifiable_image)
        
def reset_image():
    global modifiable_image
    global image

    instructions_text.set('Image Reseted')
    modifiable_image = copy.copy(image)
    display_image(modifiable_image)

def save_image():
    instructions_text.set('Image Saved')
    canvas.image_tk._PhotoImage__photo.write('filtered_image.png', format='png')


# --------------
# -- GUI CODE --
# --------------

# Interface and Image Uploading
# -----------------------------


# interface
root = tk.Tk()
root.geometry('575x365')
root.title('Awesome Image Filters')

# canvas creation
canvas = tk.Canvas(root)
canvas.grid(column=0, row=0, columnspan=3, rowspan=5)

# image variables
image = None
modifiable_image = None # copy of main image so it can be changed without altering the latter
maxsize = (350, 250)
image_id = canvas.create_image(20, 20, anchor='nw')

# instructions
instructions_text = tk.StringVar()
instructions = tk.Label(root, textvariable=instructions_text, font='Raleway')
instructions_text.set('Select a PNG or a JPEG file')
instructions.grid(column=0, row=6, columnspan=3)

# browse button and image loading
browse_text = tk.StringVar()
browse_image = tk.Button(root, width=9, height=1, command=upload_image, textvariable=browse_text, font='Raleway') # when the button is pressed, it opens the file explorer
browse_text.set('Select')
browse_image.grid(column=0, row=7)
root.grid_rowconfigure(5, minsize=10)

# reset image
reset_text = tk.StringVar()
reset_image = tk.Button(root, width=9, height=1, command=reset_image, textvariable=reset_text, font='Raleway') # when the button is pressed, it opens the file explorer
reset_text.set('Reset')
reset_image.grid(column=1, row=7)

# save image button
save_button = tk.Button(root, width=9, height=1, command=save_image, text='Save', font='Raleway')
save_button.grid(column=2, row=7)


# Menu and filter application 
# ---------------------------

# RGB sliders
rgb_label = tk.Label(root, text='RGB Filter', font='Raleway')
rgb_label.grid(column=4, row=0, columnspan=2)

# labels
red_label = tk.Label(root, text='R')
red_label.grid(column=4, row=1)
green_label = tk.Label(root, text='G')
green_label.grid(column=4, row=2)
blue_label = tk.Label(root, text='B')
blue_label.grid(column=4, row=3)

# sliders
red_slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL)
red_slider.grid(column=5, row=1)
green_slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL)
green_slider.grid(column=5, row=2)
blue_slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL)
blue_slider.grid(column=5, row=3)

# saturation slider
saturation_label = tk.Label(root, text='SATURATION')
saturation_label.grid(column=4, row=4)
saturation_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
saturation_slider.grid(column=5, row=4)

# apply color filter 
saturation = saturation_slider.get()
rgb_button = tk.Button(root, width=9, height=1, command=lambda: color_filter(red_slider.get(), green_slider.get(), blue_slider.get(), saturation_slider.get()), text='Apply', font='Raleway')
rgb_button.grid(column=5, row=7)

# main menu
menu = tk.Menu(root) 
root.config(menu=menu) 

# basic filters menu
basic_filters_menu = tk.Menu(menu)
menu.add_cascade(label='Basic Filters', menu=basic_filters_menu) 

basic_filters_menu.add_command(label='Sharpen', command=lambda:basic_filters(sharp)) 
basic_filters_menu.add_command(label='Blur', command=lambda:basic_filters('blur')) 
basic_filters_menu.add_command(label='Show edges', command=lambda:basic_filters(edges))

root.mainloop() 


